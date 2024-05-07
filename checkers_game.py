# import items from numpy library using "from" import construct

from numpy import random
from numpy import sum


# create build_board function that takes size parameter
def build_board(size):
    pieces = ['Empty', 'Red', 'Black']
    # random.choice inputs the names of the pieces randomly into board
    board = random.choice(pieces, size=(size, size))
    # returns board array
    return board


# create get_count function that gets the count of a specific item on board
def get_count(board, piece):
    # using numpy sum function to count occurrences of item within an array
    count = sum(board == piece)
    return count


if __name__ == "__main__":
    print("This file is not intended to be run as a main.")
