SublimeQSL
==========

A sublime Text 2 package for QSL.

Currently supported features:
-----------------------------

- Syntax highlighting:
  - Basic square and angle bracket highlighting.
  - Limited number of keywords.
  - The Python syntax file is imported for LimPy blocks. There is a chance
    that non-LimPy blocks will be seen as Python code in some instances.

*Disclaimer: This is a real messy first draft experimental prototype that
             most likely has all sorts of weird highlighting going on.*

Installation
------------

Note: ``super`` refers to either the ``CMD`` key in Mac OS X or the ``CTRL``
      key in Windows and Linux.

1. Follow the [instructions here](http://wbond.net/sublime_packages/package_control/installation)
    to install Sublime Package Control.

2. Add the repository URL:


    1. Type ``Super+SHIFT+P`` to enter the Command Prompt.
    2. Start typing ``add repository``. Once you see ``Package Control: Add Repository``, type ``Enter``.
    4. In the text box that has appeared at the bottom of the window,
        paste this, and type ``Enter``:

        ``https://raw.github.com/berryp/sublime_package_control_channel/master/repositories.json``

3. Install the SublimeQSL package:

    1. Type ``Super+SHIFT+P`` to enter the Command Prompt.
    2. Start typing ``install package``. Once you see ``Package Control: Install Package``, type ``Enter``.
    3. Type ``qsl`` and press ``Enter``.

Usage
-----

To enable SublimeQSL you either need to

1. Name your files with the ``.qsl`` extension, or
2. Select ``QSL`` from the file type menu in the status bar or in ``View > Syntax``