# pyfactorie
[![Build Status](https://travis-ci.org/eddotman/pyfactorie.svg?branch=master)](https://travis-ci.org/eddotman/pyfactorie)
Python wrapper for Factorie

# Installation
Use PyPI:

    pip install pyfactorie

# Usage
First, have the [Factorie](htpp://factorie.cs.umass.edu) package installed. Run the nlp server (example run command below):

    bin/fac nlp --wsj-forward-pos --transition-based-parser --conll-chain-ner

Then use the `parse_sentence("YOUR_SENTENCE")` to throw sentences at the parser and receive nested node structures. Each node will look like this:

    #Node
    {
        "name": str,
        "children": [Node],
        "data": {
            "id":        int,
            "sent_id":   int,
            "pos":       str,
            "parent_id": int,
            "phrase":    str
        }
    }

Each node can `add_child(Node)` which works in exactly the way you would expect. There is also a `NodeHandler` class that helps with some basic search and traversing algorithms.
