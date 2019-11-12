# *******How do I define a list?
grocery_list = ["eggs", "milk", "bread"]

# *******How do I get the length of a list?
len(grocery_list)

# ******How do I access a single item in a list?
grocery_list[1]
# 'milk'
grocery_list[0]
# 'eggs'
#Python indexes start at 0

# ******How do I add stuff to a list?
grocery_list.append("beer")
# ['eggs', 'milk', 'bread', 'beer']
grocery_list.append("cat food")
# ['eggs', 'milk', 'bread', 'beer', 'cat food']

# ******How do I access the last item in a list?
grocery_list[-1]

# *******How do I access multiple items in a list?
grocery_list[0:3] # known as a slice (Starts at index[0] and goes up to but not including index[3]) 

# *******What is "iteration" and how do I do that with a list?
# To iterate a list, use a FOR LOOP
# You need to buy: eggs
# You need to buy: milk
# You need to buy: bread 
# ... 
for item in grocery_list:
    print(f"You need to buy {item}")
    # Item is an automatic variable

# *******How do I replace stuff in a list?
grocery_list[1] = "almond milk"
# replaces "milk" with "almond milk"

# *******How do I replace multiple items in a list?
# grocery_list[0:3] = "chocolate"
# grocery_list["c", "h", "o", "c", "o", "l", "a", "t", "e", "beer", "cat food"]
# Don't do that
an_item = "awesome" + an_item
for item in grocery_list:
    grocery_list[???] = "awesome " + item

# replaces everything with cheese
index = 0
while index < len(grocery_list):
    # print(grocery_list[index])
    grocery_list[index] = "cheese"
    index += 1
# adds awesome before every list entry
index = 0
while index < len(grocery_list):
    # print(grocery_list[index])
    grocery_list[index] = "awesome" + grocery_list[index]
    index += 1


# ******How do I remove stuff from a list?
grocery_list.pop() #---->gives/removes last item of the list until list is empty \

#H******How to combine lists?
grocery_list = ["eggs", "milk", "bread"]
snacks = ["gummy bears", "pringles", "more beer"] 
for snakcs in snacks:
    grocery_list.append(snacks)

grocery_list.extend(snacks)

# list can be concatinated!
grocery_list + snacks
new_grocery_list = grocery_list + snacks

#******How do I create a list of lists
chris_dirs = ["Jonathan", "Tedge"]
seans_dirs = ["Evan", "Eric"]

all_dirs = [chris_dir, seans_dir]
all_dirs
[['Jonathan', 'Tedge'], ['Evan', 'Eric']]

#******How do I access items in a list... that's inside another list?
# NESTED LISTS
all_dirs = [chris_dir, seans_dir]
all_dirs
[['Jonathan', 'Tedge'], ['Evan', 'Eric']]
all_dirs[0]
['Jonathan', 'Tedge']
all_dirs[0][1]
'Tedge'
all_dirs[0][1] = ["Liz", "Tasha"]
all_dirs
[["Jonathan", ["Liz", "Tasha"]] ["Evan", "Eric"]]
all_dirs[0][1][1]
"Tasha"
all_dirs[0][1] = "Tedge"
[['Jonathan', 'Tedge'], ['Evan', 'Eric']]

count = 0
for dir_list in all_dirs:
    print(dir_list)
["Jonathan", "Tedge"]
["Evan", "Eric"]
    for name in dir_list:
    print(name)
    count += 1

count?

Jonathan
Tedge
Evan
Eric

4