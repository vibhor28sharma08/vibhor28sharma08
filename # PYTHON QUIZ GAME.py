# PYTHON QUIZ GAME
                                    # tuple questions
questions=("1. Who developed Python Programming Language?",
           "2. Which type of Programming does Python support?",
           "3. Which of the following is the correct extension of the Python file?",
           "4. Which keyword is used for function in Python language?",
           "5. Which of the following character is used to give single-line comments in Python?")
                                    #2d tuple options to the questions
options=(("a.Wick van Rossum","b.Rasmus Lerdorf","c.Guido van Rossum","d.Niene Stom"),
         ("a.object-oriented programming","b.structured programming","c.functional programming","d. all of the mentioned"),
         ("a. .python","b. .pl","c. .pn","d. .py"),
         ("a.def","b.fun","c.define","d.func"),
         ("a. &","b. #","c. *","d. /"))
                                    # correct answers to the questions
answers=("c","d","d","a","b")
                                    #list of guesses
guesses=[]

score= 0
question_num=0

                                    #displaying questions
for question in questions:
    print("----------------------------------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    
    guess= input("enter(a,b,c,d):")
    guesses.append(guess)
    if guess== answers[question_num]:
        print("Correct!")
        score+=1
    else:
        print("Incorrect")
    question_num+=1

    