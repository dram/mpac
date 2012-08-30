====
mpac
====

-----------------------
a Mageia PACage manager
-----------------------

:Author: Xin Wang <dram.wang@gmail.com>
:Date: 2012-08-30
:Version: 0.?
:Copyright: BSD 2-Clause License
:Manual section: 8
:Manual group: System Administration

SYNOPSIS
========

::

   mpac <command> [--options] [arguments]

DESCRIPTION
===========

Mpac is a command line tool used to manage packages in Mageia. It tries to
utilize functionality of URPMI to provide users with a friendly interface.

Mpac is a wrapper of URPMI, all hard stuff are done by ``urpmi(8)``
and its siblings.

COMMANDS
========

Mpac divide package management operations into seperate sub-commands,
namely:

  * ``search  (se)`` - search packages using partial match
  * ``query   (qu)`` - query info of a specified package
  * ``install (in)`` - install a packege
  * ``erase   (er)`` - erase a package
  * ``refresh (re)`` - refresh package list of media
  * ``update  (up)`` - update system

Additionally, mpac also provides commands to manipulate package media:

  * ``list        (li)`` - list all packages in media
  * ``addmedia    (am)`` - add new media
  * ``listmedia   (lm)`` - list media configured in system
  * ``modifymedia (mm)`` - enable or disable media
  * ``removemedia (rm)`` - remove existent media

Most commands accept some options to alter its behaviour, and will be
described in detail in subsequent sections.

When commands or options accept a ``pattern``, a pattern with wildcard
characters can be specified, with ``?`` matches one character, and
``*`` match zero or more ones. A pattern without wildcard will do a
exact match, with argument of ``search`` command as a exception, and
will be explained later.

All pattern match, with or without wildcard are case-insensitive. 

search (se) [options] pattern
-----------------------------

Search command try to search all active media using supplied argument
as a search pattern. It will print all matched packages with its
status, name, version and summary. If columns of console are
sufficient, name of the media which it belongs to will also be
printed.

Search command will do a sub-string match by default, if there are any
wildcard characters in the pattern, it will using a wildcard match
instead.

Status is indicated by a character, (``i``) means package is already
installed, (``u``) means update is available, (``d``) means locally
installed version is higher than media one, and it will leave blank
for packages that have not been installed in the system.

-a, --all
   By default, mpac will merge packages with same name and only print
   the highest version, using this option to let it show all matched
   versions.

-A, --include-disabled
   Also search in disabled media.

-e, --exact
   Do exact match, instead of sub-string match.

-f, --files
   Search files included in the package instead of name and summary.

-m, --media pattern
   Select which media to search.

-n, --names-only
   By default, mpac search against package name and its summary, this
   option will switch it to search name only.

-r, --requires
   Search which package requires it.

-p, --provides
   Search which package provides it.

-t, --terse
   Mpac will not print summary info if this option is enabled.

query (qu) [options] pattern
----------------------------

Mpac query command is used to display details of packages. If no option is
supplied, it print a collection of several information, or it will
print corresponding info specified by option(s).

-a, --all
   Show all matched version.

-A, --include-disabled
   Also search in disabled media.

-c, --changelog
   Print changelog of matched package(s).

-C, --conflicts
   Print conflicts of matched package(s).

-m, --media pattern
   Select which media to search, with case-insensitive.

-p, --provides
   Print provides of matched package(s).

-r, --requires
   Print requires of matched package(s).

-R, --requires-recursive
   Recursively print requires of matched package(s).

-s, --suggests
   Print suggests of matches package(s).

install (in) [options] name ...
-------------------------------

Install specified packages and their dependences, more than one name
can be supplied. Version and release number can also be specified, by
using ``=`` to seperate it from the name.

-A, --include-disabled
   Also search in disabled media.

-d, --download-only
   Do not perform installation, only download rpm packages. They can
   be found at /var/cache/urpmi/rpms.

-m, --media pattern
   From which media to find packages.

-S, --no-suggests
   Do not install suggests packages.

erase (er) [options] name ...
-----------------------------

Erase a package from system, more than one name can be supplied.

-r, --requires
   Also remove all orphans in the system. NOTE: It will remove all the
   orphans, regard less whether it is this package depends on or not.

refresh (re) [options] [pattern]
--------------------------------

By default, mpac refresh package list of all enabled media. If name is
specified, it will only refresh matched ones.

-A, --include-disabled
   Refresh all media, both enabled and disabled ones.

update (up) [options]
---------------------

Refresh package list of all enabled media, and update system.

-R, --no-refresh
   Do not refresh package list.

list (li) [options]
-------------------

With no option, list will print packages in all media.

-a, --all
   Print all version of packages.

-A, --include-disabled
   Also search in disabled media.

-m, --media name
   Select which media to list, match with case-insensitive.

-t, --terse
   Do not print summary info.

addmedia (am) [options] media-name url
--------------------------------------

With no option, addmedia will add a new media located at ``url`` to
the system, with name setting to ``media-name``.

-m, --mirror base-url
   Add a group of media reside in the mirror specified as
   ``base-url``.  ``base-url`` is usually several levels up than media
   ``url``.

-l, --list mirrorlist
   Automatically choose a mirror from the ``mirrorlist`` file and add
   it to the system. A mirrorlist file contains addresses of several
   mirrors and their location info. Addmedia will automatically detect
   the nearest one and add it to the system.

listmedia (lm) [options]
------------------------

With no option, listmedia will list all active media names
(non-ingored ones), along with their status and urls.

-a, --all
   List all media, both enabled and disabled. Enabled ones are indicated
   by a (``+``).

modifymedia (mm) [options] pattern
----------------------------------

Enable or disable media.

-e, --enable
   Enable matched media.

-d, --disable
   Disable matched media.

removemedia (rm) [options] pattern
----------------------------------

With no option, removemedia will remove media name matches ``pattern``.

-a, --all
   Remove all media.
