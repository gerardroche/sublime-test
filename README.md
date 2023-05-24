# Test

<p>
    <a href="https://packagecontrol.io/packages/Test"><img alt="Downloads" src="https://img.shields.io/packagecontrol/dt/Test.svg"></a>
</p>

Leverage the power of Sublime Text test runners.

<img src="https://raw.githubusercontent.com/gerardroche/sublime-test/master/screenshot.png" width="585" alt="Screenshot">

## Installation

Install Test via [Package Control](https://packagecontrol.io/packages/Test).

## Setup

Install your preferred test runners via Package Control:

| Language                                      | Test Runners                      | Package
| --------:                                     |:------------                      | :------
| **PHP**                                       | PHPUnit, ParaTest, Pest, Artisan  | [PHPUnitKit](https://packagecontrol.io/packages/PHPUnitKit)
| **Sublime&nbsp;Text&nbsp;plugin**             | UnitTesting                       | [UnitTesting](https://packagecontrol.io/packages/UnitTesting)
| **Sublime&nbsp;Text&nbsp;color&nbsp;scheme**  | ColorSchemeUnit                   | [ColorSchemeUnit](https://packagecontrol.io/packages/ColorSchemeUnit)

Add your preferred key bindings.

**Menu → Preferences → Key Bindings**

```json
[
    { "keys": ["ctrl+shift+a"], "command": "test_suite" },
    { "keys": ["ctrl+shift+c"], "command": "test_cancel" },
    { "keys": ["ctrl+shift+f"], "command": "test_file" },
    { "keys": ["ctrl+shift+l"], "command": "test_last" },
    { "keys": ["ctrl+shift+n"], "command": "test_nearest" },
    { "keys": ["ctrl+shift+r"], "command": "test_results" }
    { "keys": ["ctrl+shift+s"], "command": "test_switch" },
    { "keys": ["ctrl+shift+v"], "command": "test_visit" },
]
```

## Commands

You can execute all commands from the Command Palette:

Command                 | Description
:---------------------- | :----------
**Test&nbsp;Nearest**   | In a test file runs the test nearest to the cursor, otherwise runs the test for the current file.
**Test&nbsp;File**      | In a test file runs all tests in the current file, otherwise runs test for the current file.
**Test&nbsp;Suite**     | Runs the whole test suite.
**Test&nbsp;Last**      | Runs the last test.
**Test&nbsp;Switch**    | In a test file opens the file under test, otherwise opens the test file.
**Test&nbsp;Visit**     | Visits the test file from which you last run your tests (useful when you're trying to make a test pass, and you dive deep into application code and close your test buffer to make more space, and once you've made it pass you want to go back to the test file to write more tests).
**Test&nbsp;Results**   | Opens the exec test output panel.
**Test&nbsp;Cancel**    | Cancels any currently running test.

## Key Bindings

Key         | Description
:---        | :----------
`F4`        | Jump to next failure
`SHIFT+F4`  | Jump to previous failure

## License

Released under the [GPL-3.0-or-later License](LICENSE).
