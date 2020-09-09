import random

#Get user input
name = input("Please enter your name : ").title().strip()
rounds = int(input("\nHello, " + name + "!\nHow many rounds would you like to play : "))

#Initializing variables
moves = ['rock', 'paper', 'scissors']
p_score = 0
c_score = 0

#Main game loop
for game_round in range(rounds):
    #Print score and get user input
    print("\nRound " + "(" + str(game_round+1) + ")")
    print(name + ": " + str(p_score) + "\t\tComputer: " + str(c_score))
   
    #Get coumputers move
    c_index = random.randint(0, 2)
    c_choice = moves[c_index]
    
    #Get users move
    p_choice = input("Time to pick...rock, paper, scissors : ").lower().strip()
    
    #If the player makes a valid move
    if p_choice in moves:
        print ("\tComputer: " + c_choice)
        print("\t" + name + ": " + p_choice)
        
        #Computer chooses rock
        if p_choice == 'rock' and c_choice == 'rock':
            winner = 'tie'
            phrase = 'It is a tie, how boring!'
        elif p_choice == 'paper' and c_choice == 'rock':
            winner = 'player'
            phrase = 'Paper covers rock!'
        elif p_choice == 'scissors' and c_choice == 'rock':
            winner = 'computer'
            phrase = 'Rock smashes scissors!'
            
        #Computer chooses paper
        elif p_choice == 'rock' and c_choice == 'paper':
            winner = 'computer'
            phrase = 'Paper covers rock!'
        elif p_choice == 'paper' and c_choice == 'paper':
            winner = 'tie'
            phrase = 'It is a tie, how boring!'
        elif p_choice == 'scissors' and c_choice == 'paper':
            winner = 'player'
            phrase = 'Scissors cut paper!'
           
        #Computer chooses scissors
        elif p_choice == 'rock' and c_choice == 'scissors':
            winner = 'player'
            phrase = 'Rock smashes scissors!'
        elif p_choice == 'paper' and c_choice == 'scissors':
            winner = 'computer'
            phrase = 'Scissors cut paper!'
        elif p_choice == 'scissors' and c_choice == 'scissors':
            winner == 'tie'
            phrase = 'It is a tie, how boring!'
        
        #Catch for any other conditions
        else:
            print("\tRound winner not calculated.")
            winner = 'tie'
            phrase = 'It is a tie, how boring!'
            
        #Display round result
        print("\t" + phrase)
        if winner == 'player':
            print("\tYou win round " + str(game_round+1) + ".")
            p_score += 1
        elif winner == 'computer':
            print("\tComputer wins round " + str(game_round+1) + ".")
            c_score += 1
        else:
            print("\tThis round was a tie.")
            
    #If player did not make a valid move
    else:
        print("That is not a valid game option!")
        print("Computer gets the point!")
        c_score += 1
        
#Game has ended, print results
print("\n\nFinal Game Results: ")
print("\tRounds Played: " + str(rounds))
print("\t" + name + "'s Score: " + str(p_score))
print("\tComputer Score: " + str(c_score))

if p_score > c_score:
    print("\tWinner: " + name + " :)")
elif p_score < c_score:
    print("\tWinner: Computer :(") 
else:
    print("\tThe game was a tie.")
