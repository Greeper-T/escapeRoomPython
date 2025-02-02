import random
import time


current = time.ctime()
end = time.ctime()
firstHallway = True
firstRoom1 = True
newRoom1 = False
UV = False
hammer = False
currentRoom = 0
roomDead = 0
eyeColor = ["green", "pink", "orange", "black", "brown", "yellow", "red", "purple"]
randoEye = random.randrange(0,len(eyeColor))
hour = random.randrange(1, 13)
minute = random.randrange(10, 60)
clockTime = str(hour) + str(minute)
int(clockTime)


def startOfGame():
    global name, clockTime
    print("before we start the game please input your name below")
    name = input()
    print("welcome,", name,"\n")
    mainRoom()


def mainRoom():
    global firstRoom1, currentRoom, UV, hammer, roomDead
    currentRoom = 1
    if firstRoom1:
        input("press Z to start game\n")
        divider()
        print("\nyou wake up in a dark room, you can't really see much, you feel around the room for a light switch and turn it on\n"
            "you find yourself in some kind of a medical room, this place feels oddly familiar... as if you've been here many times before, you don't remember much though\n"
            "your head starts to feel fuzzy, what do you do?\n")
        firstRoom1 = False
    divider()
    print("you are in the same room you started in")
    options = ["look around the room", "check your pockets", "exit the room to find you where you are"]
    choices(options)
    choice = (input().lower()).strip()
    if choice == "1":
        room1()
    if choice == "2":
        pokets()
    if choice == "3":
        hallway()
    if choice == "uv" and UV:
        print("you used the uv light but nothing showed up")
        mainRoom()
    if choice == "ham" and hammer:
        "you used the slegehammer to destroy the room"
        roomDead += 1
    mainRoom()


def pokets():
    global name, currentRoom
    divider()
    print("\nyou look inside your pockets to see if you can find anything useful\n"
          "inside your pocket you find an id card, the id card contains your name,", name.upper(), "and a embarrassing picture of yourself\n")
    if currentRoom == 1:
        mainRoom()
    if currentRoom == 2:
        room2()
    if currentRoom == 3:
        room3()
    if currentRoom == 4:
        room4()
    if currentRoom == 5:
        room5()
    if currentRoom == 10:
        storage()
    if currentRoom == 0:
        hallway()


def room1():
    global hour, minute
    divider()
    print("\nyou looks around the room to see if you can find anything\n"
          "it looks like a pretty normal room exept you spotted a deer head on the wall and wonder why that is there.\n"
          "you look at the clock and the time is", hour, ":", minute, "it looks like the clock is broken"
          "\nyour start having a headache so you search the drawer for advil, inside the drawer you find the advil you were looking for, a pen and what seems to be a journal\n"
          "do you want to read it?")
    choice = input().lower()
    if choice == "yes":
        journal()
    else:
        mainRoom()


def hallway():
    global currentRoom, UV, roomDead, hammer
    currentRoom = 0
    divider()
    print("\nyou go outside the room and find yourself in a hallway, you spot a room on the right which looks like a triangular room, the left room looks circular and one in front that looks like a storage room.\n"
          "where should you go?\n")
    options = ["circular room", "storage room", "triangular room", "medical room"]
    choices(options)
    choice = (input().lower()).strip()
    if choice == "1":
        room3()
    elif choice == "2":
        storage()
    elif choice == "3":
        room2()
    elif choice == "4":
        mainRoom()
    elif UV:
        if choice == "uv":
            print("you used the uv light but nothing showed up")
    elif choice == "ham":
        "you used the slegehammer to destroy the room"
        roomDead += 1
    hallway()


map = False


def storage():
    global currentRoom, map, UV, hammer, roomDead
    currentRoom = 10
    divider()
    print("you walk into the room in front of you\n"
          "it looks like some kind of a storage room\n"
          "you see one of those dance machines in it\n"
          "what do you do?\n")
    options = ["go back to hallway", "use dance machine and start rocking the floor"]
    choices(options)
    choice = (input().lower()).strip()
    if choice == "1":
        hallway()
    if choice == "2":
        print("chose the buttons to press\"up down left right\" below")
        answer = (input().lower()).strip()
        print(answer)
        if answer == "up up down down left right left right":
            print("after entering the gamer code, the dance machine opens up and you see a map\n"
                  "on the map you see 2 triangle room 4 normal rooms and 1 circle room")
            map = True
        else:
            print("you just rocked the dance floor and feel a little better now")
        storage()
    if UV:
        if choice == "uv" and map:
            print("you use the uv light on the map and see that there is some kind of a secret room in the room that was locked")
        elif choice == "uv":
            print("you used the uv light and found nothing")
    if choice == "ham" and hammer:
        "you used the slegehammer to destroy the room"
        roomDead += 1
    storage()


def room2():
    global currentRoom, UV, roomDead, hammer
    currentRoom = 2
    divider()
    print("you are in a triangular room\n"
          "you see a door next to the door you came from\n"
          "what do you do?")
    options = ["look around the room", "check your pockets", "go back to hallway", "go to the room to the right"]
    choices(options)
    choice = (input().lower()).strip()
    if choice == "1":
        print("you look around the room\n"
              "you find it very strange that you are in some kind of triangular room\n"
              "you check the clock on this room but it's still", hour, ":", minute, "the clock apears to be broken in here as well\n"
              "you see a large safe on the floor, it's a 3 combination safe, above the numbers are shapes in this order: circle, rectangle, triangle\n")
        a = input("try and unlock the safe?\n").lower()
        if a == "yes":
            room2Safe()
        else:
            room2()
    if choice == "2":
        pokets()
    if choice == "3":
        hallway()
    if choice == "4":
        room4()
    if UV:
        if choice == "uv":
            print("you used the uv light but nothing showed up")
            room2()
    if choice == "ham" and hammer:
        "you used the slegehammer to destroy the room"
        roomDead += 1
    room2()


def room2Safe():
    global hammer
    print("please enter passcode below")
    answer = int(input())
    if answer == 142:
        print("you opened the safe and aquired a slegehammer! next to it you also spot a rabbits foot but you think nothing of it\n"
              "to use slgehammer, just type ham to use it")
        hammer = True
    else:
        print("the number you inputted was wrong...")
        room2()


def room3():
    global newRoom1, eyeColor, randoEye, currentRoom, UV, roomDead, hammer
    currentRoom = 3
    divider()
    print("you are in a circular room\n"
          "you see a door next to the one you came from\n"
          "what do you do?")
    options = ["look around the room", "check your pockets", "go to hallway", "go to room on the other side"]
    choices(options)
    if newRoom1:
        print(" 5 : go into the locked room")
    choice = (input().lower()).strip()
    if choice == "1":
        print("you look around the room\n"
              "you find it strange that you are in a circular room\n"
              "on one of the tables you see a glass vile with a", eyeColor[randoEye], "colored eye in it")
        if not newRoom1:
            print("at the other side of the room you find a door that looks to be locked by a kaypad\n"
                  "it apears to be a 4 digit number pad\n")
            print("would you like to try and solve it?")
            choice = input().lower()
            if choice == "yes":
                lockForCircleRoom()
            else:
                room3()
    elif choice == "2":
        pokets()
    elif choice == "3":
        hallway()
    elif choice == "4":
        room4()
    elif choice == "5":
        room5()
    if UV:
        if choice == "uv":
            print("you used the uv light but nothing showed up")
            room3()
    if choice == "ham" and hammer:
        "you used the slegehammer to destroy the room"
        roomDead += 1
    room3()


def lockForCircleRoom():
    global newRoom1, clockTime
    print("please enter the passcode below")
    answer = int(input())
    if answer == 3469:
        print("after inputting those numbers, you heard a click and the door was unlocked")
        newRoom1 = True
        room3()
    else:
        print("there was a red beep, you got the passcode wrong")
        room3()


def room4():
    global UV, currentRoom, hammer, roomDead
    currentRoom = 4
    divider()
    print("you enter the room\n"
          "what do you do?\n")
    options = ["look around the room", "check your pockets", "go to triangle room", "go to circle room"]
    choices(options)
    choice = (input().lower()).strip()
    if choice == "1":
        print("unlike the other rooms, this room also seems pretty normal\n"
              "there was a window in this room, you look through it and find another room on the other side\n"
              "inside that room you found a monkeys paw in it\n"
              "\"that room is proboly cursed\" you thought to yourself\n"
              "you spotted a safe that has a", len(clockTime), "digit passcode\n"
              "try to solve it?")
        answer = input().lower()
        if answer == "yes":
            number = input("please put your answer below\n")
            if number == clockTime:
                print("you open the safe and inside you find a uv light, next to it you also find a turtle shell\n"
                      "congragulations! you have aquired a uv light, you can use it in any room, in order to use it just type uv as your answer and that uses it")
                UV = True
            else:
                print("you enter the numbers but nothing happened... you probely typed the wrong passcode")
        else:
            room4()
    elif choice == "2":
        pokets()
    elif choice == "3":
        room2()
    elif choice == "4":
        room3()
    if UV:
        if choice == "uv":
            print("you used the uv light\n"
                  "on the walls it said\"HAHAHAHA YOU THOUGHT\"")
            room4()
    if choice == "ham" and hammer:
        "you used the slegehammer to destroy the room"
        roomDead += 1
    room4()


def room5():
    global UV, hammer, roomDead, currentRoom
    currentRoom = 5
    divider()
    print("you enter the locked room\n"
          "what do you do?")
    options = ["look around", "check your pockets"]
    choices(options)
    choice = (input().lower()).strip()
    if choice == "1":
        print("you find yourself in another triangular room\n"
              "inside the room you find a very nice suit, but that's about it")
    if choice == "2":
        pokets()
    if choice == "uv" and UV:
        print("you use the uv light but find nothing")
    if choice == "ham" and hammer:
        "you used the slegehammer to destroy the room\n" \
        "when you destoryed this room, a wall opened up to reveal another room\n" \
        "you go inside"
        roomDead += 1
        finalRoom()
    room5()


def finalRoom():
    global eyeColor, randoEye
    divider()
    print("you enter the room that just opened up\n"
          "the moment you step foot in that the the wall filled in itself, your now trapped in this room\n"
          "in front of you you find a computer, so you booted up the computer\n"
          "once it booted up it read\"congrats on making it this far... now lets see how good your momory is\"\n"
          "please type in what kind of head was in the first room?")
    answer = input().lower()
    if answer == "deer":
        print("correct\n"
              "now, enter the hand?")
        answer = input().lower()
        if answer == "monkey":
            print("correct\n"
                  "now, enter the foot?")
            answer = input().lower()
            if answer == "rabbit":
                print("correct\n"
                      "now, enter the eye color?")
                answer = input().lower()
                if answer == eyeColor[randoEye]:
                    print("correct\n"
                          "now, what is the body?")
                    answer = input().lower()
                    if answer == "turtle":
                        print("correct\n"
                              "what cloths?")
                        answer = input().lower()
                        if answer == "suit":
                            goodEnd()
    elif answer == "ham":
        print("you used the hammer to destroy the computer")
        badEnd()
    elif answer == "uv":
        print("you used the uv light but nothing happened")
    else:
        finalRoom()


def badEnd():
    global current, end, name
    print("you then promply black out\n"
          "you wake up in the same room that you started in\n"
          "but this time you found yourself hooked up to some kind of machine\n"
          "you suddenly remember why you were there\n")
    time.sleep(1)
    print("what have you done", name, "!")
    print("you... you destroid it... the doctor said as he walked in\n"
          "you broke the simulation...\n\n"
          "bad end")
    print("you started the game at:", current)
    print("ended the game at:", end)


def goodEnd():
    global current, end, name
    end = time.ctime()
    print("congragualations,", name, "you have passed!\n"
          "you then promply black out\n"
          "you wake up in the same room that you started in\n"
          "but this time you found yourself hooked up to some kind of machine\n"
          "you suddenly remember why you were there\n")
    time.sleep(1)
    print("suddenly, a doctor walks in the room\n"
          "\"congragulations! you have finished the escape room demo!\""
          "thats right, you were hooked up to the brand now escape room technology that simulates an escape room\n"
          "once you enter the place, you lose momory of why you were there so its more immersive\n"
          "\nyou got the good ending...")
    print("you started the game at:", current)
    print("ended the game at:", end)


def journal():
    global UV
    divider()
    print("\nyou open the journal and start reading it\n\n"
          "\"After I woke up this morning, I made the regrettable decision of waking up. I tried to go back to sleep, but I could not even relax.\n"
          "Today was one of those days where either I get up, or I get up. I then decided to go outside, but because it was raining, I got wet.\n"
          "I went back inside, felt tired enough to go back to bed, but I still had to change out of my wet clothes. Then I got a phone call from you know who.\n"
          "I got so excited that I didn’t care that I was naked, tired, and there was a puddle on the floor. We are going on a date this Friday.\n"
          "I don’t know how I’m going to sleep. What am I going to wear? :naked dance: :singing in the rain: oh diary,\n"
          "one day I’ll look back on this and say remember when I didn’t pay attention to anything but the phone ringing. FINALLY.\"\n"
          "\n that was random... you thought to yourself")
    if UV:
        answer = input("use uv light on journal?").lower()
        if answer == "yes":
            print("after using the uv light on the journal, the letters t h r e e  f o u r  s i x  n i n e was highlitted")
    mainRoom()


def divider():
    print("----------------------------------------------------------------------------------")


def choices(a):
    for i in range(0,len(a)):
        print(" ", i+1, ": ", a[i])


def main():
    startOfGame()


main()
