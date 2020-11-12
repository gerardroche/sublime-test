# Test

Leverage the power of Sublime Text test runners.

[![Minimum Sublime Version](https://img.shields.io/badge/sublime-%3E%3D%203.0-brightgreen.svg?style=flat-square)](https://sublimetext.com) [![Latest Version](https://img.shields.io/github/tag/gerardroche/sublime-test.svg?style=flat-square&label=version)](https://github.com/gerardroche/sublime-test/tags) [![GitHub stars](https://img.shields.io/github/stars/gerardroche/sublime-test.svg?style=flat-square)](https://github.com/gerardroche/sublime-test/stargazers) [![Downloads](https://img.shields.io/packagecontrol/dt/Test.svg?style=flat-square)](https://packagecontrol.io/packages/Test)

## INSTALLATION

### Package Control installation

The preferred method of installation is [Package Control](https://packagecontrol.io/packages/Test).

### Manual installation

Close Sublime Text, then download or clone this repository to a directory named **"Test"** in the Sublime Text Packages directory for your platform:

* Linux: `git clone https://github.com/gerardroche/sublime-test.git ~/.config/sublime-text-3/Packages/Test`
* OSX: `git clone https://github.com/gerardroche/sublime-test.git ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/Test`
* Windows: `git clone https://github.com/gerardroche/sublime-test.git %APPDATA%\Sublime/ Text/ 3/Packages/Test`

## Commands

These commands are available through the Command Palette. To use the command palette:

1. Press `Ctrl+Shift+P`
2. Select a command
3. Press `Enter`

command | description
------- | -----------
`TestSuite` | Runs the whole test suite (if the current file is a test file, runs that framework's test suite).
`TestFile` | In a test file runs all tests in the current file, otherwise runs that file's tests.
`TestNearest` | In a test file runs the test nearest to the cursor, otherwise runs that file's tests.
`TestLast` | Runs the last test.
`TestVisit` | Visits the test file from which you last run your tests (useful when you're trying to make a test pass, and you dive deep into application code and close your test buffer to make more space, and once you've made it pass you want to go back to the test file to write more tests).
`TestSwitch` | In a test file opens the file under test, otherwise opens the test file.
`TestResults` | Opens the test results panel.
`TestCancel` | Cancels the test runner.

### Key Bindings

Add your preferred key bindings via `Menu > Preferences > Key Bindings` or use the command palette. To use the command palette:

1. Press `Ctrl+Shift+P`
2. Select the "Preferences: Key Bindings" command
3. Press `Enter`

```json
{ "keys": ["ctrl+shift+a"], "command": "test_suite" },
{ "keys": ["ctrl+shift+c"], "command": "test_cancel" },
{ "keys": ["ctrl+shift+f"], "command": "test_file" },
{ "keys": ["ctrl+shift+l"], "command": "test_last" },
{ "keys": ["ctrl+shift+n"], "command": "test_nearest" },
{ "keys": ["ctrl+shift+r"], "command": "test_results" }
{ "keys": ["ctrl+shift+s"], "command": "test_switch" },
{ "keys": ["ctrl+shift+v"], "command": "test_visit" },
```

key | description
--- | -----------
`F4` | Jump to Next Failure
`Shift+F4` | Jump to Previous Failure

## Supported packages

The following test runners are supported:

Language |  Package | Test Runners
--------:|:-------- | ------------
**PHP** | [PHPUnitKit](https://github.com/gerardroche/sublime-phpunit) | PHPUnit
 | [UnitTesting](https://github.com/randy3k/UnitTesting) | Sublime Text plugins
 | [ColorSchemeUnit](https://github.com/gerardroche/sublime-color-scheme-unit) | Sublime Text color schemes

## LICENSE

Released under the [BSD 3-Clause License](LICENSE).
