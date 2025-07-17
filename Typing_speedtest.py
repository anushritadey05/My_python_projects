from time import *
import random as r
def mistake(partest,usertest):
    error=0
    for i in range(len(partest)):
        try:
            if partest[i]!=usertest[i]:
                error=error+1
        except:
            error=error+1
    return error

def speed_time(time_s,time_e,userinput):
    time_delay=time_e-time_s
    time_R=round(time_delay,2)
    speed=len(userinput)/time_R
    return round(speed)

test=["The quick brown fox jumps over the lazy dog, but thats just the beginning of the story. In a quiet forest, animals gather each morning to greet the sun with cheerful sounds and playful energy. Typing is a skill that improves with practice, just like playing an instrument or painting a picture. As your fingers dance across the keyboard, remember to stay focused, keep a steady pace, and enjoy the rhythm of each word forming under your touch.","I am Anushrita Dey","I am an AIML engineering student"]
test1=r.choice(test)
print("*****TYPING SPEED*****")
print(test1)
print()
print()
time_1=time()
testinput=input("Enter:")
time_2=time()

print("SPEED:",speed_time(time_1,time_2,testinput),"w/sec")
print("ERROR:",mistake(test1,testinput))