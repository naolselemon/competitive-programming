# [2, 5, 1, 2, 3, 5, 1, 2, 4] return 2
# [2, 1, 1, 2, 3, 5, 1, 2, 4]  return 1
# [2, 3, 4, 5] return None


def firstRecurringCharacter(arr):
    map = {}
    for n in range(len(arr)):
        current_number = arr[n]

        if current_number in map:
            return arr[n]
        else:
            map[arr[n]] = True

        # print(map)
    return None


print(firstRecurringCharacter([2, 5, 1, 2, 3, 5, 1, 2, 4]))
