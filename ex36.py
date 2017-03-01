from sys import exit

def tunnel2():
    print """The tunnel branches yet again. The left side slopes down, while
    the right side slopes up. Which way do you go?"""
    choice = raw_input("> ")
    if choice == "left":
        smalltreasure()
    elif choice == "right":
        dead("You come out on cliff full of harpy nests. The harpies kill you.")
    else:
        print "You have to choose left or right."

def smalltreasure():
    print "You see a room with a chest full of gold bars. How many do you take?"
    choice = raw_input("> " )
    try:
        how_much = int(choice)
        if how_much < 0:
            print "What, you're donating gold? Okay then!"
            exit()
        elif how_much == 0:
            print "If you're sure you don't want any, okay!"
            exit()
        elif 1 <= how_much <= 25:
            print "Okay, they're heavy but you can carry them. Good job!"
            exit()
        else:
            dead("You're too greedy, so you die in the cave.")
    except TypeError:
            dead("You have to enter a number!")

def treasure():
  print """This room is full of jewels, scrolls, a crown, and other treasure.
   What do you take?"""
  choice = raw_input("> ")
  if "crown" in choice:
      dead("The crown is cursed. You die screaming!")
  if "scrolls" in choice:
    print "Nice, you're not greedy, you win!"
    exit(0)
  else:
    dead("You greedy bastard!")


def gnolls():
  print "You see a bunch of human bones and smell something awful."
  print "Then you see what's chewing on the bones - and some bodies that aren't bones yet."
  print "Gnolls!!"
  print "What do you do?"
  gnolls_see_you = False

  while True:
      choice = raw_input("> ")

      if "run" in choice:
          dead("The gnolls swarm you and you die sreaming under their sharp teeth!")
      elif "sneak" in choice and not gnolls_see_you:
          print "The gnolls don't see or smell you. You manage to get away."
          exit()
      elif "sneak" in choice and gnolls_see_you:
          dead("The gnolls smelled you and ate you as you screamed.")
      else:
          print "What does that mean?"

def tunnel8():
    print "You find yourself outside. Do you want to start over?"
    choice = raw_input("> ")
    if "yes" in choice:
        start()
    else:
        exit(0)

def tunnel11():
    print """As you walk down the tunnel, the slope goes downhill and gets
    increasingly steep. You finally lose your step and beginning falling. You
    black out."""
    start()

def tunnel15():
    print "You see a large, purple dragon! What do you do?"
    choice = raw_input("> ")
    if "talk" or "speak" or "chat" in choice:
        print """The dragon is surprised, but pleased to receive a friendly
        visitor. She invites you to tea."""
    elif "kill" or "attack" in choice:
        print """The dragon kills you, of course. Did you really think you
        could survive a fight with a full-grown dragon?"""
    else:
        print "I don't know what you mean."

def tunnel13():
    print """You're almost done! Right or left? You feel air from the left."""
    choice = raw_input("> ")
    if "right" in choice:
        treasure()
    elif "left" in choice:
        tunnel15()
    else:
        print "You can only go left or right."

def tunnel9():
    print "There's another branching ahead. Left or right?"
    choice = raw_input("> ")
    if "right" in choice:
        tunnel13()
    elif "left" in choice:
        tunnel10()
    else:
        print "Please choose right or left."

def tunnel7():
    print """You see yet another branch. The right side goes up, and you see a
    little light ahead. The left side goes on down. Choose one."""
    choice = raw_input("> ")
    if "right" in choice:
        tunnel8()
    elif "left" in choice:
        tunnel9()
    else:
        print "Which way did you mean to go? Right or left?"

def tunnel5():
    print """This tunnel has two branches. Both slope downward. Do you go
    right or left?"""
    choice = raw_input("> ")

    if "left" in choice:
        gnolls()
    elif "right" in choice:
        tunnel7()
    else:
        print "You can only go to the left or the right."


def tunnel1():
    print "You see two branches to the tunnel, right and left. Which do you take?"
    choice = raw_input("> ")
    if choice == "left":
        tunnel2()
    elif choice == "right":
        tunnel5()
    else:
        print "I don't know what that means."



def dead(why):
  print why, "Oh well, try again!"
  exit(0)

def start():
  print "You are in a cave."
  print "There is a tunnel. Do you go through it?"

  choice = raw_input("> ")
  if choice == "yes":
      tunnel1()
  elif choice == "no":
      print "Coward."
      exit(0)
  else:
      print "I don't know what that means."

start()
