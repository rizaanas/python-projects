Quizz = {
    "question1": {
        "question": "What is the capital of France?",
        "answer": "paris"
    },
    "question2": {
        "question": "What is the capital of Germany?",
        "answer": "berlin"
    },
    "question3": {
        "question": "What is the capital of Italy?",
        "answer": "rome"
    },
    "question4": {
        "question": "What is the capital of Sri Lanka?",
        "answer": "colombo"
    },
}

score = 0

for key, value in Quizz.items():
    print(value['question'])
    answer = input("Answer? ")

    if answer.lower() == value['answer'].lower():
        print("Correct")
        score += 1
        print("Your score is: " + str(score))
    else:
        print("Wrong!")
        print("The answer is: " + value['answer'])
        print("Your score is: " + str(score))
    print("\n")

print("You got " + str(score) + " out of 4 questions")
print("Your percentage is " + str(int(score / 4 * 100)) + "%")



