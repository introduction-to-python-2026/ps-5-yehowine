def split_before_uppercases(formula):
    start = 0
    elements_lst = []

    if not formula:
        return elements_lst

    # תיקון מבני: שימוש בלולאת for במקום while להגברת הבהירות
    for end in range(1, len(formula)):
        if formula[end].isupper():
            elements_lst.append(formula[start:end])
            start = end
    
    # הוספת החלק האחרון של המחרוזת
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
    
    # *** הוספת הגנת try/except לקריסה של index(1) ***
    try:
        # הפונקציה split_before_uppercases אינה תלויה בערך 1 ברשימה
        # אך אם נרצה להשתמש בקוד המקורי, יש להגן על index()
        for atom in split_before_uppercases(molecular_formula):
            atom_name, atom_count = split_at_digit(atom)
            # עדכון המילון בצורה נקייה
            atoms_count_dict[atom_name] = atoms_count_dict.get(atom_name, 0) + atom_count
        return atoms_count_dict
    
    except ValueError:
        # טיפול בקריסה אם יש בעיה כלשהי בפירוק (לא רלוונטי כאן, אך מוסיף רובסטיות)
        # מכיוון שהקוד המקורי לא משתמש ב- index(1), נשאיר את הפונקציה מוגנת
        # כדי לא לשנות את הלוגיקה העיקרית של הפירוק:
        print("Error during atom counting process.")
        return {}


def parse_chemical_reaction(reaction_equation):
    """Takes a reaction equation (string) and returns reactants and products as lists. 
    Example: 'H2 + O2 -> H2O' → (['H2', 'O2'], ['H2O'])"""
    
    # הסרת כל הרווחים
    reaction_equation = reaction_equation.replace(" ", "")
    
    # פיצול למגיבים ותוצרים
    # הוספת הגנה לטיפול בסוגריים במידה והן לא קיימות (כפי שקורה בשאלה המקורית)
    if "->" not in reaction_equation:
        return [], [] # אם אין חץ, אין תגובה
        
    reactants, products = reaction_equation.split("->")
    
    return reactants.split("+"), products.split("+")

def count_atoms_in_reaction(molecules_list):
    """Takes a list of molecular formulas and returns a list of atom count dictionaries. 
    Example: ['H2', 'O2'] → [{'H': 2}, {'O': 2}]"""
    
    molecules_atoms_count = []
    for molecule in molecules_list:
        molecules_atoms_count.append(count_atoms_in_molecule(molecule))
    return molecules_atoms_count
