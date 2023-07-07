import itertools
from colorama import Fore, init, Style


init()


def game_board(game_map, player=0, column=0, row=0, just_display=False):
    try:
        if game_map[column][row] != 0:
            print("This position is occupied. Choose another !")
            return game_map, False
        if not just_display:
            game_map[column][row] = player
        print("   "+"  ".join([str(i) for i in range(len(game_map))]))
        for count, row in enumerate(game_map):
            coloured_item = ""
            for item in row:
                if item == 0:
                    coloured_item += "   "
                elif item == 1:
                    coloured_item += Fore.GREEN + " X " + Style.RESET_ALL
                elif item == 2:
                    coloured_item += Fore.MAGENTA + " O " + Style.RESET_ALL
            print(count, coloured_item)

        return game_map, True
    except IndexError as e:
        print("Make sure you enter numbers between the range shown ", e)
        return game_map, False
    except Exception as e:
        print("Something happened very bad :", e)
        return game_map, False


def win(game_map):

    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True

    # Horizontal
    for row in game_map:
        if all_same(row):
            print(f" Player {row[0]} is Winner Horizontally ")
            return True

    # Vertical
    for i in range(len(game_map)):
        check = []
        for row in game_map:
            check.append(row[i])
        if all_same(check):
            print(f" Player {check[0]} is Winner Vertically ")
            return True

    # Diagonal \
    check = []
    for i in range(len(game_map)):
        check.append(game_map[i][i])
    if all_same(check):
        print(f" Player {check[0]} is Winner Diagonally (\\)")
        return True
    # Diagonally /
    check = []
    for row, col in enumerate(reversed(range(len(game_map)))):
        check.append(game_map[row][col])
    if all_same(check):
        print(f" Player {check[0]} is Winner Diagonally(/) ")
        return True

    # Tied
    n = 0
    for i in game_map:
        n += i.count(0)
    if n == 0:
        print("Game Tied....")
        return True
    return False


play = True
players = [1, 2]
while play:

    try:
        size = int(input("Enter the size of Tic Toc Toe game you want to play : "))
    except ValueError as e:
        print("Enter proper number")
    game = [[0 for i in range(size)] for i in range(size)]

    game_won = False
    game, _ = game_board(game, just_display=True)
    player_choice = itertools.cycle([1, 2])
    while not game_won:
        current_player = next(player_choice)
        print(f"Current player: {current_player}")
        played = False

        while not played:
            try:
                row_choice = int(input("What row do you want to play?  "))
                column_choice = int(input("What column do you want to play?  "))
                game, played = game_board(game, current_player, row_choice, column_choice)
            except ValueError as e:
                print("Enter proper value ..: ", e)

        if win(game):
            game_won = True
            again = input("Game is over.... Do you want to Play again .....(y/n): ")
            if again.lower() == "y":
                print("Restarting")
            elif again.lower() == "n":
                print("Thanks for Playing... Byeeeee.....")
                play = False
            else:
                print(" Not a valid choice.... Closing....")
                play = False
