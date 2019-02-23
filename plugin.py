import os

from sublime import packages_path
from sublime import status_message
import sublime_plugin


class TestCancelCommand(sublime_plugin.WindowCommand):

    def run(self, **kwargs):
        _run_command(self.window, 'cancel', **kwargs)


class TestFileCommand(sublime_plugin.WindowCommand):
    def run(self, **kwargs):
        _run_command(self.window, 'file', **kwargs)


class TestFileWithCoverageCommand(sublime_plugin.WindowCommand):
    def run(self, **kwargs):
        _run_command(self.window, 'file_with_coverage', **kwargs)


class TestLastCommand(sublime_plugin.WindowCommand):
    def run(self, **kwargs):
        _run_command(self.window, 'last', **kwargs)


class TestNearestCommand(sublime_plugin.WindowCommand):
    def run(self, **kwargs):
        _run_command(self.window, 'nearest', **kwargs)


class TestResultsCommand(sublime_plugin.WindowCommand):
    def run(self, **kwargs):
        _run_command(self.window, 'results', **kwargs)


class TestSuiteCommand(sublime_plugin.WindowCommand):
    def run(self, **kwargs):
        _run_command(self.window, 'suite', **kwargs)


class TestSuiteWithCommand(sublime_plugin.WindowCommand):
    def run(self, **kwargs):
        _run_command(self.window, 'suite_with_coverage', **kwargs)


class TestSwitchCommand(sublime_plugin.WindowCommand):
    def run(self, **kwargs):
        _run_command(self.window, 'switch', **kwargs)


class TestVisitCommand(sublime_plugin.WindowCommand):
    def run(self, **kwargs):
        _run_command(self.window, 'visit', **kwargs)


def _switch_file(window):
    view = window.active_view()
    if not view:
        return status_message('view not found')

    file_name = view.file_name()
    if not file_name:
        return status_message('file name not found')

    _debug_message(window, 'switch from {}'.format(file_name))

    # We need to evaluate the realpath of the file in order to mutate it to and
    # from test -> file and file -> test.
    file_name = os.path.realpath(file_name)
    _debug_message(window, 'switch from {} (realpath)'.format(file_name))

    for package in os.listdir(packages_path()):
        p_path = os.path.join(packages_path(), package)
        if file_name.startswith(p_path):
            if os.path.isdir(p_path):
                f_path, f_base = os.path.split(file_name)

                if f_base.startswith('test_'):
                    # Switch from test -> file
                    switch_to_file = os.path.join(
                        f_path.replace(os.path.join(p_path, 'tests'), os.path.join(p_path)),
                        f_base[5:])
                else:
                    # Switch from file -> test
                    switch_to_file = os.path.join(
                        f_path.replace(p_path, os.path.join(p_path, 'tests')),
                        'test_' + f_base)

                _debug_message(window, 'switch to   {}'.format(switch_to_file))

                # Checks to see if the file we're switching to is already open,
                # and takes into account symlinks i.e. if we didn't do this then
                # we would end up opening a second view with the realpath file
                # rather than opening the symlinked one.
                for view in window.views():
                    if view.file_name():
                        if os.path.realpath(view.file_name()) == switch_to_file:
                            return window.open_file(view.file_name())

                if os.path.isfile(switch_to_file):
                    window.open_file(switch_to_file)


# TODO This command belongs in a Python Testing plugin.
class PythonTestSwitchCommand(sublime_plugin.WindowCommand):
    def run(self):
        _switch_file(self.window)


_COMMANDS = {
    'cancel': {
        'phpunit': 'phpunit_test_cancel',
    },
    'file': {
        'color_scheme_unit': 'color_scheme_unit_test_file',
        'phpunit': 'phpunit_test_file',
        'sublime_text': 'unit_testing_test_file',
    },
    'file_with_coverage': {
        'phpunit': ('phpunit_test_file', {'coverage': True}),
        'sublime_text': ('unit_testing_test_file', {'coverage': True}),
    },
    'last': {
        'phpunit': 'phpunit_test_last',
        'sublime_text': 'unit_testing_test_last',
    },
    'nearest': {
        'color_scheme_unit': 'color_scheme_unit_test_file',
        'phpunit': 'phpunit_test_nearest',
        'sublime_text': 'unit_testing_test_nearest',
    },
    'results': {
        'color_scheme_unit': 'color_scheme_unit_test_results',
        'phpunit': 'phpunit_test_results',
    },
    'suite': {
        'color_scheme_unit': 'color_scheme_unit_test_suite',
        'phpunit': 'phpunit_test_suite',
        'sublime_text': 'unit_testing_test_suite',
    },
    'suite_with_coverage': {
        'phpunit': ('phpunit_test_suite', {'coverage': True}),
        'sublime_text': ('unit_testing_test_suite', {'coverage': True})
    },
    'switch': {
        'phpunit': 'phpunit_test_switch',
        'sublime_text': 'unit_testing_test_switch',
    },
    'visit': {
        'phpunit': 'phpunit_test_visit',
    },
}


_NAME = {
    'unittesting.json': 'sublime_text',
    'phpunit.xml': 'phpunit',
    'phpunit.xml.dist': 'phpunit',
    'composer.json': 'phpunit',
}

_NAME_STARTS = {
    'color_scheme_test': 'color_scheme_unit',
}


_EXTENSIONS = {
    '.tmTheme': 'color_scheme_unit',
    '.php': 'phpunit',
    '.sublime-project': 'sublime_text',
}


def _get_context(window):
    view = window.active_view()
    if view:
        file_name = view.file_name()
        if file_name:
            f_path, f_base = os.path.split(file_name)
            f_name, f_ext = os.path.splitext(f_base)

            if f_base in _NAME:
                return _NAME[f_base]

            for k, v in _NAME_STARTS.items():
                if f_name.startswith(k):
                    return v

            if f_ext in _EXTENSIONS:
                return _EXTENSIONS[f_ext]

        if view.match_selector(view.sel()[0].begin(), 'source.python'):
            return 'sublime_text'

    return None


def _debug_message(window, msg):
    view = window.active_view()
    if view and view.settings().get('test.debug', False):
        print('Test:', msg)


def _run_command(window, name, **kwargs):
    context = _get_context(window)
    if not context:
        print('Test: context not known')

        return

    _debug_message(window, 'context: {}'.format(context))

    try:
        cmd = _COMMANDS[name][context]

        if isinstance(cmd, tuple):
            cmd, cmd_args = cmd
        else:
            cmd_args = {}

        cmd_args.update(kwargs)

        _debug_message(window, 'command: {} {}'.format(cmd, cmd_args))

        window.run_command(cmd, cmd_args)
    except KeyError:
        print('Test: command not found')
