import os
import re

from sublime_plugin import WindowCommand


class TestCancelCommand(WindowCommand):

    def run(self):
        self.window.run_command(_get_run_command('cancel', self.window))


class TestCoverageCommand(WindowCommand):

    def run(self):
        self.window.run_command(_get_run_command('coverage', self.window))


class TestFileCommand(WindowCommand):
    def run(self):
        self.window.run_command(_get_run_command('file', self.window))


class TestLastCommand(WindowCommand):
    def run(self):
        self.window.run_command(_get_run_command('last', self.window))


class TestNearestCommand(WindowCommand):
    def run(self):
        self.window.run_command(_get_run_command('nearest', self.window))


class TestResultsCommand(WindowCommand):
    def run(self):
        self.window.run_command(_get_run_command('results', self.window))


class TestSuiteCommand(WindowCommand):
    def run(self):
        self.window.run_command(_get_run_command('suite', self.window))


class TestSwitchCommand(WindowCommand):
    def run(self):
        self.window.run_command(_get_run_command('switch', self.window))


class TestVisitCommand(WindowCommand):
    def run(self):
        self.window.run_command(_get_run_command('visit', self.window))


_COMMANDS = {
    'cancel': {
        'phpunit': 'phpunit_test_cancel',
    },
    'coverage': {
        'phpunit': 'phpunit_test_coverage',
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
        'sublimetext': 'unit_testing_current_project',
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


def _get_run_command(name, window):
    try:
        return _COMMANDS[name][_get_context(window)]
    except KeyError:
        return 'test_noop'
