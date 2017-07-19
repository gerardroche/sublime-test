from sublime_plugin import WindowCommand


class TestNearestCommand(WindowCommand):

    def run(self):
        if _is_in_python_context(self.window):
            command = 'unit_testing_current_file'
        else:
            command = 'phpunit_test_nearest'

        self.window.run_command(command)


class TestFileCommand(WindowCommand):

    def run(self):
        if _is_in_python_context(self.window):
            command = 'unit_testing_current_file'
        else:
            command = 'phpunit_test_file'

        self.window.run_command(command)


class TestSuiteCommand(WindowCommand):

    def run(self):
        if _is_in_python_context(self.window):
            command = 'unit_testing_current_project'
        else:
            command = 'phpunit_test_suite'

        self.window.run_command(command)


class TestLastCommand(WindowCommand):

    def run(self):
        if _is_in_python_context(self.window):
            command = 'unit_testing_test_last'
        else:
            command = 'phpunit_test_last'

        self.window.run_command(command)


class TestSwitchCommand(WindowCommand):

    def run(self):
        if _is_in_python_context(self.window):
            command = 'python_test_switch'
        else:
            command = 'phpunit_test_switch'

        self.window.run_command(command)


def _is_in_python_context(window):
    view = window.active_view()
    return view.match_selector(view.sel()[0].begin(), 'source.python')
