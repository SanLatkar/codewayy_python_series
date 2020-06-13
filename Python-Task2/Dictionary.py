#Working with methods of Dictionaries:


Vedas = {"A": "Atharvaveda", "R": "Rigveda", "S": "Samveda", "Y": "Yajurveda"}            # Creating a Vedas Dictionary:
print("The dictionary of Vedas : ", Vedas)

get_vedas = Vedas.get("S")           # get() gives us value assigned to key mentioned
print("\nvalue for the 'S' key is: ", get_vedas)

keys = Vedas.keys()                # keys() gives us all the keys in Dictionary
print("\nKeys of Vedas: ", keys)

values = Vedas.values()             # values() gives us all the values in Dictionary
print("\nValues of Vedas : ", values)

items = Vedas.items()              # items() gives us all the items in Dictionary
print("\nItems of Vedas: ", items)

length = len(Vedas)                # len() gives us length of tuple means it gives number of values in Dictionary
print("\nTotal number of the Vedas is: ", length)

Vedas.pop("Y")                     # pop() is used to remove particular item from Dictionary
print("\nThe Vedas dictionary after performing a pop('Y') opearation: ", Vedas)

Trivedas = Vedas.copy()          # copy() is used to copy one dictionary to another
print("\nThe new copy of Vedas dictionary is: ", Trivedas)
