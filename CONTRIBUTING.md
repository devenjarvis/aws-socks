# Contributing Guide

Thank you for contributing to socks! This document shows you how to get started

## General
- The [Codebase Structure](/CODEBASE_STRUCTURE.md) has detailed information about how the various files in this project are structured
- Please ensure that any changes you make are in accordance with the [Coding Guidelines](/CODING_GUIDELINES.md) of this repo

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

PRs will be reviewed by maintainers of the project and wither rejected with detailed change requests, or merged into develop (and eventually master) for all to use.
