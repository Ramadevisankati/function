# def count_down(start):
#     """ Count down from a number  """
#     print(start)
#     count_down(start-1)
# count_down(3)


def count_down(start):
    """ Count down from a number  """
    print(start)
    next = start - 1
    if next > 0:
        count_down(next)


count_down(3)
