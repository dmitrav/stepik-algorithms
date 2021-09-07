
def read_items():
    n, volume = [int(x) for x in input().split()]
    items = []
    for i in range(n):
        item = [int(x) for x in input().split()]
        items.append(tuple(item))

    return volume, items


def sort_items_by_volume_unit_price(items):

    for i in range(1, len(items)):
        key = items[i]
        key_volume_unit_price = key[0] / key[1]  # price / volume
        j = i - 1
        while j >= 0 and items[j][0] / items[j][1] > key_volume_unit_price:
            items[j+1] = items[j]
            j -= 1
        items[j+1] = key

    return items


def pack_backpack(volume, sorted_items):

    # items are sorted in the increasing order,
    # so go from the last to the first
    i, total_price = len(sorted_items)-1, 0

    while i >= 0:
        if sorted_items[i][1] >= volume:
            total_price += sorted_items[i][0] / sorted_items[i][1] * volume
            return total_price
        else:
            volume -= sorted_items[i][1]
            total_price += sorted_items[i][0]
            i -= 1

    return total_price


if __name__ == "__main__":

    volume, items = read_items()
    sorted_items = sort_items_by_volume_unit_price(items)
    total_price = pack_backpack(volume, sorted_items)
    print(total_price)
