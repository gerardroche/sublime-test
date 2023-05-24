# Copyright (C) 2023 Gerard Roche
#
# This file is part of Test.
#
# Test is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Test is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Test.  If not, see <https://www.gnu.org/licenses/>.

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

    _log_debug(window, 'switch from {}'.format(file_name))

    # We need to evaluate the realpath of the file in order to mutate it to and
    # from test -> file and file -> test.
    file_name = os.path.realpath(file_name)
    _log_debug(window, 'switch from {} (realpath)'.format(file_name))

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

                _log_debug(window, 'switch to   {}'.format(switch_to_file))

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


_DEFINITIONS = {}  # type: dict


_CONFIG_FILE_NAME_CONTEXTS = {
    'unittesting.json': 'unit_testing',
    'phpunit.xml': 'phpunit',
    'phpunit.xml.dist': 'phpunit',
    'phpunit.dist.xml': 'phpunit',
    'composer.json': 'phpunit',
}

_FILE_NAME_STARTS_WITH_CONTEXTS = {
    'color_scheme_test': 'color_scheme_unit',
}


_FILE_NAME_EXTENSION_CONTEXTS = {
    '.tmTheme': 'color_scheme_unit',
    '.php': 'phpunit',
    '.sublime-project': 'unit_testing',
}


def _get_context(window):
    view = window.active_view()
    if view:
        file_name = view.file_name()
        if file_name:
            f_path, f_base = os.path.split(file_name)
            f_name, f_ext = os.path.splitext(f_base)

            if f_base in _CONFIG_FILE_NAME_CONTEXTS:
                return _CONFIG_FILE_NAME_CONTEXTS[f_base]

            for k, v in _FILE_NAME_STARTS_WITH_CONTEXTS.items():
                if f_name.startswith(k):
                    return v

            if f_ext in _FILE_NAME_EXTENSION_CONTEXTS:
                return _FILE_NAME_EXTENSION_CONTEXTS[f_ext]

        if view.match_selector(view.sel()[0].begin(), 'source.python'):
            return 'unit_testing'

    return None


def _log_debug(window, msg):
    view = window.active_view()
    if view and view.settings().get('test.debug', False):
        print('Test:', msg)


def _run_command(window, name, **kwargs):
    context = _get_context(window)
    if not context:
        return status_message('Test: could not run command: unknown context')

    try:
        cmd = _DEFINITIONS[name][context]
    except KeyError:
        cmd = '%s_test_%s' % (context, name)

    if isinstance(cmd, tuple):
        cmd, cmd_args = cmd
    else:
        cmd_args = {}

    cmd_args.update(kwargs)

    _log_debug(window, 'command: {} {}'.format(cmd, cmd_args))

    window.run_command(cmd, cmd_args)
