
#Adventure Game


print ("Welcome to the Adventure Game" )

name =input("What is your name ?\n")

print("Hi", name , "! Welcome to our Adventure game .\n")

proceed = input("Did you like to start the Adventure now ? (Yes/No) \n").lower()
if proceed == "yes":
    print("let's begin the Adventure", name ,"!!")

else:
    proceed == "no"
    print("come back when you are ready. ")
    quit()

q1=input("You are now have going through the main enterance of the legendary Forest. While you walking, you have arive the lonside rever.Did you want to swim across the river or turn back ? (Swim/turn)").lower()

if q1 == "swim":
    print("You have succesfully arive at the anotherside of the river!")

elif q1 == "turn":
    print("you have lost the game!!")
    quit()
else:
    print("The answered not include in the option")
    quit()

q2=input("Now, you proceed the walking untill u have arive at the end of the road.There is two way that you can go left side and the right side. which did you want to go ? (left/right)").lower()
if q2 == "right":
    print("you came to a bridge, it looks woobly,do you want to across? (yes/no)")
    q2 = input().lower()

    if q2 == "yes":
        print("the bridge have falling down and you have loose the game ")
        quit()

    elif q2 == "no":
        print("you turn back and you realise that you there is a strangers at the side of the road. did you like to asked the stranger about the direction ? (yes/no)")
        q2=input().lower()

        if q2 == "yes":
            print("the stranger give you an 1000 gold to bring back home . You won !!!")

        elif q2 =="no" :
            print("you dont have any other way except to turn back. you sangat la lemah ")

elif q2 == "left":
    print("you have found a mind field. Did you want to go through the fields ? (yes/no) ")
    q2 = input().lower()
    if q2 == "yes":
        print("you have step the landmiles and exploded . you sangat la lemah")
        quit()
    elif q2 == "no":
        print ('u have turning back and saw a stranger by the side of the road. did you like to asked the stranger about the direction ? (yes/no) ')
        q2=input().lower()
        if q2 == "yes":
            print("the stranger give you an 1000 gold to bring back home. You won Mantap!!!!")

        elif q2 == "no":
            print("you dont have any other way except to turn back. you loose")
