#from IPython import get_ipython
#import IPython
# coding: utf-8

# <a id="home"></a>

# # Python Collections

# ## Lists

# ## Tasks:
#
# - [Code Challenge 1](#task1)
# - [Code Challenge 2](#task2)
# - [Code Challenge 3](#challenge3)
# - [Code Challenge 4](#challenge4)
#
# ## Topics & Functions:
#
# - [Lists](#lists)
# - [Adding to lists](#adding)
# - [Extend lists](#extend)
# - [Insert into lists](#insert)
# - [Shopping List App](#shopping)
# - [Delete from a list](#delete)
# - [Remove from a list](#remove)
# - [Pop off a list](#pop)
#
# ## Quizzes:
#
# - [Quiz 1](#quiz1)

# <a id="task1"></a>

# ### Code Challenge 1:
#
# - Create a *list* that contains **3 numbers, 2 strings & 1 sublist with 2 items**.

# In[33]:

# my_list created with required items
my_list = [1,2,3,"string1","string2",[2,"items"]]


# <a id="lists"></a>
# [Return to Top](#home)

# ### Lists

# Now we will work with lists and start by creating a list:

# In[6]:

favorite_things = ["raindrops on roses", "whiskers on kittens", "bright copper kettles"]


# If we print the list we will see the 3 items included:

# In[7]:

favorite_things


# <a id="adding"></a>
# [Return to Top](#home)

# ### Adding to lists

# Now to add just one thing to our list we will use the plus sign.

# In[9]:

favorite_things + ["warm woolen mittens"]


# However you will notice that the addition was not permanant when we print out the list below:

# In[10]:

favorite_things


# To make the addition permanent we will use **"+="**.

# In[11]:

favorite_things += ["warm woolen mittens"]


# In[12]:

favorite_things


# <a id="append"></a>
# [Return to Top](#home)

# ### Append

# The **append()** method works pretty much the same way.

# In[13]:

favorite_things.append(["bright paper packages tied with string"])


# In[14]:

favorite_things


# Whoops, we accidentally added a list to our list, instead of a string. To fix this we will use the **del()** function with the index. Because this is the last item in the list we can reference its position as **-1**.

# In[15]:

del favorite_things[-1]


# In[16]:

favorite_things


# Now to use **append()** again but correctly this time passing an item instead.

# In[17]:

favorite_things.append("bright paper packages tied with string")


# In[18]:

favorite_things


# <a id="extend"></a>
# [Return to Top](#home)

# ### Extend lists

# **Extend()** however will allow us to add itesm from one list onto the end of another list.

# In[19]:

favorite_things.extend(["cream colored ponies","crisp apple strudels"])


# In[20]:

favorite_things


# **Extend()** can be used with any iterable even if it isn't a list. Example below:

# In[21]:

a = [1,2,3]


# In[22]:

a.extend("abc")


# In[23]:

a


# As you can see the *string* of "abc" was added as list items when it is iterated.

# <a id="insert"></a>
# [Return to Top](#home)

# ### Insert into lists

# **Insert()** however lets us add an item to a list at whatever index we designate. Essentially the reverse of **del()**. See the example below of removing **"whiskers on kittens"** at index **1** and the insertion of the string back into index **1**.

# In[24]:

del favorite_things[1]


# In[25]:

favorite_things


# In[26]:

favorite_things.insert(1, "whiskers on kittens")


# In[27]:

favorite_things


# As you can see **"whiskers on kittens"** was added back to the list at item **1** that we specified. Note that we have been changing the list rather than creating different variations of the list. This is an example of the mutability of lists.

# <a id="task2"><a/>
# [Return to Top](#home)

# ### Code Challenge 2:
#
# - Create a list variable called "best" with 3 items
# - Using .extend(), .append(), or +, add two new items onto the end of best
# - Use the .insert() method to place the string "start" at the beginning of the "best" list

# In[34]:

# best created with required number of items
best = ["apples","oranges","bananas"]


# In[35]:

# Extend() was used to add 2 items to list
best.extend(["grapes","pears"])


# In[36]:

best


# In[42]:

# Insert() was used to add "start" to index 0
best.insert(0,"start")


# In[41]:

best


# <a id="shopping".<a/>
# [Return to Top](#home)

# ### Shopping List App

# In[74]:

# Needed for new function to clear screen between states
# Alows us to look at information about the machine running the app
# Also allows to run system level scripts like "clear" on non-Windows computers
import os
#While in our iPython environment we will use clear_output
from IPython.display import clear_output


# In[121]:

shopping_list = []

# This will clear the screen
# "nt" identifies version of Windows that need to call "cls"
# For any other OS we will call "clear"
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
    if os.name == "posix":
        clear_output()

def show_help():
    clear_screen()
    print("What should we pick up at the store?")
    print("""
            Enter 'DONE' to stop adding items.
            Enter 'HELP' for this help.
            Enter 'SHOW' to see your current list.
            Enter 'REMOVE' to delete an item from your list.
            """)

def add_to_list(item):
    show_list()
    if len(shopping_list):
        position = input("Where should I add {}?\n"
                         "Press ENTER to add to the end of the list"
                         "> ".format(item))
    else:
        position = 0
    try:
        position = abs(int(position))
    except ValueError:
        position = None
    if position is not None:
        shopping_list.insert(position-1, item)
    else:
        shopping_list.append(new_item)
    show_list()

def show_list():
    clear_screen()
    index = 1
    print("Here's your list:")
    for item in shopping_list:
        print("{}. {}".format(index,item))
        index += 1
    print("-"*10)

def remove_from_list():
    show_list()
    what_to_remove = input("What would you like to remove?\n> ")
    try:
        shopping_list.remove(what_to_remove)
    except ValueError:
        pass
    show_list()

show_help()

while True:
    new_item = input("> ")

    if new_item.upper() == 'DONE' or new_item.upper() == 'QUIT':
        break
    elif new_item.upper() == 'HELP':
        show_help()
        continue
    elif new_item.upper() == 'SHOW':
        show_list()
        continue
    elif new_item.upper() == 'REMOVE':
        remove_from_list()
    else:
        add_to_list(new_item)

show_list()


# <a id="quiz1"></a>
# [Return to Top](#home)

path = "/Users/kierstenmuther/Team_Treehouse/Python_Collections_Lists/"

clear_screen()
print("Quiz 1")

print("Question 1:\n\n"
"What does the first_list.extend(second_list) method do?\n\n"
"1. Nothing, this isn't a real method.\n"
"2. Inserts the second list into the first list.\n"
"3. Adds the contents of the first list into the second list.\n"
"4. Adds the contents of the second list into the first list.\n")


# Attempt answering the question:
get_ipython().magic('run {}quiz1_q1.py'.format(path))

clear_screen()
print("Quiz 1\n"
"Question 2:\n\n"
"What is the first argument to the .insert() method?\n\n"
"1. A boolean that says whether or not to create a new list.\n"
"2. Index - the position in the list that you want something inserted.\n"
"3. Content - the thing you want instered into the list.\n"
"4. The list to insert something into.\n")

# Attempt answering the question:
get_ipython().magic('run {}quiz1_q2.py'.format(path))


clear_screen()
print("""Quiz 1
Question 3:\n
letters = ["A", "B", "C"]
letters.append(["D", "E", "F"])\n
What will letters be at the end of this?\n
1. ["A", "B", "C",["D", "E", "F"]]
2. [["A", "B", "C"],"D", "E", "F"]
3. It'll throw an error because you can't append a list to a list.
4. ["A", "B", "C", "D", "E", "F"]\n""")

# Attempt answering the question:
get_ipython().magic('run {}quiz1_q3.py'.format(path))

clear_screen()
print("""Quiz 1
Question 4:\n
I want my_list to have 1 as the last item.
Complete this method call:\n
my_list.`__________`(1)\n""")

# Attempt answering the question:
get_ipython().magic('run {}quiz1_q4.py'.format(path))


clear_screen()
print("""Quiz 1
Question 5:\n
What does the list() function do?\n
1. Create a new list.
2. Turns an iterable into a list.
3. Checks to see if something is a list.
4. Both 1 & 2.\n""")

# Attempt answering the question:
get_ipython().magic('run {}quiz1_q5.py'.format(path))


clear_screen()
print("""Quiz 1
Question 6:\n
The + symbol is used to concatenate two lists together, just like with strings.\n
1. True
2. False\n""")

# Attempt answering the question:
get_ipython().magic('run {}quiz1_q6.py'.format(path))


# <a id="delete"><a/>
# [Return to Top](#home)

# ### Delete from a list

# In[111]:

alpha_list = ["a", "b", "z", "c", "d"]


# In[112]:

del alpha_list[2]


# In[113]:

alpha_list


# <a id="remove"><a/>
# [Return to Top](#home)

# ### Remove from a list

# In[114]:

my_list = [1,2,3,1]


# Lets use the **remove()** command to remove the last 1.

# In[115]:

my_list.remove(1)


# In[116]:

my_list


# Unfortunately that removed the wrong 1. That's because it removes the first instance.

# In[117]:

my_list.remove(1)


# In[118]:

my_list


# my_list.remove(1) will now return a ValueError because there are no **1's** left in the list.

# <a id="challenge3"><a/>
# [Return to Top](#home)

# ### Code Challenge 3:
#
# OK, I need you to finish writing a function for me. The function *disemvowel* takes a single word as a parameter and then returns that word at the end.
#
# I need you to make it so, inside of the function, all of the vowels **("a", "e", "i", "o", and "u")** are removed from the word. Solve this however you want, it's totally up to you!
#
# Oh, be sure to look for both uppercase and lowercase vowels!

# In[143]:

def disemvowel(word):
    ls = []
    vowels = ["a","e","i","o","u","A","E","I","O","U"]
    ls += word
    for vowel in vowels:
        try:
            ls.remove(vowel)
        except ValueError:
            pass
    word = ''.join(ls)
    return word


# We will test this on the word **because** with some vowels uppercase and lowercase.

# In[144]:

test = "BecAusE"


# In[145]:

disemvowel(test)


# <a id="pop"><a/>
# [Return to Top](#home)

# ### Pop item off list

# This will not only remove an item from a list but it will return the item from the command so it can be stored and saved if necessary.

# In[146]:

names = ["Brady", "Sikander", "Joe", "Dylan", "Carlos", "Josh"]


# In[147]:

name1 = names.pop()


# In[148]:

name1


# Without an index declaration **pop()** remove the last item.

# In[149]:

name2 = names.pop(3)


# In[150]:

name2


# As you can see when we referenced index **3** the function removed **Dylan** who was listed in the **3** position.

# In[151]:

names


# Just as expected **Josh** and **Dylan** are no longing in the list.

# In[156]:

clear_screen()

sodas = ["Pepsi", "Cherry Coke Zero", "Sprite"]
chips = ["Doritos", "Fritos"]
candy = ["Snickers", "M&Ms", "Twizzlers"]

while True:
    choice = input("Would you like a SODA, some CHIPS, or a CANDY? (DONE to quit) ").lower()
    try:
        if choice == "soda":
            snack = sodas.pop()
        elif choice == "chips":
            snack = chips.pop()
        elif choice == "candy":
            snack = candy.pop()
        elif choice == "done":
            break
        else:
            print("Sorry I didn't understand that.")
            continue
    except IndexError:
        print("We're all out of {}! Sorry!".format(choice))
    else:
        print("Here's your {}: {}".format(choice, snack))


# <a id="challenge4"><a/>
# [Return to Top](#home)

# ### Code Challenge 4:
#
# Alright, my list is messy! Help me clean it up!
#
# First, start by moving the 1 from index 3 to index 0.
#
# Try to do this in a single step by using both **.pop() and .insert()**.
#
# It's OK if it takes you more than one step, though!

# In[165]:

messy_list = ["a", 2, 3, 1, False, [1, 2, 3]]
# Your code goes below here
zero = messy_list.pop(3)
messy_list.insert(0, zero)


# In[166]:

messy_list


# Great! Now use .remove() and/or del to remove the string, the boolean, and the list from inside of messy_list.
#
# When you're done, messy_list should have only integers in it.

# In[167]:

del messy_list[5]
del messy_list[4]
del messy_list[1]


# In[168]:

messy_list

clear_screen()
