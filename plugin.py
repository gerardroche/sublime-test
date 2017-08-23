import os
import re

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


def _get_context(window):
    view = window.active_view()
    if view:
        file_name = view.file_name()

        if file_name:
            if bool(re.match('^color_scheme_test.*\.[a-zA-Z0-9]+$', os.path.basename(file_name))):
                return 'color_scheme_unit'

        if view.match_selector(view.sel()[0].begin(), 'source.python'):
            return 'sublimetext'

    return 'phpunit'


def _run_command(window, name):
    try:
        command = _COMMANDS[name][_get_context(window)]
        print('Test: run command \'{}\''.format(command))
        window.run_command(command)
    except KeyError:
        print('Test: test not found')
