"""                                      >>>>>>>>>Snake, Water and Gun Game<<<<<<<<                               """
import random
import pyttsx3
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 130)

computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice:")
youdict = {"s":1,"w":-1,"g":0}
reversedict = {1:"Snake",-1:"Water",0:"Gun"}
you = youdict[youstr]
print(f"you choose {reversedict[you]}\nComputer choose {reversedict[computer]}")

if(computer == you):
    engine.say("Its a draw!!")
    engine.runAndWait()

else:
    if(computer == -1 and you == 1): 
        engine.say("You win snake drink water!!")
        engine.runAndWait()
    elif(computer == -1 and you == 0): 
        engine.say("you loose you drown the gun in water!!")
        engine.runAndWait()

    elif(computer == 1 and you == -1): 
        engine.say("you win you gave water to snake!!")
        engine.runAndWait()

    elif(computer == 1 and you == 0): 
        engine.say("you kill the snake")
        engine.runAndWait()

    elif(computer == 0 and you == -1):
        engine.say("you loose you drown the gun")
        engine.runAndWait()

    elif(computer == 0 and you == 1):
        engine.say("ohh sit!! you loose!!")
        engine.runAndWait()

    else:
        engine.say("Something went wrong please enter valid key")
        engine.runAndWait()
