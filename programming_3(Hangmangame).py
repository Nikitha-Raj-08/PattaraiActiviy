import random
def hangman():
    list_of_word = ["apple","google","tesla","amazon","techmahindra","capgemini","meta","flipkart"]
    word = random.choice(list_of_word)
    turns = 8
    guessmade = " "
    valid_entry = set("abcdefghijklmnopqrstuvwxyz")
    while len(word)>0:
        main_word = ""
        missed = 0
        for letter in word:
            if letter in guessmade:
                main_word = main_word+letter
            else:
                main_word = main_word+"_ "
        if main_word == word:
            print(main_word)
            print("Well Done",name,"You WON the game!!!!")
            break
        print("Guess the words : ",main_word)
        guess=input()
        if guess in valid_entry:
            guessmade = guessmade+guess
        else:
            print("Please,Enter a valid character...")
            guess=input()
        if guess not in word:
            turns=turns-1
            if turns==7:
                print("7 Turns left")
                print("____________________")
                print("         |          ")
            if turns==6:
                print("6 Turns left")
                print("____________________")
                print("         |          ")
                print("         O          ")
            if turns==5:
                print("5 Turns left")
                print("____________________")
                print("         |          ")
                print("        \O          ")
            if turns==4:
                print("4 Turns left")
                print("____________________")
                print("         |          ")
                print("        \O/         ")
            if turns==3:
                print("3 Turns left")
                print("____________________")
                print("         |          ")
                print("        \O/         ")
                print("         |          ")
            if turns==2:
                print("2 Turns left")
                print("____________________")
                print("         |          ")
                print("        \O/         ")
                print("         |          ")
                print("        /           ")
            if turns==1:
                print("Only 1 Turn left!!! ")
                print("Hangman on his last breath")
                print("____________________")
                print("         |          ")
                print("        \O/         ")
                print("         |          ")
                print("        / \         ")
            if turns==0:
                print("Sorry",name,",you loose")
                print("!!!YOU LET A GOOD MAN DIE!!!")
                print("____________________")
                print("         |          ")
                print("         O          ")
                print("        /|\         ")
                print("        / \         ")
                break
name=input("Enter your name:")
print("**********!!LETS PLAY HANGMAN!!**********")
print("Welcome",name,"!")
print("All the best")
print("Here the game starts")
print("Try to guess the word in less than 8 attemps......")
hangman()
