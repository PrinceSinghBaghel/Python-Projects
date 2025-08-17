print(''' _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
                                                                 ''')

print("*******************************************************************")

print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

choice1 = input('You\'re at a cross road. Where do you want to go?\nType "left" or "right"\n')

if choice1 == "left" or choice1 == "Left":
    choice2 = input('You\'ve come to a lake. '
                    'There is an island in the mniddle of the lake. '
                    'Type "wait" to wait for a boat. Type "swim" to swim across. ').lower()
    if choice2 == "wait" :
        choice3=input("You arrived at the island unharmed. '" \
        "'There is house with 3 doors. One red, one yellow and blue . '" \
        "'Which color do you choose ? : ").lower()
        if choice3 =="red":
            print("Its a room full of fire. Game Over")
        elif choice3=="yellow":
            print("You found the treasure. You Win !")
        elif choice3=="blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You choose a door that doesnt exist.")
    else :
        print("You got attacked by an angry trout . Game Over . ")

else :
    print("You fell in to a hole. Game Over. ")