# Contributing

Code must be put into the repository as the result of a pull request, we don't want (unless in exceptional circumstances)
people randomly throwing code into the repo.

## Getting Started

Clone the repository:

    git clone https://github.com/HarveyHunt/seprcph.git
  
Change to the develop branch:

    git checkout develop
  
Hack away until your heart is content.

Take a look at the [issues](https://github.com/HarveyHunt/seprcph/issues) for ideas on what to work on.

## Code Style

Follow [PEP8](http://legacy.python.org/dev/peps/pep-0008/) as closely as sanely possible.

Running a code linter, such as [PyFlakes](https://launchpad.net/pyflakes) is always a nice idea- try to minimise errors.

The hard rules are as follows:

  * 4 spaces per tab
  * use_of_underscores_for_functions_variables_etc
  * Code should be pythonic
  * All new code *must* be documented
  
## Commit Rules

Try to stick to the following rules:
  * Keep the first line of a commit message less than 80 characters.
  * Keep commit messages descriptive but short.
  * If you fix an issue or your commit is related to an issue, read more [here](https://github.com/blog/957-introducing-issue-mentions).
  * Commit small and often, otherwise tools such as [git-bisect](http://git-scm.com/docs/git-bisect) will become useless.
  
## What comes after code?

You have written an awesome new feature and want to get it merged straight away- have you forgotten something?

Documentation is an important part of any project, Project Homeslice is no different. Document all new features, as has been done
in the README already.

If you're feeling especially kind and in a Python mood, try to add some unit tests for your new feature- or even more parts of Project Homeslice in general.

## Sending PRs
  
Once you have made some cool changes, push to github and send a PR.

Make sure that the PR is targeted at the develop branch, we want to keep master "clean" and only push to it at the end of a sprint.

## Merging PRs

We all have the ability to merge PRs, that doesn't mean we should randomly start merging stuff. 

At least one person (other than the PR's author) should "sign off" on the PR by commenting on its issue.

