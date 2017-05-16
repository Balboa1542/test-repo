from IPython.display import clear_output
while True:
    item = input("> ")
    if int(item) == 2:
        clear_output()
        print("{} is Correct!".format(item))
        break
    else:
        clear_output()
        print("{} is incorrect, please try again...".format(item))
        continue

