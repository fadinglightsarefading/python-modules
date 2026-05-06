import sys


def ft_inventory_system() -> None:
    inventory = {}
    entry = []
    i = 1
    while i < len(sys.argv):
        if ':' not in sys.argv[i]:
            print(f"Error: Invalid parametre \'{sys.argv[i]}\'")
        else:
            try:
                entry = sys.argv[i].split(':')
                entry[1] = int(entry[1])
            except ValueError as e:
                print(f"Quantity error for \'{entry[0]}\': {e}")
                i += 1
                continue
            if entry[0] in inventory:
                print(f"Redundant item \'{entry[0]}\': discarding")
            else:
                inventory.update({entry[0]: entry[1]})
        i += 1
    print(f"Got inventory: {inventory}\nItem list: {list(inventory.keys())}")
    print(f"Total quantity of the {len(inventory.keys())} items: {sum(inventory.values())}")
    for key in inventory:
        value = inventory[key]
        print(f"Item {key} represents "
              f"{round(100 / sum(inventory.values()) * inventory[key], 1)}%")
        if inventory[key] == max(inventory.values()):
            item_most = key
        elif inventory[key] == min(inventory.values()):
            item_least = key
    print(f"Item most abundant: {item_most} with quantity {max(inventory.values())}")
    print(f"Item least abundant: {item_least} with quantity {min(inventory.values())}")
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


def main() -> None:
    ft_inventory_system()


if __name__ == "__main__":
    main()
