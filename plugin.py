import os

from sublime_plugin import WindowCommand


class TestCancelCommand(WindowCommand):

    def run(self):
        _run_command(self.window, 'cancel')


class TestFileCommand(WindowCommand):
    def run(self):
        _run_command(self.window, 'file')


class TestLastCommand(WindowCommand):
    def run(self):
        _run_command(self.window, 'last')


class TestNearestCommand(WindowCommand):
    def run(self):
        _run_command(self.window, 'nearest')


class TestResultsCommand(WindowCommand):
    def run(self):
        _run_command(self.window, 'results')


class TestSuiteCommand(WindowCommand):
    def run(self):
        _run_command(self.window, 'suite')


class TestSwitchCommand(WindowCommand):
    def run(self):
        _run_command(self.window, 'switch')


class TestVisitCommand(WindowCommand):
    def run(self):
        _run_command(self.window, 'visit')


_COMMANDS = {
    'cancel': {
        'phpunit': 'phpunit_test_cancel',
    },
    'file': {
        'color_scheme_unit': 'color_scheme_unit_test_file',
        'phpunit': 'phpunit_test_file',
        'sublimetext': 'unit_testing_current_file',
    },
    'last': {
        'phpunit': 'phpunit_test_suite',
    },
    'nearest': {
        'color_scheme_unit': 'color_scheme_unit_test_file',
        'phpunit': 'phpunit_test_nearest',
        'sublimetext': 'unit_testing_current_file',
    },
    'results': {
        'color_scheme_unit': 'color_scheme_unit_test_results',
        'phpunit': 'phpunit_test_results',
    },
    'suite': {
        'color_scheme_unit': 'color_scheme_unit_test_suite',
        'phpunit': 'phpunit_test_suite',
        'sublimetext': 'unit_testing_current_package',
    },
    'switch': {
        'phpunit': 'phpunit_test_switch',
    },
    'visit': {
        'phpunit': 'phpunit_test_visit',
    },
}


_EXTENSIONS = {
    '.tmTheme': 'color_scheme_unit'
}


_NAME_STARTS = {
    'color_scheme_test': 'color_scheme_unit'
}


def _get_context(window):
    view = window.active_view()
    if view:
        file_name = view.file_name()
        if file_name:
            f_path, f_base = os.path.split(file_name)
            f_name, f_ext = os.path.splitext(f_base)

            for k, v in _NAME_STARTS.items():
                if f_name.startswith(k):
                    return v

            if f_ext in _EXTENSIONS:
                return _EXTENSIONS[f_ext]

        if view.match_selector(view.sel()[0].begin(), 'source.python'):
            return 'sublimetext'

    return 'phpunit'


def _run_command(window, name):
    try:
        view = window.active_view()
        is_debug = view.settings().get('test.debug') if view else window.settings().get('test.debug')
        if is_debug:
            print('Test: view=[id={},file={}]'.format(view.id(), view.file_name()))

        context = _get_context(window)

        if is_debug:
            print('Test: in \'{}\' context'.format(context))

        command = _COMMANDS[name][context]

        if is_debug:
            print('Test: run \'{}\' command'.format(command))

        window.run_command(command)
    except KeyError:
        print('Test: test not found')
