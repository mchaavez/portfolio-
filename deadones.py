gameOn = True

while gameOn:
    print("get supplies")

    print("You're now in the middle of the zombie apocalypse. There is a bang at your door. You can either ignore or open the door.")


    action = input("type 'ignore' or 'open the door'")
    if action == "ignore":
        print("you lose one of your greates allies")
    if action == "open the door":
        print("If you open door a zombie will appear and it'll eat you alive")

        print("now you need to decide between ordering pizza or staying hungry")

    user_input = input("order pizza or stay hungry")
    if user_input == "order pizza":
        print("zombies delivers your pizza and you die")
    if user_input == "stay hungry":
        print("you starve and die")

    print("game over you died!")
    print("Do you want to keep playing")
    user_input = input("type yes or no.")
    if user_input == "yes":
        gameOn = True
    if user_input == "no":
        gameOn = False

print("Game over.")
