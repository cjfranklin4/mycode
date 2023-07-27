#!/usr/bin/env python3 
import requests
import html
import random

#API URL
url = 'https://opentdb.com/api.php?amount=10&category=31'

def call_api():
    res = requests.get(url).json()
    return res

def main():
    results = call_api()
    #Part 1
    #print(results)

    # Part 2, 3, and some of 4
    for result in results['results']:
        print(html.unescape(result['question']))
        
        #put answers in a list
        answers = []
        answers.append(html.unescape(result['correct_answer']))
        
        for answer in result['incorrect_answers']:
            answers.append(html.unescape(answer))
        # Randomize answers
        answers = random.sample(answers,len(answers))
        
        for answer in answers:
            print(f"- {answer}")
        print("\n")

if __name__ == "__main__":
    main()
