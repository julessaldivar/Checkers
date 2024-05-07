# import checkers_game library
import checkers_game as checkers


# Create game function that uses build_board function
def game():
    # input for size of the board
    size = int(input("Enter the size of the board: "))
    board = checkers.build_board(size)
    print("Checkers Board:")
    print(board)
    print(f"Number of Empty Cells: {checkers.get_count(board, 'Empty')}")
    print(f"Number of Red Cells: {checkers.get_count(board, 'Red')}")
    print(f"Number of Black Cells: {checkers.get_count(board, 'Black')}")


# check to see if running as main
if __name__ == "__main__":
    game()
