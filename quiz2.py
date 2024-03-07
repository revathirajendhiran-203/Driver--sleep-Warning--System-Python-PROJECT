print('Welcome to learn with esprit')


player=input('do you want to play?')

if player.lower() != "yes":
    quit()


print(' ok lets play')
score=0



question = input('How many days do we have in a week?')
if question.lower() == "seven":
    print("correct")
    score +=1

else:
    print("incorrect")

question = input('In which direction does the sun rise?')
if question.lower() == "East":
    print("correct")
    score +=1

else:
    print("incorrect")

question = input('What is your national bird?')
if question.lower() == "Peacock":
    print("correct")
    score +=1

else:
    print("incorrect")

question = input('Which is the fastest animal on the land? ')
if question.lower() == "Cheatch":
    print("correct")
    score +=1

else:
    print("incorrect")

question = input('Which is the largest ocean in the world? ')
if question.lower() == "Pacific Ocean":
    print("correct")
    score +=1

    
else:
    print("incorrect")

print("your score"+str(score))
