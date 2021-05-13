
def print_matrix(game_matrix, grid_size):

    for i in range(0, grid_size):
        for j in range(0, grid_size):
            print(game_matrix[i][j], end = " ")
        print("")

def check_grid_for_winner(game_matrix, grid_size):
    #Check diagonals

    win_first_diagonal = game_matrix[0][0]
    win_second_diagonal = game_matrix[0][grid_size - 1]

    for i in range(1, grid_size):
        if(win_first_diagonal != "_" and game_matrix[i][i] != win_first_diagonal):
            win_first_diagonal = "_"
        if(win_second_diagonal != "_" and game_matrix[i][grid_size - 1 - i] != win_second_diagonal):
            win_second_diagonal = "_"
        if(win_first_diagonal == "_" and win_second_diagonal == "_"):
            break

    if(win_first_diagonal in "X0"):
        return win_first_diagonal
    elif(win_second_diagonal in "X0"):
        return win_second_diagonal
    else:
        #Check lines
        for i in range(0, grid_size):
            win_row = game_matrix[i][0]
            win_column = game_matrix[0][i]
            for j in range(1, grid_size):
                if(win_row != "_" and game_matrix[i][j] != win_row):
                    win_row = "_"
                if(win_column != "_" and game_matrix[j][i] != win_column):
                    win_column = "_"
                if(win_column == "_" and win_row == "_"):
                    break
            if(win_row in "X0"):
                return win_row
            elif(win_column in "X0"):
                return win_column

        return "T"

def imax(game_matrix, nr_of_moves, grid_size):

    game_result = check_grid_for_winner(game_matrix, grid_size)
    if(game_result == "X"):
        return -1000 + nr_of_moves, -1, -1
    if(game_result == "0"):
        return 1000 - nr_of_moves, -1, -1
    if (nr_of_moves == grid_size * grid_size):
        return 0, -1, -1

    best_score = -1000
    x, y = -1, -1
    for i in range(0, grid_size):
        for j in range(0, grid_size):
            if(game_matrix[i][j] == "_"):
                game_matrix[i][j] = "0"
                score, _, _ = imin(game_matrix, nr_of_moves + 1, grid_size)
                game_matrix[i][j] = "_"
                if(score > best_score):
                    best_score = score
                    x = i
                    y = j
    return best_score, x, y

def imin(game_matrix, nr_of_moves, grid_size):

    game_result = check_grid_for_winner(game_matrix, grid_size)
    if (game_result == "X"):
        return -1000 + nr_of_moves, -1, -1
    if (game_result == "0"):
        return 1000 - nr_of_moves, -1, -1
    if(nr_of_moves == grid_size * grid_size):
        return 0, -1, -1

    best_score = 1000
    x, y = -1, -1
    for i in range(0, grid_size):
        for j in range(0, grid_size):
            if (game_matrix[i][j] == "_"):
                game_matrix[i][j] = "X"
                score, _, _ = imax(game_matrix, nr_of_moves + 1, grid_size)
                game_matrix[i][j] = "_"
                if (score < best_score):
                    best_score = score
                    x = i
                    y = j
    return best_score, x, y


if __name__ == '__main__':
    game_matrix = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
    grid_size = len(game_matrix)
    valid_input = "123"
    player_symbol = "X"
    i = 0
    max_moves = grid_size * grid_size

    while(i < max_moves):
        print_matrix(game_matrix, grid_size)
        if(i % 2 == 0):
            print("Input position for row and column:")
            x, y = input().strip().split(" ")
            if (x not in valid_input or y not in valid_input):
                print("Invalid input. Please try again")
                continue
            else:
                x = int(x) - 1
                y = int(y) - 1
                if(game_matrix[x][y] != "_"):
                    print("Position is already taken. Please try again")
                    continue
                else:
                    player_symbol = "X"
        else:
            player_symbol = "0"
            _, x, y = imax(game_matrix, i, grid_size)
            print("Bot has played on ({0}, {1})".format(x, y))
        game_matrix[x][y] = player_symbol
        if(check_grid_for_winner(game_matrix, grid_size) != "T"):
            print("Player {0} won the game".format(player_symbol))
            break
        i += 1

    if(i == max_moves):
        print("It's a tie")