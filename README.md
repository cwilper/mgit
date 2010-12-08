mgit
====

Runs any git command across all repositories beneath a given directory.

Installation
------------

    $ [sudo] easy_install mgit

Usage
-----

    $ mgit path git-arg [git-arg..]

Example
-------

Say you organize all of your code projects under a `projects` directory
like this:

    ~/projects/work/proj1/           
                   /proj2/
    ~/projects/home/proj1/
                   /proj2/

The following would find all git repositories in this directory and
issue a `git status -s` for each:

    $ mgit ~/projects status -s
