#This is an example of how to read/write a text file.
#Add this code to your VS Code, run it, and understand it
#Then, build your own code from scratch that writes and reads from a text file.

#Give your file a name. Dont forget the .txt
fileName = "test_text_file.txt"

#create a method that writes to the text file on-demand
#content is the data that will be sent to the text file
def writeToFile(content):
    try:
        with open(fileName, 'a') as file:
            #add a '\n' to the content so it prints on a new line each time
            content = content +"\n"
            #write the content to the file
            file.write(content)
            #tell the user it was sent
            print("content added!")
            #close the file
            file.close()
    #in the event the file is unreachable, go here
    except:
        print("An error has occured!")

#create a method that reads from the text file on-demand
def readFromFile():
    try:
        with open(fileName, 'r') as file:
            #get the data and store it as 'content'
            content = file.read()
            #print 'content'
            print(content)
            file.close()
    except:
        print("An error has occured!")

        
#Create a loop that allows the user to add content to the file, read content from the file,
#  or exit the program
while True:
    print("What would you like to do?")
    print("1: send data   2:read data   3:exit program")
    choice = input("->")
    if choice == "1":
        #Choice 1 writes to the file
        print("What would you like to write to file?")
        content = input("->")
        writeToFile(content)
        print("Content added to file")

    elif choice == "2":
        #choice 2 reads the content of the file
        print("Reading your text file")
        readFromFile()

    elif choice == "3":
        #choice 3 closes the program using 'break' command
        break
print("Good Bye")
