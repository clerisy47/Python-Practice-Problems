import random

c=0
c1=1000000

for i in range(0, c1):
    choiceAI = random.randint(1, 3)
    choiceUser = random.randint(1, 3)
    for i in range(1, 4):
        if(i not in [choiceAI, choiceUser]):
            wrongChoice = i
            break
    for i in range(1, 4):
        if(i not in [wrongChoice, choiceUser]):
            choiceUser = i
            break
    if(choiceUser==choiceAI):
        c+=1

print(c/c1)