#CS101
#Binh Mai Program 3
#Program 3
#Binh Mai
#bvmvw5@mail.umkc.edu or binhvinhmai@gmail.com
#Started: September 29, 2014
#Finished: October 2, 2014

"""
Problem:
Given a file full of madlibs (where certain parts of the sentences can be replaced to make silly sentences),
be able to create a program that can take user input from the prompts of a random sentence, and create
a whole new sentence with the user input
"""

"""
Open up Wordlibs.txt
Import a random line from the Wordlibs.txt
Go through the line and find the various prompts
You will find the various prompts based on finding the first {
The program should find the word inbetween the first { and the second }.
It should then prompt the user for the word in between those curly braces
The program will then take all of those words and combine them. 
It will then give the user the sentence with all of the user's given words
Ask the user if they want to play again
If yes, restart the program
If no, end the program
"""

title = "Welcome to Wordlibs!"
print (title)

game = True #game will be the main variable, and everything will be nested underneath it

while game == True: #so long as this conditional is true, the game will run

    try:
        wordlibs = open("wordlibs.txt", "r") #Open up text
    except FileNotFoundError: #If file can't be opened, lets user know something is wrong
        print ("The file, Wordlibs.txt, could not be opened. Please try again")

#Importing a random sentence from the module

    import random #imports random module

    wordlibs_sentence = wordlibs.readlines() #assigns new variable to the various
                                             #lines of the file
    random_sentence = random.choice(wordlibs_sentence) #brings a random sentence from file

    print ("Please enter a word for the given prompt") #telling the user the rules of the game

    index = 0 #initialize index

#Now to actually play the MadLibs game

    try:
        while index < len(random_sentence): #It's in a range loop for the counter to iterate through the loop
            if random_sentence[index] == "{": #finds the first { of a prompt
                second_index = random_sentence.find("}", index) #finds the second } of a prompt
                user_word = input("Enter a "+ (random_sentence[index+1:second_index]) + "==>")  #finds the inbetween word
                #and assigns it to a variable. 
                if user_word == "": #if they type in a blank, this prompt will force them to reenter a word
                    print ("You have to type in a word!")
                random_sentence = random_sentence.replace(random_sentence[index:second_index+1], user_word, 1)
                #creates a new variable, random_sentence, and replaces each word as it goes through the sentence
            index += 1 #adjust the counting number
    except:
        Print ("Error!") #if there's any possible errors with the loop, this will print out
            
    print(random_sentence) #creates the sentence with the user's new addition!

#Now to ask the player if they want to play again

    while True:
        restart = 0 #initialize main variable
        affirmative=("Y","YES","YE","YEAH","YEP") #possible affirmative commands
        negative = ("N","NO","NOPE","NAH") #possible negative commands
        restart = input("Would you like to play again? Type in YES/Y to play again or NO/N to quit")
        if restart.upper() in affirmative: #capitalizes the variable restart to possibly match affirmative commands
            print("Let's play again!")
            break #breaks out of this current loop and swings back up to the top
        elif restart.upper() in negative: #capitalizes the variable restart to possibly match negative commands
            print("Thanks for playing!")
            game = False #assigns False to game, so that when loop restarts, it will end the loop
            break #since game is now False, the program will be taken out of the loop and then end
        else: #loop for incorrect input
            print("Sorry I didn't understand. Type YES/Y/NO/N to decide if you want to play again or not")
            continue #brings it back to the restart loop
