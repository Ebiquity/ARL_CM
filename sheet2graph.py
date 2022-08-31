#!/usr/bin/env python
# coding: utf-8

""" convert a DXTRS Bridging Combat Messages excel spreadsheet to an RDF graph.
    e.g.: python sheet2graph.py dxbcm_v5.xls sim5.nt

    if the sheet has multiple tabs, ony the first one is processed.
"""

import argparse
from sheet2rdf import sheet2graph

def get_args( ):
    p = argparse.ArgumentParser()
    p.add_argument('sheet', help='filename of excel spreadsheet with simulator crossing data')
    p.add_argument('graph', nargs='?', default='sim.nt', help='filename for graph output')
    p.add_argument('-f', '--format', nargs='?', default='nt', help='format for graph serialization')
    p.add_argument('-nm', '--no-messages', default=False, action='store_true', help='do not include messages')
    return p.parse_args()

def main(args):
    g = sheet2graph(args.sheet)
    g.serialize(format=args.format, destination=args.graph, encoding="utf-8")
    
if __name__ == '__main__':
    main(get_args())

