#HANGMAN

words=["raccoon","success","dizzy","follow","holler","coffee","better","tissue","address","collar","effect","feeling","hallow","mousse","missile"]

from random import randint

print("Welcome to HANGMAN")
selected_word=words[randint(0,len(words)-1)]#can also use choice method
print(selected_word)
for word in selected_word:
    print("_",end=" ")
print()
chances=6
the_list=["_"]*len(selected_word)

while chances!=0:
    if "_" not in the_list:
        print(f"You've won! \n you have got {chances} lives left")
        break
    user_value=input("Please enter your letter: ").lower()

    if user_value in selected_word:
        #the_list=["_"]*len(selected_word)
        for i in range(len(selected_word)):
            if user_value==selected_word[i] and user_value not in the_list[i]:
                the_list[i]=user_value
                #print(the_list)
            elif user_value==selected_word[i] and user_value in the_list[i]:
                chances-=1
                print(f"You guessing the same letter again try different, only {chances} lives left")
                if chances==0:
                    print("You've lost :(")
                    break
        print(f"{the_list}")
    else:
        chances-=1
        print(f"you've made a wrong Guess, only {chances} lives left")
        if chances==0:
            print("You lost :(")