#Rock Paper Scissors Game

#What this code does:
#4 players input their names and then play agaisnt a computer in 3 games of rps
#Each win = 1 point and the top 2 players move to next round
#top 2 play another 3 games agaisnt computer and the player with most points win
#scissors = 1, rock = 2, paper = 3



import random


def main():
    #Inputs and creation of new dictionaries
    print("Hello players! This is an intense game of Rock Paper Scissors agaisnt the computer.")
    print("Four contestants are needed to make the game come to life.")
    p1 = input("Enter player one: ")
    p2 = input("Enter player two: ")
    p3 = input("Enter player three: ")
    p4 = input("Enter player four: ")
    print("You will each play agaisnt the computer three times and each win will equal one point.")
    print("The top two players with the most points will move onto the next round.")
    print("If there is a tie, the players that are tied will continue to play the computer until one gains a lead of one.")
    dic_players = {p1: 0, p2: 0, p3: 0, p4: 0}
    players = [p1, p2, p3, p4]
    newdict= {}
    print(players)
    print(dic_players)
    j = comp_play()

    
    for i in players:
        print("Game:", i)
        dic_players[i] = game(i, j)
    print(dic_players)
   
    winners = []
    values = []

    #filtering out the losers from the players, leaving the winners in the dictionary
    for i,n in dic_players.items():
        values.append(n)
    values.sort(reverse=True)
    print(values)
    if values[1] > values[2]:
        values.remove(values[2])
        values.remove(values[2])
    elif values[2] > values[3]:
        values.remove(values[3])


    #adding winners into two new lists (names and scores) 
    
    for n in values:
        for i,c in dic_players.items():
            if dic_players[i] == n and i not in winners:
                winners.append(i)          


   #merging the top 2 winner lists into new dictionary
    for key in winners:
        for points in values:
            newdict[key] = points
            break
    print("These are the winners of the first round! Time to see who's the champion!")
    print(newdict)
    replay= input("Are you guys ready for the next round? (Y/N)")
    game(i,j)
    

    
def comp_play():
    hand = ["Rock", "Paper", "Scissors"]
    computer = hand[random.randint(0,2)]
    return computer

#This puts both user and computer choices against each other

def game(player, computer):
    points = 0
    rounds = 0
    while rounds < 3:
        computer = comp_play()
        player = input("Rock Paper Scissors shoot!: ")
        player = player.lower()
        player = player.capitalize()
        if computer == 'Rock':
            if player == 'Scissors':
                rounds += 1
                print("loss :(")
            elif player == 'Paper':
                rounds += 1
                points += 1
                print("Win!!")
            elif player == 'Rock':
                print("Tie!")
            else:
                print("Error, try again.")
        elif computer == 'Paper':
            if player == 'Scissors':
                rounds += 1
                points += 1
                print("Win!!")
            elif player == 'Rock':
                rounds += 1
                print("loss :(")
            elif player == 'Paper':
                print("Tie!")
            else:
                print("Error, try again.")
        elif computer == 'Scissors':
            if player == 'Rock':
                rounds += 1
                points += 1
                print("Win!!")
            elif player == 'Paper':
                rounds += 1
                print("loss :(")
            elif player == 'Scissors':
                print("Tie!")
            else:
                print("Error, try again.")
    return points


    
    
def tie_breaker(player, computer):
    points = 0
    rounds = 0
    while rounds < 1:
        computer = comp_play()
        player = input("Rock Paper Scissors shoot!: ")
        player = player.lower()
        player = player.capitalize()
        if computer == 'Rock':
            if player == 'Scissors':
                rounds += 1
                print("loss :(")
            elif player == 'Paper':
                rounds += 1
                points += 1
                print("Win!!")
            elif player == 'Rock':
                print("Tie!")
            else:
                print("Error, try again.")
        elif computer == 'Paper':
            if player == 'Scissors':
                rounds += 1
                points += 1
                print("Win!!")
            elif player == 'Rock':
                rounds += 1
                print("loss :(")
            elif player == 'Paper':
                print("Tie!")
            else:
                print("Error, try again.")
        elif computer == 'Scissors':
            if player == 'Rock':
                rounds += 1
                points += 1
                print("Win!!")
            elif player == 'Paper':
                rounds += 1
                print("loss :(")
            elif player == 'Scissors':
                print("Tie!")
            else:
                print("Error, try again.")
    return points



    


main()

