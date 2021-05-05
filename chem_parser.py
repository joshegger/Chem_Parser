import re
from collections import defaultdict

"""The general approach is to use Regex and recursion to parse arbitrary chemical
formulas and obtain the desired output"""

class MolecularParser:

    opening_brackets = r'[\(\[\{]'
    closing_brackets = r'[\)\]\}](\d+)?'
    str_atom_re = r'([A-Z][a-z]?)(\d+)?'

    # defaultdict allows us to insert key into dict if it doesn't exist
    def __init__(self, formula):
        self.formula = formula
        self._stack = [defaultdict(int)]

    def process_formula(self):
        """
        Public interface to begin the processing of provided formula
        """
        self._process_formula(self.formula)

    def _process_formula(self, formula):
        """
        Recursively looks through the given molecular formula as well as all of its subformulas,
         checking the following conditions:

        1. If opening bracket is encountered (e.g. '['):
            - This indicates that a new formula has been found, and should be processed recursively
         The new formula is initially added to a stack as an empty dictionary, and is subsequently
         popped from the stack when we hit the appropriate closing bracket. We then continue from the start

        2. If a closing bracket is encountered (e.g. ']'):
            - We consider the part-formula as processed and pop it out from the stack

        3. If an atom is encountered (e.g. Mg):
            - We check whether there is a multiplier, if so, we add the multiplied value. If there is no
            multiplier, we assume a multiplier of 1.

        """
        # Set remainder equal to 'None'
        r = None

        # Regular expression matching for each of the three cases:
        atom = re.match(MolecularParser.str_atom_re, formula)
        opening = re.match(MolecularParser.opening_brackets, formula)
        closing = re.match(MolecularParser.closing_brackets, formula)

        # If atom is identified:
        if atom:
            r = formula[len(atom.group()):]
            self._stack[-1][atom.group(1)] += int(atom.group(2) or 1)

        # If opening brackets encountered:
        elif opening:
            r = formula[len(opening.group()):]
            self._stack.append(defaultdict(int))

        # If closing brackets encountered:
        elif closing:
            r = formula[len(closing.group()):]
            for (k, v) in self._stack.pop().items():
                self._stack[-1][k] += v * int(closing.group(1) or 1)

        # If anything remains, process remainders recursively as nested formulas:
        if r:
            self._process_formula(r)

    # Python object representation for the class object
    def __repr__(self):

        return '%r' % dict(self._stack[0])

    # String representation for the class object
    def __str__(self):
        """
        string identifier of the class object
        """
        return self.formula
