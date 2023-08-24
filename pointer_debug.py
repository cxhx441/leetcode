from typing import Iterable

MULTI_SYMBOL = "x"


def pointer_debug(arr: str, pointers: dict[int, list[str]]):
    print()
    print(arr)
    places = []

    for i in range(len(arr)):
        if i in pointers.keys():
            if len(pointers[i]) > 1:
                places.append(MULTI_SYMBOL)
            else:
                places.append(pointers[i][0])

        else:
            places.append(" ")
    print(''.join(places))
