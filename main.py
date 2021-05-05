import sys
from os import path

def __fix_path__():
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

if __name__ == '__main__':
    __fix_path__()

    from chem_parser import MolecularParser

    print('Please enter an arbitrary molecular formula:')
    formula = input()
    parser = MolecularParser(formula)
    try:
            parser.process_formula()
            print(f'{formula} -->', repr(parser))
    except:
            print("Error: Chemical formula not recognized")