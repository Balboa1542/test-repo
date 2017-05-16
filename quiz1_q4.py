from IPython.display import clear_output
while True:
    item = input("")
    if item == "append":
        clear_output()
        print("my_list.{}(1) is Correct!".format(item))
        break
    else:
        clear_output()
        print("my_list.{}(1) is incorrect, please try again...".format(item))
        continue

