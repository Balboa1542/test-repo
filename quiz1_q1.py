from IPython.display import clear_output
while True:
    item = input("> ")
    if int(item) == 4:
        clear_output()
        print("{} is Correct!".format(item))
        print("Press ENTER to continue")
        enter = input("")
        break
    else:
        clear_output()
        print("{} is incorrect, please try again...".format(item))
        continue
