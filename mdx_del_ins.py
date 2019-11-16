#! /usr/bin/env python


'''
Del/Ins Extension for Python-Markdown
=====================================

Wraps the inline content with ins/del tags.


Usage
-----

    >>> import markdown
    >>> src = """This is ++added content++ and this is ~~deleted content~~""" 
    >>> html = markdown.markdown(src, ['del_ins'])
    >>> print(html)
    <p>This is <ins>added content</ins> and this is <del>deleted content</del>
    </p>


Dependencies
------------

* [Markdown 3](https://pypi.org/project/Markdown/)


Copyright
---------

2011, 2012 [The active archives contributors](http://activearchives.org/)
All rights reserved.

This software is released under the modified BSD License. 
See LICENSE.md for details.
'''


import markdown
from markdown.inlinepatterns import SimpleTagPattern

# Matches:
# ~~ (literal)
# any character that isn't white space or a ~
# Any character (except ~) OR a ~ that isn't followed by another ~, matching as many characters as required (lazy)
# any character that isn't white space or a ~
# ~~ (literal)
# INS uses +s instead of ~s
DEL_RE = r"(\~\~)([^\s\~](?:(?:[^\~]|\~(?!\~))*?[^\s~])?)(\~\~)"
INS_RE = r"(\+\+)([^\s\+](?:(?:[^\+]|\+(?!\+))*?[^\s+])?)(\+\+)"
# r"(\~\~)(\S(?:.*?\S)?)(\~\~)"
# r"(\~\~)([^\s~](?:.*?[^\s~])?)(\~\~)"


class DelInsExtension(markdown.extensions.Extension):
    """Adds del_ins extension to Markdown class."""

    def extendMarkdown(self, md):
        """Modifies inline patterns."""
        md.inlinePatterns.add('del', SimpleTagPattern(DEL_RE, 'del'), '<not_strong')
        md.inlinePatterns.add('ins', SimpleTagPattern(INS_RE, 'ins'), '<not_strong')


def makeExtension(**kwargs):
    return DelInsExtension(**kwargs)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
