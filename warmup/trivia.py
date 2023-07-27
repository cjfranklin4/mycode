#!/usr/bin/env python3 
import requests
import html
import random

#API URL
url = 'https://opentdb.com/api.php?amount=10&category=31'

def call_api():
    res = requests.get(url).json()
    return res

def get_quiz():
    results = call_api()
    #Part 1
    question_list = []
    correct_answers = []
    answer_list = {}
    key_name = 0

    # Part 2, 3, and some of 4
    for result in results['results']:
        ques = html.unescape(result['question'])
        question_list.append(ques)

        #put answers in a list
        answers = []
        correct = html.unescape(result['correct_answer'])
        correct_answers.append(correct)
        answers.append(correct)

        for answer in result['incorrect_answers']:
            answers.append(html.unescape(answer))
        # Randomize answers
        answers = random.sample(answers,len(answers))
        answer_list.setdefault(key_name, answers)
        key_name += 1

    return question_list, answer_list, correct_answers

def main():
    questions, answers, correct = get_quiz()
    score = 0
    for index, question in enumerate(questions):
        print(question)
        for answer in answers[index]:
            print(answer)
        while True:
            your_ans = input("Your Answer:")
            your_ans.strip()
            if your_ans in answers[index]:
                print("You got it right!\n")
                score+= 1
                break
            else:
                print(f"Sorry, wrong answer. The correct answer was {correct[index]}.\n")
                break

            #print("\n")
    print(f"You got {score}/10 correct!")
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
