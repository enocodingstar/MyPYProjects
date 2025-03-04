import QuizFunc



def main():
    print("Hello there! Time to show your IQ!")
    print("There are 20 questions to answer")
    print("Showcase your skills!")

    questions = QuizFunc.ReturnQuestion()
    options = ['a', 'b', 'c', 'd']
    correct = 0
    incorrect = 0

    for i, question in enumerate(questions, start=1):
        print(f"Question {i} \n {question['question']} \n a. {question['a']} \n b. {question['b']} \n c. {question['c']} \n d. {question['d']}")
        

        while True:
            answer = input("Your answer: ").strip().lower()
            if answer in options:
                break
            print("Invalid answer. Enter an answer from a-d.")

        if(answer == question['answer']):
            print("Correct!")
            correct += 1
        else:
            print("Incorrect!")
            incorrect += 1

    print(f"Quiz completed! \n Correct: {correct} \n Incorrect: {incorrect}")

            
    

    


if (__name__ == "__main__"):
    main()


        

    