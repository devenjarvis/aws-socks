# Contributing Guide

Thank you for contributing to socks! This document shows you how to get started

## General

### Codebase Structure
The structure to socks is fairly simple - one module (i.e. .py file) per AWS service. 
- If a service has a common acronym or shorthand (like S3) then use that, elsewise prefer the full name (like athena) with no spaces
- Following standard Python naming standards all file names should be lowercase with single words preferred

### Coding Guidelines
- Function names and variable names should all be lower_case_with_underscores
- Class names should use the CapWords convention
- Function names should be short but descriptive.
- All modules should be imported into the __init__.py file to simplify usage
- 3rd party packages (except for boto3) should be generally avoided.
- Standard Python packages are allowed
- Indent with 4 spaces
- Function calls have no space before the parentheses
- A space after each comma, but without a space before
- All operators must have one space before and one after
- There should not be more than one contiguous blank line
- There should be no empty comments

## Getting the code

1. [Fork the repo](https://github.com/devenjarvis/aws-socks/fork)
  a. If you've already forked the repo before, jump to step 4.
2. Clone down your fork to your local machine
3. Specify a new remote upstream repository that will be synced with the fork
    ```
    git remote add upstream https://github.com/devenjarvis/aws-socks.git
    ```
4.  Pull the latest version of the upstream repo branches by running:
    ```
    git fetch upstream
    ```
5. Check out a new branch off of upstream/master and name it based on what you intend to contribute:
    ````
    git checkout -b feat/NAME_OF_FEATURE upstream/master
    ````

## Development
- Install dependencies
  - If you haven't already install poetry with `pip install poetry`
  - Running `poetry install` will install any missing Python dependencies for this package
- Add your code
    - Don't forget to check out the [Coding Guidelines](/CODING_GUIDELINES.md)

## Testing
- The provided unit tests can be run with `poetry run pytest --cov-report term --cov=socks ./tests`
- New unit tests can and should be added for any new functions in the appropriate test_module file in the ./tests directory.
    - Note the pytest fixture used to MagicMock boto3 calls. return_values are defined for boto3 calls that rely on one another, or when you need a mocked output to assert against.

## Documentation
- Make comments in the code as needed throughout your new functionality.
- Remember to remove any TODO comments you might have completed.
- Add your name under the Contributors section in the [README](/README.md). Give yourself credit!

## Submitting changes
- Commit your changes
  - Please provide a commit message that explains what you've done, don't be afraid to be verbose!
  - Commit to the forked repository
  - Example:
    ````
    $ git commit -am 'YOUR_HELPFUL_COMMIT_MESSAGE'
    ````
- Push to the branch
  - Example:
    ````
    $ git push origin feat/NAME_OF_FEATURE
    ````
- Make a pull request
  - Make sure you send the PR to the <code>develop</code> branch

PRs will be reviewed by maintainers of the project and either rejected with detailed change requests, or merged into develop (and eventually master) for all to use.
