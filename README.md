seprcph
=======

Trains across Europe - a riveting Python 2 game. Reviewers have had the following to say about the game:

> The map is better than anything from a CoD map pack.

> Trains have never been this interesting!

> I locked myself away for days on end to play this game.

> This made me sell my Xbox.

Contents
==========
- [Requirements](#requirements)
- [Generating Documentation](#generating-documentation)
- [Unit Tests](#unit-tests)
- [Code checking](#code-checking)
- [Continuous Integration](#continuous-integration)

Requirements
==========
For building and running the game:
- [Python 2.7](https://www.python.org/)
- [Pygame](http://www.pygame.org/news.html)

For generating the documentation:
- [Doxygen](http://www.pygame.org/news.html)
- [doxypypy](https://github.com/Feneric/doxypypy)

For running tests:
- [pep8](https://pypi.python.org/pypi/pep8)
- [pylint](http://www.pylint.org/)

Generating Documentation
==========
The code makes heavy use of [Doxygen](http://www.stack.nl/~dimitri/doxygen/) to document everything. We have a custom ```Doxyfile``` that is optimised for Python and our game. It will create a HTML website based upon the comments from within the code.

We use an extension for Doxygen called [doxypypy](https://github.com/Feneric/doxypypy). In order to use this, we have set the ```INPUT_FILTER``` variable to use a script we have created.

In order to generate the documentation, you need to be in the top level of the project (you should see the file ```Doxyfile``` in that directory) and run the command:

```
doxygen
```

We have been using Github Pages to host our documentation - you can read about them [here](https://pages.github.com/). The branch ```gh-pages``` in this repository contains the code for the website and the generated documentation.

Unit Tests
==========
We have over 50 unit tests for our game. ```pygame``` is required to run them.

Change into the top level directory of the project (the one containing the file ```setup.py```.

```
cd /path/to/seprcph
```

Then run:

```
python2.7 setup.py test
```

This will output the results of all of the tests. Make sure you rerun the tests after each change you make.

Code Checking
==========
We have tried hard to stick to the [PEP8](https://www.python.org/dev/peps/pep-0008/) standard and have tests written to help with this. In order to run the code checking tests, you will need to have [PEP8](https://pypi.python.org/pypi/pep8) and [pylint](http://www.pylint.org/).

A script has been written to help with the code checking - but it will only work on *NIX systems (or Windows if you have Cygwin + Bash). You can run it as follows:

```
scripts/check seprcph
```

Take a look inside of the script to see what commands are being run - in case you want to run them on your own.

Continuous Integration
==========
We used [Jenkins](http://jenkins-ci.org/) to run our tests each time a commit was made - it keeps track of PEP8 violations, how often unit tests fail as well as proof that a commit won't break unit tests if it is merged.

There is a script called ```jenkins.sh``` that is used as the build comman in Jenkins.

Some of the Jenkins plugins we used include:
- Github
- Git
- Github OAuth
- Github Pull Request Builder
- Violations
