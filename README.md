seprcph
=======

Trains across Europe - a riveting Python 2 game. Reviewers have had the following to say about the game:

> The map is better than anything from a CoD map pack.

> Trains have never been this interesting!

> I locked myself away for days on end to play this game.

> This made me sell my Xbox.

> 9 / 10 - lost me my marriage.

Contents
==========
- [Requirements](#requirements)
- [Installation](#installation)
- [Running the Binary](#running-the-binary)
- [Building](#building)
- [Generating Documentation](#generating-documentation)
- [Unit Tests](#unit-tests)
- [Code checking](#code-checking)
- [Continuous Integration](#continuous-integration)
- [Completion](#completion)

Requirements
==========
For running the game:
- [Python 2.7](https://www.python.org/)
- [Pygame](http://www.pygame.org/news.html)

For building binaries:
- [cx_Freeze](http://cx-freeze.sourceforge.net/)

For generating the documentation:
- [Doxygen](http://www.pygame.org/news.html)
- [doxypypy](https://github.com/Feneric/doxypypy)

For running tests:
- [pep8](https://pypi.python.org/pypi/pep8)
- [pylint](http://www.pylint.org/)

Installation
============
**NOTE: If you can't install dependencies onto the computer you're using, create and copy the folders as mentioned below and then skip to [running the binary](#running-the-binary).**

- Clone git repository into a folder called ```seprcph```
- Navigate to the local repository using the command line
- Depending on your Python installation run one of the following commands:
    - ```python2.7 setup.py install```
    - ```python setup.py install```
- Create a new folder in the relevant directory:
    - Windows: ```C:\Users\Username\seprcph```
    - Linux ```~/.config/seprcph```
- Copy the ```assets``` and ```data``` folders from the local repository to the folder that you just created
- If you're on Linux, you can simply run ```seprcph``` from terminal. If you're on Windows, you can either install a better OS or do the following:
    - Launch the game by running the command (using the python guidelines above):
    ```python2.7 {path from current directory to the seprcph folder in the local repo}/main```
Running The Binary
===========
If you are lucky enough to have the binary files, navigate to the folder that they are located in. Running the binary is as simple as double clicking it, alternatively, you can run it from terminal. This binary doesn't require any dependencies to be installed, so it will work on the university computers.

Make sure that the binary remains in the folder it was provided in - all of the libraries required for running th binary are in that folder.


Building
===========
It is possible to build the game into a binary, so that it can be run on other computers that don't have Pygame installed (such as the university PCs). In order to do this, you will need to have [cx_Freeze](http://cx-freeze.sourceforge.net/) installed.

There is a script that will build the binaries for you - ```cx_build.py```.

**NOTE: If you want to build a binary for Windows - you must do so on a Windows computer, the same is true for Linux.**

Generating a binary is as simple as running:

```
python2.7 cx_build.py build
```

This will create a new ```build``` folder. This folder will contain a generated binary, as well as all the libraries required for running the game.

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

Completion
==========

The following have been completed:
- Card class
- Hand class
- Deck class
- Player class
- Goal class
- Train class
- Map class
- Track class
- Effect class
- GoalFactory class
- CardFactory class
- Renderable class
- Affectable class
- EventManager and Event (most classes are tied into this system)
- Rendering sprites and the map (some elements of the GUI too)
- Artwork is completed
- Loading Cards from JSON
- Loading Cities from JSON
- Loading Tracks from JSON
- Logging
- Unit tests (over 50)
- Documentation generation
- Configuration file is created and successfully parsed

The following are very close to completion, or are completed but not 'hooked up':
- GUI (there is a bug here relating to rendering the contents of containers. I have explained it in the comments).
- CardFactory can handle different deck biases (referred to elsewhere as policies), but the rest of the game isn't aware of them.
- GUI layout hasn't been created - the building blocks are there though.
- An effect can only be applied to a City, Track of Train.
- Trains should move and calculate their rotation correctly (not tested).
- A turn limit is loosely implemented.
- More effects need adding.

The following haven't been completed:
- Turn based gameplay - most of the building blocks are there.
- Goal progress (currently a goal is either completed or isn't).
- A player can't discard unwanted cards.
