
# -----------------   This is Simple Gaming Project  ---------------
 
import random

myscore = 0
compscore = 0
print("\n\t You have 5 Matches with the Computer\n")
for i in range(5):
    if(i==0):
        print(" ----------------- \tThis is your First Match.\t ----------------- \n")
    if(i==1):
        print(" ----------------- \tThis is your Second Match.\t ----------------- \n ")
    if(i==2):
        print(" ----------------- \tThis is your Third Match.\t ----------------- \n")
    if(i==3):
        print(" ----------------- \tThis is your Fourth Match.\t ----------------- \n ")
    if(i==4):
        print(" ----------------- \tThis is your Fifth Match.\t ----------------- \n")

    comp = random.choice("SWG")
    mine = input("Choose 'S' for Snake 🐍\nChoose 'W' for Water 🌊\nChoose 'G' for Gun 🔫 \n\tSo what's your choice : ")
    mine = mine.capitalize()

    if(mine != 'S' and mine != 'W' and mine != 'G'):
        print(f'\nYou Choose {mine}')
        print("Please Select Either Snake 🐍, Water 🌊 or Gun 🔫 \n\t 🙄 Means Pickup From 'S' 'W' or 'G' \n")
    else:
        def game(comp , mine):
            if(mine == comp):
                return None
            elif(comp =='S' and mine =='G'):
                return True
            elif(comp =='W' and mine =='S'):
                return True
            elif(comp =='G' and mine =='W'):
                return True
            else:
                return False

        print(f'\nYou Choose {mine} and Computer Choose {comp}')

        result = game(comp , mine)
        if result is None:
            print("\n\t 😲 Both Chooses the Same. So Match has been Tie ! \n")
            compscore += 1
            myscore += 1
        elif result is True:
            print("\n\t🎉🎊  Congrats You Won.....! 🥳 \n")
            myscore += 1
        elif result is False:
            print("\n\t Ohh No You Loose....||🥺|| \n")
            compscore += 1

print("\n  #############   Your Score is : ", myscore , "\tComouter Score is : " , compscore , "   ##################")
if(myscore==compscore):
    print("\n\tHere, The Match has been Drawn....!\nYou and Computer Both are Winner.")
elif(myscore > compscore):
    print("\n\t Finally, You are Winner of this Battle......\n")
else:
    print("\n\t Computer Won the Battle, Better Luck next time...... \n") 

