'''
# project 1
print("welcome!")
player = input("do you want to play :" + "")

if player.lower() != "yes":
    quit()
print ("okay you just play")
'''



#project 2 
score = 0
question = input("how many days in week" + ":")
if question.lower() == "seven":
    print("correct")
    score+=1
else:
    print("incorrect")


question = input("how many hours in day" + ":")
if question.lower() == "24":
    print("correct")
    score+=1
else:
    print("incorrect")

question = input("what is your country" + ":")
if question.lower() == "srilanka":
    print("correct")
    score+=1
else:
    print("incorrect")

print("total score : " + str(score))










