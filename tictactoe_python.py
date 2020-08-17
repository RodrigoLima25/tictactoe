#Tic-Tac-Toe
#By Rodrigo Lima
#TAFE ID 20048442

#import of the modules that I am using in this application
import os
import random
import sys 

#Class Board is the only and main class, where I am using all methods I need to run this game
class Board():
    
    #using the init method to initialize the attributes of the class
    def __init__(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    #display the board, and define the position of each field according to the numeric keyboard
    def display(self):
        print("\n %s | %s | %s " %(self.cells[7], self.cells[8], self.cells[9]))
        print("-----------")
        print(" %s | %s | %s " %(self.cells[4], self.cells[5], self.cells[6]))
        print("-----------")
        print(" %s | %s | %s " %(self.cells[1], self.cells[2], self.cells[3]))

    #update cell according to the value entered by the player
    def update_cell(self, cell_index, player):

        #check if the cell is empty, if so just set a new value and return true, otherwise return false
        #the return of this method will be used in the play_game method
        if(self.cells[cell_index] == " "):
            self.cells[cell_index] = player
            result = True
        else:
            result = False

        refresh()
        return result

    #check if there is winner. The only attribute of this method is the player id (x,o)
    def is_winner(self, player):
        for combo in [[1,2,3],[4,5,6],[7,8,9],[7,4,1],[8,5,2],[9,6,3],[7,5,3],[9,5,1]]:
            result = True
            for cell_index in combo:
                if self.cells[cell_index] != player:
                    result = False

            if result == True:
                return True

        return False

    #check if there is a tie, looking if there is any empty cell and increasing 1 for each of those. When reach 9 it means the board is full and there is a tie
    def is_tie(self):
        used_cells = 0
        for cell in self.cells:
            if cell != " ":
                used_cells += 1

        if used_cells == 9:
            return True
        else:
            return False

    #manage the players turn, and call the 'update_cell' method.
    #I am doing a double check in the value entered by the player, just to make sure it is between 1 and 9.
    #if the player enter any other different character, I return a warming message and call the same method again
    def play_game(self, player):
        choice = int(input(f"\n({player} TURN) Please enter between 1 and 9: "))
        if(choice != 1 and
           choice != 2 and
           choice != 3 and
           choice != 4 and
           choice != 5 and
           choice != 6 and
           choice != 7 and
           choice != 8 and
           choice != 9):
            print("The value entered is invalid! Please try it again.")
            self.play_game(player)

        """verificar quando precisa colocar outro numero alem de 1 e 9"""

            
        #when calling the method update_cell, I check if it will return false, if so I print a message saying that the number has been already chosen, and call
        #the method play_game again, to repeat the proccess
        if not(board.update_cell(choice, player)):
            print("\nThis number has been already chosen! Enter a different one")
            self.play_game(player)

    #Check if the player intends to play again. This method accepts one attribute.
    def play_again(self, answer):

        #if the attribute is Y, I just reset the board, and execute the method refresh, otherwise I exit the application using the function exit of the module sys
        if(answer == "Y"):
            self.reset()
            refresh()
        else:
            sys.exit()

    #This function just clean the cells of the table
    def reset(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]            

#the variable board is an instance of the class Board
board = Board()

#this function is out of the class Board. This function just clear the screen and display the board
def refresh():
    #Clear the screen
    os.system("cls")

    #Display the board
    board.display()

# ==== START THE GAME ===
#all the methods were declared above. From here I start running my application.

#Ask for player 1 which they will want (X/O) and use the function upper to make sure the next IF will work correctly
choice_p1 = input(f"Player 1 would you like to be 'X' or 'O'? ").upper()

#according to the choice of the player 1, the player 2 will have the opposite value and vice versa
if(choice_p1 == "X"):
    player1 = "X"
    player2 = "O"
else:
    player1 = "O"
    player2 = "X"

#Print a message showing who is player 1 and who is player 2
print(f"\nLet's start! Player 1 is '{player1}' and Player 2 is '{player2}'")

#Display the board
board.display()

#Define who will start playing
#using the function choice of the module random, I set X and O, so the application will return randomly who is playing first
player = random.choice("XO")

#Print to the players who is playing first, player 1 or player 2
print(f"\nPlayer {player} starts the game!")
board.play_game(player)

#keep the game in looping through the while true
while True:

    #Whenever I run the code, I change the value of variable `player` and change the player's turn
    #I check if player is X and then change to O, or vice versa
    if(player == "X"):
        player = "O"
    else:
        player = "X"

    #I run the function 'play_game' and send on it the player variable value    
    board.play_game(player)

    #Adter play, I check if there is a winner for X or O, depending on who is playing
    #using the method 'is_winner', and using the player info, I return true or false for 'is_winner'
    if(board.is_winner(player)):
        print(f"\n{player} IS THE WINNER!!! CONGRATULATIONS!!!\n")

        #Ask if the player wants to play again
        answer = input("Would you like to play again (Y/N)? ")

        #calling the method 'play_again' and sending the value that was entered by the player (Y or N)
        board.play_again(answer.upper())

    #Check for a tie
    if(board.is_tie()):
        print("\nTie game!\n")
        #Ask if the player wants to play again
        answer = input("Would you like to play again (Y/N)? ")

        #calling the method 'play_again' and sending the value that was entered by the player (Y or N)
        board.play_again(answer.upper())

    
