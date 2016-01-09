#!/usr/bin/python
import re

from aggregator import aggregate
from element import Element
from latex2mathml.commands import MATRICES, SPACES
from symbols_parser import convert_symbol

__author__ = 'Ronie Martinez'

commands = {
    # command: (params_count, mathml_equivalent, attributes)
    '_': (2, 'msub', {}),
    '^': (2, 'msup', {}),
    '_^': (3, 'msubsup', {}),
    r'\frac': (2, 'mfrac', {}),
    r'\sqrt': (1, 'msqrt', {}),
    r'\root': (2, 'mroot', {}),
    r'\binom': (2, 'mfrac', {'linethickness': 0}),
    r'\left': (1, 'mo', {'stretchy': 'true', 'fence': 'true', 'form': 'prefix'}),
    r'\right': (1, 'mo', {'stretchy': 'true', 'fence': 'true', 'form': 'postfix'}),
    r'\overline': (1, 'mover', {}),
    r'\underline': (1, 'munder', {}),
}

for space in SPACES:
    commands[space] = (0, 'mspace', {'width': '0.167em'})

for matrix in MATRICES:
    commands[matrix] = (1, 'mtable', {})


def convert(latex):
    math = Element('math')
    math.pretty = True
    row = math.append_child('mrow')
    _classify_subgroup(aggregate(latex), row)
    return str(math)


def _convert_matrix_content(param, parent, alignment=None):
    for row in param:
        mtr = parent.append_child('mtr')
        for element in row:
            if alignment:
                column_align = {'r': 'right', 'l': 'left', 'c': 'center'}.get(alignment)
                mtd = mtr.append_child('mtd', None, columnalign=column_align)
            else:
                mtd = mtr.append_child('mtd')
            if isinstance(element, list):
                _classify_subgroup(element, mtd)
            else:
                _classify(element, mtd)


def _classify_subgroup(elements, row):
    iterable = iter(xrange(len(elements)))
    for i in iterable:
        element = elements[i]
        if isinstance(element, list):
            _row = row.append_child('mrow')
            _classify_subgroup(element, _row)
        elif element in commands:
            _get_prefix_element(element, row)
            params, tag, attributes = commands[element]
            parent = row.append_child(tag, None, **attributes)
            alignment = None
            if element in MATRICES and element.endswith('*'):
                i += 1
                alignment = elements[i]
                iterable.next()
            for j in range(params):
                i += 1
                param = elements[i]
                if element == r'\left' or element == r'\right':
                    symbol = convert_symbol(param)
                    parent.text = param if symbol is None else '&#x{};'.format(symbol)
                elif element in MATRICES:
                    _convert_matrix_content(param, parent, alignment)
                else:
                    if isinstance(param, list):
                        _parent = parent.append_child('mrow')
                        _classify_subgroup(param, _parent)
                    else:
                        _classify(param, parent)
            _get_postfix_element(element, row)
            if element == r'\overline':
                parent.append_child(Element('mo', '&#x000AF;', stretchy='true'))
            elif element == r'\underline':
                parent.append_child(Element('mo', '&#x00332;', stretchy='true'))
            [iterable.next() for _ in xrange(params)]
        else:
            _classify(element, row)


def _convert_and_append_operator(symbol, parent):
    symbol = convert_symbol(symbol)
    parent.append_child(Element('mo', '&#x{};'.format(symbol)))


def _get_postfix_element(element, row):
    if element in (r'\binom', r'\pmatrix'):
        _convert_and_append_operator(r'\rparen', row)
    elif element == r'\bmatrix':
        _convert_and_append_operator(r'\rbrack', row)
    elif element == r'\Bmatrix':
        _convert_and_append_operator(r'\rbrace', row)
    elif element == r'\vmatrix':
        _convert_and_append_operator(r'\vert', row)
    elif element == r'\Vmatrix':
        _convert_and_append_operator(r'\Vert', row)


def _get_prefix_element(element, row):
    if element in (r'\binom', r'\pmatrix'):
        _convert_and_append_operator(r'\lparen', row)
    elif element == r'\bmatrix':
        _convert_and_append_operator(r'\lbrack', row)
    elif element == r'\Bmatrix':
        _convert_and_append_operator(r'\lbrace', row)
    elif element == r'\vmatrix':
        _convert_and_append_operator(r'\vert', row)
    elif element == r'\Vmatrix':
        _convert_and_append_operator(r'\Vert', row)


def _classify(_element, parent):
    symbol = convert_symbol(_element)
    if re.match('\d+(.\d+)?', _element):
        parent.append_child(Element('mn', _element))
    elif _element in '+-*/()=':
        parent.append_child(Element('mo', _element if symbol is None else '&#x{};'.format(symbol)))
    elif symbol and (int(symbol, 16) in xrange(int('2200', 16), int('22FF', 16) + 1) or
                             int(symbol, 16) in xrange(int('2190', 16), int('21FF', 16) + 1)):
        parent.append_child(Element('mo', '&#x{};'.format(symbol)))
    elif _element.startswith('\\'):
        if symbol is not None:
            parent.append_child(Element('mi', '&#x{};'.format(symbol)))
        else:
            e = _element.lstrip('\\')
            parent.append_child(Element('mi', e))
    else:
        parent.append_child(Element('mi', _element))
