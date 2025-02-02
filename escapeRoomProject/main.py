

def start():
    print("before we start the game, please enter your name below")
    name = input()
    print("hello, ", name)
    print("in games like these, it might be better to keep a notepad or something on you at all times in case you want to jot down any notes")
    temp = input("press Z to start game\n")
    begin()


def begin():
    print("you wake up in a dark room, you feel your way around to turn on the light.\n"
          "\"where am I? what am I doing here?\" you thought to yourself.\n"
          "You find yourself to be in some sort of medical room, on the walls you see a large dear head for some reason.\n"
          "what do you do?\n")
    options = ["look around the room", "go out into the hallway", "check your pockets"]
    choices(options)
    choice = int(input())
    if choice == 1:
        room1()


def room1():
    print("You look around the room and noted in your head what you could find\n")


def choices(array):
    for x in range(0,len(array)):
        print(" ", x+1, ": ", array[x])


def main():
    start()


main()
