# graphviz - create dot, save, render, view

"""Assemble DOT source code and render it with Graphviz.

>>> import graphviz
>>> dot = graphviz.Digraph(comment='The Round Table')

>>> dot.node('A', 'King Arthur')
>>> dot.node('B', 'Sir Bedevere the Wise')
>>> dot.node('L', 'Sir Lancelot the Brave')

>>> dot.edges(['AB', 'AL'])

>>> dot.edge('B', 'L', constraint='false')

>>> print(dot)  #doctest: +NORMALIZE_WHITESPACE
// The Round Table
digraph {
    A [label="King Arthur"]
    B [label="Sir Bedevere the Wise"]
    L [label="Sir Lancelot the Brave"]
    A -> B
    A -> L
    B -> L [constraint=false]
}
"""

from .backend import (render, pipe, unflatten, version, view,
                      ENGINES, FORMATS, RENDERERS, FORMATTERS,
                      ExecutableNotFound, RequiredArgumentError)
from .dot import Graph, Digraph
from .files import Source
from .lang import escape, nohtml

__all__ = ['Graph', 'Digraph',
           'Source',
           'escape', 'nohtml',
           'render', 'pipe', 'unflatten', 'version', 'view',
           'ENGINES', 'FORMATS', 'RENDERERS', 'FORMATTERS',
           'ExecutableNotFound', 'RequiredArgumentError']

__title__ = 'graphviz'
__version__ = '0.17.1.dev0'
__author__ = 'Sebastian Bank <sebastian.bank@uni-leipzig.de>'
__license__ = 'MIT, see LICENSE.txt'
__copyright__ = 'Copyright (c) 2013-2021 Sebastian Bank'

#: :class:`set` of known layout commands used for rendering (``'dot'``, ``'neato'``, ...)
ENGINES = ENGINES

#: :class:`set` of known output formats for rendering (``'pdf'``, ``'png'``, ...)
FORMATS = FORMATS

#: :class:`set` of known output formatters for rendering (``'cairo'``, ``'gd'``, ...)
FORMATTERS = FORMATTERS

#: :class:`set` of known output renderers for rendering (``'cairo'``, ``'gd'``, ...)
RENDERERS = RENDERERS

ExecutableNotFound = ExecutableNotFound

RequiredArgumentError = RequiredArgumentError
