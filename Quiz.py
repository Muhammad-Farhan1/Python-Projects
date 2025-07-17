questions = ("What is the capital of France?:",
             "How many days are there in a week?:",
             "What color is a ripe banana?:",
             "Which planet is known as the 'Red Planet'?:",
             "What is 5 + 7?:")

options = (("A. London", "B. Berlin", "C. Paris", "D. Rome"),
           ("A. 4", "B. 5", "C. 6", "D. 7"),
           ("A. Red", "B. Orange", "C. Yellow", "D. Green"),
           ("A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"),
           ("A. 10", "B. 11", "C. 12", "D. 14"))

answers = ("C", "D", "C", "B", "C")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------")
    print(question)
    for option in options[question_num]: 
        print(option)
    
    guess = input("Enter your answer (A, B, C, or D): ").upper()
    guesses.append(guess)
    
    if guess == answers[question_num]:
        print("Hurrah! Correct")
        score += 1
    else:
        print("OH! incorrect")
        print(f"{answers[question_num]} is the correct answer")

    question_num += 1

print("------------")   
print("---Answers---")   
print("------------")   

print("Answer:" , end=" ")
for answer in answers :
    print(answer  , end=" ")
print()
print("Guess:" , end=" ")
for guess in guesses:
    print(guess , end=" ")
print()

score = int(score / len(questions) * 100)
print(f"The total score is : {score}%")