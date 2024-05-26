print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

print("Two roads diverge into the woods. Some followed the path of safety and some took the road less taken. Left or right, which path did you take?")
path = input("Type 'left' or 'right'.\n")
path_inp = path.lower()
if path_inp == "left":
          print('''Your path has lead you to a clearing in the woods. 
There is an enchanting lake in front of you. 
The water sparkles in the sunlight. 
You can see an island in the middle of it. 
Do you dare to quench your curiosity and swim to the island or wait for a boat?''')
          lake = input("Type'swim' or 'wait'. \n")
          lake_inp = lake.lower()
          if lake_inp == "wait":
                    print('''They say patience is a virtue, and they don't say wrong.
You waited for a boat and it arrived. 
You hopped aboard, took the oars in your hand and started to row towards the island. 
You reached the island and found a cave.
You enter its dark passage and it shines with towering golden torches from within.
You see three doors. One red, one yellow, and one blue. 
Go ahead on your big adventure, fear not and chose wisely.Which door do you choose?''')
                    door = input("Type 'red', 'yellow', or 'blue'\n")
                    door_inp = door.lower()
                    if door_inp == "yellow":
                              print('''All that is yellow is not gold. Or however the saying goes...
This door is not gold but it does hold the treasure you seek. 
You open the door and find a room full of gold.
You have conquered the treasure island and found its hidden treasure.
You win!''')
                    elif door_inp == "red":
                              print('''You were saved from the water but got burned by the fire. 
The angry red flames consume you as you open the door.
Game Over.''')
                    elif door_inp == "blue":
                              print('''The 'B' in this blue door stands for 'Beware of Beasts'.
Hungry wild beasts wait in the shadows for you to enter their lair. 
You are devoured for a lunchtime snack.
Game Over.''')
                    else:
                              print('''You must persist in the face of all obstructions.
Traveller you strayed from your path.
You were distracted by the beauty of this enchanting island.
You have forgotten your mission. You are not worthy of the treasure.
Game over.''' )

          else:
                    print('''A hover of trout wait in the green dark depths of the lake. 
They are not friendly. 
They are attracted towards the disturbance in water. 
They attack the prey they can get. You were a delicious meal.
Game Over.''')
else:
          print('''You took the road less taken. And it does not lead to victory.
          You fall into a hole of regretful decisions.
          Even though it was an acoustic scream, you are not worthy of the treasure. 
          Game Over.''')
