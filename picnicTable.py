# ljust() rjust() center()


def printItems(picnicitems, leftjustify, rightjustify):

    print()

    print("PICNIC ITEMS".center(leftjustify + rightjustify, "-"))

    for k, v in picnicitems.items():

        print(k.ljust(leftjustify, ".") + str(str(v).rjust(rightjustify)))


picnicItems = {"apple": 12, "sandwiches": 15, "juices": 12, "snacks": 28}

printItems(picnicItems, 19, 1)
