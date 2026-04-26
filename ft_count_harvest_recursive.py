def ft_helper(n: int):
    if n == 0:
        return
    ft_helper(n - 1)
    print("Day", n)


def ft_count_harvest_recursive():
    days = input("Days until harvest: ")
    ft_helper(int(days))
    print("Harvest time!")
