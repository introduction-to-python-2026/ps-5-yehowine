def split_before_uppercases(formula):
    start = 0
    end = 1
    elements_lst = []

    if not formula:
        return elements_lst

    # לולאה על המחרוזת החל מהאינדקס השני
    while end < len(formula):
        if formula[end].isupper():
            elements_lst.append(formula[start:end])
            start = end
        end += 1
    
    # הוספת החלק האחרון של המחרוזת (היסוד האחרון)
    elements_lst.append(formula[start:])

    return elements_lst

def split_at_digit(formula):
    for char_index, char in enumerate(formula):
        if char.isdigit():
            # מפריד שם (עד הספרה) וכמות (החל מהספרה)
            return formula[:char_index], int(formula[char_index:])
    return formula, 1

def count_atoms_in_molecule(molecular_formula):
    atoms_count_dict = {}
    
    for atom in split_before_uppercases(molecular_formula):
        atom_name, atom_count = split_at_digit(atom)
        # עדכון המילון: מוסיף את הספירה הנוכחית לספירה הקיימת (או 0 אם חדש)
        atoms_count_dict[atom_name] = atoms_count_dict.get(atom_name, 0) + atom_count
    return atoms_count_dict


def parse_chemical_reaction(reaction_equation):
    """Takes a reaction equation (string) and returns reactants and products as lists. 
    Example: 'H2 + O2 -> H2O' -> (['H2', 'O2'], ['H2O'])"""
    
    # הסרת כל הרווחים
    reaction_equation = reaction_equation.replace(" ", "")
    
    if "->" not in reaction_equation:
        return [], []
        
    # שמירה על רווחים נקיים סביב סימני ההשמה
    reactants, products = reaction_equation.split("->")
    
    return reactants.split("+"), products.split("+")

def count_atoms_in_reaction(molecules_list):
    """Takes a list of molecular formulas and returns a list of atom count dictionaries. 
    Example: ['H2', 'O2'] -> [{'H': 2}, {'O': 2}]"""
    
    molecules_atoms_count = []
    
    for molecule in molecules_list:
        molecules_atoms_count.append(count_atoms_in_molecule(molecule))
        
    # ה-return מוזח כעת נכונה (אותה הזחה כמו הלולאה for)
    return molecules_atoms_count
 
