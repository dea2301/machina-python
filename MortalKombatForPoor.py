# Mortal_Kobat_for_poor.py is a simple game that allows two players to play against each other.
# There are three inputs for each player: name, heath of the player and the damage that the player can inflict.
# The game will continue until one of the players health is equal to 0.
# The game will display the winner and the loser.

print ("Welcome to Mortal Kombat for Poor")
print ("This is a simple game that allows two players to play against each other.")
print ("There are three mandatory inputs for each player: name, health of the player and the damage that the player can inflict.")

#PLAYER1


while True:
    player1_name = input ("Player 1, please enter your name: ").strip()
    if player1_name: 
        break
    
       
while True:
    player1_health = input("Player 1, please enter health in HP, enter number between 1-10: ")
    if ' ' in player1_health:
        number, unit = player1_health.split()
        if number.isdigit() and unit == "HP":
            number = int(number)
            if 1 <= number <= 10:
                player1_health = number
                break
    print ("Invalid value! Please enter a number between 1 and 10 folowing HP!")
  
    
while True:
    player1_damage = input ("Player 1, please enter damage, enter number between 1-3: ")
    if player1_damage.isdigit ():
         player1_damage = int(player1_damage)
         if 1 <= player1_damage <= 3:
            break
    print ("Invalid value! Please enter a number between 1 and 3!")
    
#PLAYER2
 

while True:
    player2_name = input("Player 2, please enter your name: ").strip()
    if player2_name and player2_name != player1_name:
        break
    print ("Invalid value! Please enter a name different from Player 1!")
       
while True:
    player2_health = input("Player 2, please enter health in HP, enter number between 1-10: ")
    
    if ' ' in player2_health:
        number, unit = player2_health.split()
        if number.isdigit() and unit == "HP":
            number = int(number)
            if 1 <= number <= 10:
                player2_health = number
                break 
    

while True:
    player2_damage = input ("Player 2, please enter damage, enter number between 1-3: ")
    if player2_damage.isdigit ():
         player2_damage = int(player2_damage)
         if 1 <= player2_damage <= 3:
            break
    print ("Invalid value! Please enter a number between 1 and 3!")



# GAME STARTED


round_number = 0

while player1_health > 0 and player2_health > 0:
    round_number += 1
    print (f"Starting round, {round_number}.") 

#PLAYER1 ATTACKS PLAYER2
 
    player2_health = player2_health - player1_damage
    print (f"{player2_name} hits {player1_name}!")  
    if player2_health <= 0:
        print(f"Game over! {player1_name} wins! {player2_name} is dead!")
        break

#PLAYER2 ATTACKS PLAYER1 
 
    player1_health = player1_health - player2_damage
    print (f"{player2_name} hits {player1_name}!")
    if player1_health <= 0:
        print(f"Game over! {player2_name} wins! {player1_name} is dead!")
        break
    
    

