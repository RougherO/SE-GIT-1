import tabulate as tb
from db import Inventory

inv = Inventory()


def show():
    print(
        tb.tabulate(
            tabular_data=inv.getItems(),
            headers=["Product Name", "Quantity", "Cost per Item"],
            tablefmt="outline",
            numalign="center",
            stralign="center",
        )
    )


def add():
    name = input("Enter item name: ")
    quant = int(input("Enter quantity of item: "))
    cost = float(input("Enter cost of item: "))

    inv.addItem(name, quant, cost)
    print(f"{name} has been added to the inventory")


def remove():
    name = input("Enter item name to remove: ")

    inv.removeItem(name)
    print(f"{name} has been removed from the inventory")


def update():
    name = input("Enter item name to update: ")
    quant = input("Enter new quantity[N/n to skip]: ")
    cost = input("Enter new cost[N/n to skip]: ")

    quant = int(quant) if quant.lower() != "n" else None
    cost = float(cost) if cost.lower() != "n" else None

    inv.updateItem(name, quant, cost)
