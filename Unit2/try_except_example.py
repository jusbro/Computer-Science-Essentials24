#This file will demonstrate how to prevent crashes using 'try... except...'

#For Lesson 2.6, use this code to learn how try/except works.
#Then, based on what you learned, build your own code that uses try/except
#Or, you may update old code of yours to have a try/except

while True:

    try:
        first_num = float(input("Give me a number"))
        second_num = float(input("Give me another number"))
        answer = first_num + second_num
        print(first_num ,"+",  second_num, "is", answer)
        break
    except:
        print("You did not provide numbers! Please try again!")

print("Good Bye")
