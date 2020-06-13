# Working with methods of Sets:
# Set does not follow any sequence so we can not use indexing method fon set

Scriptures = {"Atharvaveda", "Samveda", "Rigveda", "Yajurveda"}         # creating a Scriptures set
print("Scriptures are : ", Scriptures)

Scriptures.add("Vedant")            # add() is used to add single element in set
print("\nSet of Scriptures after adding Vedant: ", Scriptures)

Scriptures.update(["Ramayan", "Mahabharat"])            # update() is used to add multiple element in set
print("\nSet of Scriptures after updation of Ramayan,Mahabharat: ", Scriptures)

length = len(Scriptures)            # len() is used to extract length of set
print("\nThe length of Set of Scriptures is: ", length)

Goals = {"Dharma", "Artha", "Kaam", "Moksha"}                       # creating a Goals set
Human = Goals.union(Scriptures)                 # union() combine all distinct values from both sets
print("\nHuman should follow Goals and Scriptures that are: ", Human)

Scriptures.remove("Ramayan")        # remove() removes mentioned element from set
print("\nSet of Scriptures after removing Ramayan: ", Scriptures)

Scriptures.discard("Ramayan")       # discard() also removes mentioned element in list but unlike remove() it don't give error if element is not present in set
print("\nSet of Scriptures after discarding Mahabharat: ", Scriptures)

Scriptures.pop()                    # pop() removes last element from set
print("\nSet of Scriptures after performing a pop opearation: ", Scriptures)

Scriptures.clear()                  # clear() delete all element from set and return empty set
print("\nSet of Scriptures after using clear method: ", Scriptures)
