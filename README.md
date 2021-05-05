# Chem_Parser
##


For a given chemical formula represented by a string, Chem_Parser counts the number of atoms of each element contained in the molecule and returns a dictionary.



- Approach: RegEx and Recursion

## Requirements

- The only requirement is the latest version of Python (To date this is 3.9.0)



## Installation

Simply cd into the main directory and run 'main.py':
```sh
cd Chem_Parser
python main.py
```
or just execute the file directly:
```sh
python **YourPathToDirectory**/Chem_Parser/main.py
```


## Examples


Running python main.py will result in a prompt to enter a molecular formula, and behaves as in the following test cases:

Water:
```sh
Please enter an arbitrary molecular formula:
H2O
H2O --> {'H': 2, 'O': 1}
```
Magnesium Hydroxide
```sh
Please enter an arbitrary molecular formula:
Mg(OH)2
Mg(OH)2 --> {'Mg': 1, 'O': 2, 'H': 2}
```
Fremy Salt:
```sh
Please enter an arbitrary molecular formula:
K4[ON(SO3)2]2
K4[ON(SO3)2]2 --> {'K': 4, 'O': 14, 'N': 2, 'S': 4}
```
You can also enter formulas without brackets, like in the following example for biotin:
```sh
Please enter an arbitrary molecular formula:
C10H16N2O3S
C10H16N2O3S --> {'C': 10, 'H': 16, 'N': 2, 'O': 3, 'S': 1}
```
