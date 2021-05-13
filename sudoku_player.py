
def print_matrix(game_matrix, grid_size):

    for i in range(0, grid_size):
        for j in range(0, grid_size):
            print(game_matrix[i][j], end = " ")
        print("")

def check_grid_for_winner(game_matrix, player_symbol, grid_size):
    #Check diagonals

    win_first_diagonal = True
    win_second_diagonal = True

    for i in range(0, grid_size):
        if(win_first_diagonal is True and game_matrix[i][i] != player_symbol):
            win_first_diagonal = False
        if(win_second_diagonal is True and game_matrix[i][grid_size - 1 - i] != player_symbol):
            win_second_diagonal = False
        if(win_first_diagonal is False and win_second_diagonal is False):
            break

    if(win_first_diagonal is True or win_second_diagonal is True):
        return True
    else:
        #Check lines
        for i in range(0, grid_size):
            win_row = True
            win_column = True
            for j in range(0, grid_size):
                if(win_row is True and game_matrix[i][j] != player_symbol):
                    win_row = False
                if(win_column is True and game_matrix[j][i] != player_symbol):
                    win_column = False
                if(win_column is False and win_row is False):
                    break
            if(win_row is True or win_column is True):
                return True

        return False


if __name__ == '__main__':
    game_matrix = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
    grid_size = len(game_matrix)
    valid_input = "123"
    player_symbol = "X"
    i = 0
    max_moves = grid_size * grid_size
    while(i < max_moves):
        print_matrix(game_matrix, grid_size)
        print("Input position for row and column:")
        x, y = input().strip().split(" ")
        if (x not in valid_input or y not in valid_input):
            print("Invalid input. Please try again")
        else:
            x = int(x) - 1
            y = int(y) - 1
            if(game_matrix[x][y] != "_"):
                print("Position is already taken. Please try again")
            else:
                if(i % 2 == 0):
                    player_symbol = "X"
                else:
                    player_symbol = "0"

                game_matrix[x][y] = player_symbol
                if(check_grid_for_winner(game_matrix, player_symbol, grid_size) is True):
                    print("Player {0} won the game".format(player_symbol))
                    break
                i += 1
    if(i == max_moves):
        print("It's a tie")