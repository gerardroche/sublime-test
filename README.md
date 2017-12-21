# Test

Leverage the power of Sublime Text testing plugins.

[![Minimum Sublime Version](https://img.shields.io/badge/sublime-%3E%3D%203.0-brightgreen.svg?style=flat-square)](https://sublimetext.com) [![Latest Stable Version](https://img.shields.io/github/tag/gerardroche/sublime-test.svg?style=flat-square&label=stable)](https://github.com/gerardroche/sublime-test/tags) [![GitHub stars](https://img.shields.io/github/stars/gerardroche/sublime-test.svg?style=flat-square)](https://github.com/gerardroche/sublime-test/stargazers) [![Downloads](https://img.shields.io/packagecontrol/dt/Test.svg?style=flat-square)](https://packagecontrol.io/packages/Test) [![Author](https://img.shields.io/badge/twitter-gerardroche-blue.svg?style=flat-square)](https://twitter.com/gerardroche)

![Screenshot](screenshot.png)

## INSTALLATION

### Package Control installation

The preferred method of installation is [Package Control](https://packagecontrol.io/browse/authors/gerardroche).

### Manual installation

Close Sublime Text, then download or clone this repository to a directory named `Test` in the Sublime Text Packages directory for your platform:

* Linux: `git clone https://github.com/gerardroche/sublime-test.git ~/.config/sublime-text-3/Packages/Test`
* OSX: `git clone https://github.com/gerardroche/sublime-test.git ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/Test`
* Windows: `git clone https://github.com/gerardroche/sublime-test.git %APPDATA%\Sublime/ Text/ 3/Packages/Test`

## USAGE

### Supported plugins

Language | Framework | Package
-------- | --------- | -------
 | Sublime Text | [ColorSchemeUnit](https://github.com/gerardroche/sublime-color-scheme-unit)
PHP | PHPUnit | [PHPUnitKit](https://github.com/gerardroche/sublime-phpunit)
Python | Sublime Text | [UnitTesting](https://github.com/randy3k/UnitTesting)

Please open an issue to add support for your testing plugin.

### Commands

Command Palette | Command | Description
--------------- | ------- | -----------
`:TestSuite` | `test_suite` | Run test suite of the current file.
`:TestFile` | `test_file` | Run tests for the current file. If the current file is not a test file, it runs tests of the test file for the current file.
`:TestNearest` | `test_nearest` | Run a test nearest to the cursor (supports multiple selections). If the current file is not a test file, it runs tests of the test file for the current file.
`:TestLast` | `test_last` | Run the last test.
`:TestVisit` | `test_visit` | Open the last run test in the current window (useful when you're trying to make a test pass, and you dive deep into application code and close your test buffer to make more space, and once you've made it pass you want to go back to the test file to write more tests).
`:TestSwitch` | `test_switch` | Splits the window and puts nearest test case and class under test side by side.
`:TestResults` | `test_results` | Show the test results panel.
`:TestCancel` | `test_cancel` | Cancels current test run.

### Key Bindings

Add your preferred key bindings: `Menu > Preferences > Key Bindings`

```json
[
    { "keys": ["ctrl+shift+a"], "command": "test_suite" },
    { "keys": ["ctrl+shift+f"], "command": "test_file" },
    { "keys": ["ctrl+shift+n"], "command": "test_nearest" },
    { "keys": ["ctrl+shift+l"], "command": "test_last" },
    { "keys": ["ctrl+shift+v"], "command": "test_visit" },
    { "keys": ["ctrl+shift+s"], "command": "test_switch" },
    { "keys": ["ctrl+shift+c"], "command": "test_cancel" },
    { "keys": ["ctrl+shift+r"], "command": "test_results" },
]
```

Key | Description
--- | -----------
`F4` | Jump to Next Failure
`Shift+F4` | Jump to Previous Failure

## LICENSE

Released under the [BSD 3-Clause License](LICENSE).
