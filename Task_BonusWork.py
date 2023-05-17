"""def answer_multiple_choice_questions(questions):
    for i, question in enumerate(questions):
        print(f"Question {i}: {question['question']}")
        
        for j, answer in enumerate(question['answers']):
            print(f"{chr(ord('a')+j)}) {answer}")
        
        user_choice = input("Enter your choice (a, b, c, d, etc.): ").lower()
        user_choice_index = ord(user_choice) - ord('a')
        
        if user_choice_index == question['solution']:
            print("Correct answer!")
        else:
            print(f"Incorrect answer. The correct answer is: {chr(ord('a')+question['solution'])}")
        
        print()

# Example usage
questions = [
    {
        'question': 'Which of the following words contains all five vowels (a, e, i, o, u) exactly once?',
        'answers': ['Exotic', 'Aqueduct', 'Outstanding', 'Sequential'],
        'solution': 1
    },
    {
        'question': 'What is the value of 2 + 2 x 2 - 2 ÷ 2?',
        'answers': ['4', '5', '6', '7'],
        'solution': 2
    }
]

answer_multiple_choice_questions(questions)"""

#################### Solution ##########################
def answer_multiple_choice_questions(questions):
    for i, question in enumerate(questions):
        print(f"Question {i+1}: {question['question']}")
        
        for j, answer in enumerate(question['answers']):
            print(f"{chr(ord('a')+j)}) {answer}")
        
        user_choice = input("Enter your choice (a, b, c, d, etc.): ").lower()
        user_choice_index = ord(user_choice) - ord('a')
        
        if user_choice_index == question['solution']:
            print("Correct answer!")
        else:
            print(f"Incorrect answer. The correct answer is: {chr(ord('a')+question['solution'])}")
        
        print()

questions = [
    {
        'question': 'Which of the following words contains all five vowels (a, e, i, o, u) exactly once?',
        'answers': ['Exotic', 'Aqueduct', 'Outstanding', 'Sequential'],
        'solution': 1
    },
    {
        'question': 'What is the value of 2 + 2 x 2 - 2 ÷ 2?',
        'answers': ['4', '5', '6', '7'],
        'solution': 2
    },
    {
        'question': 'Identify the correct spelling of the word that means "a person who studies birds."',
        'answers': ['Ornithologist', 'Ornitologist', 'Ornithollogist', 'Ornothologist'],
        'solution': 0
    },
    {
        'question': 'Which of the following is an example of an omnivorous animal?',
        'answers': ['Lion', 'Eagle', 'Cow', 'Bear'],
        'solution': 3
    },
    {
        'question': 'How many sides does a heptagon have?',
        'answers': ['5', '6', '7', '8', '9'],
        'solution': 2
    },
    {
        'question': 'Which planet in our solar system has the largest number of moons?',
        'answers': ['Jupiter', 'Saturn'],
        'solution': 0
    },
    {
        'question': 'What is the chemical symbol for the element gold?',
        'answers': ['Au', 'Ag', 'Pt', 'Go'],
        'solution': 0
    },
    {
        'question': 'Which of the following countries is not a member of the European Union?',
        'answers': ['Germany', 'Sweden', 'Switzerland', 'France'],
        'solution': 2
    },
    {
        'question': 'Who wrote the novel "Pride and Prejudice"?',
        'answers': ['Jane Austen', 'Charlotte Brontë', 'Emily Dickinson', 'Virginia Woolf'],
        'solution': 0
    },
    {
        'question': 'Which famous scientist developed the theory of general relativity?',
        'answers': ['Isaac Newton', 'Albert Einstein', 'Nikola Tesla', 'Marie Curie'],
        'solution': 1
    }
]

answer_multiple_choice_questions(questions)

