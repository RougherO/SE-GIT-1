from ops import *

while True:
    ch = int(
        input(
            """
Welcome to the Inventory

1) View inventory
2) Add Item
3) Remove Item
4) Update Item information
5) Exit

Enter choice: """
        )
    )
    if ch == 1:
        show()
    elif ch == 2:
        add()
    elif ch == 3:
        remove()
    elif ch == 4:
        update()
    elif ch == 5:
        exit()
    else:
        print("Bad Choice. Try again")
        continue
