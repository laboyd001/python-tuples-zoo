# create a tuple named 'zoo' that contains your favorite animals:
zoo = ("lion", "hippo", "flamingo")
print("Here's the zoo tuple:", zoo)

# find one of your animals using the .index(value) method on the tuple:
print("This is the animal found with index 0:", zoo[0])

# Determine if an animal is in your tuple by using a keyword:
if 'hippo' in zoo:
    print("The hippo is in the zoo.")
else:
    print("The hippo is not in the zoo.")

# Create a variable for each of the animals in your tuple
(lion, hippo, flamingo) = zoo
print("Show me a 'hipppo':", hippo)

# Convert your tuple into a list:
my_list = list(zoo)
print("This is my zoo list:", my_list)

# Use extend() to add three more animals to your zoo
more_animals = ['snake', 'monkey', 'giraffe']
my_list.extend(more_animals)
print("Here's a larger list of zoo animals:", my_list)

# Convert the list back to a tuple:
new_zoo = tuple(my_list)
print("Here's the larger zoo list as a tuple:", new_zoo)
