# Solution

import re

# Define the multiple-choice questions as a string
questions = '''
Which of the following words contains all five vowels (a, e, i, o, u) exactly once?
a) Exotic
b) Aqueduct
c) Outstanding
d) Sequential
[ANSWER: b]

What is the value of 2 + 2 x 2 - 2 ÷ 2?
(a) 4
(b) 5
(c) 6
(d) 7
[ANSWER: c]

Identify the correct spelling of the word that means "a person who studies birds."
A) Ornithologist
B) Ornitologist
C) Ornithollogist
D) Ornothologist
[ANSWER: a]

Which of the following is an example of an omnivorous animal?
a)Lion
b)Eagle
c)Cow
d)Bear
[ANSWER: d]

How many sides does a heptagon have?
a) 5
b) 6
c) 7
d) 8
e) 9
[ANSWER: c]

Which planet in our solar system has the largest number of moons?
a) Jupiter
b) Saturn
[ANSWER: a]

What is the chemical symbol for the element gold?
a) Au
b) Ag
c) Pt
d) Go
[ANSWER: a]

Which of the following countries is not a member of the European Union?
a) Germany
b) Sweden
c) Switzerland
d) France
[ANSWER: c]

Who wrote the novel "Pride and Prejudice"?
a) Jane Austen
b) Charlotte Brontë
c) Emily Dickinson
d) Virginia Woolf
[ANSWER: a]

Which famous scientist developed the theory of general relativity?
a) Isaac Newton
b) Albert Einstein
c) Nikola Tesla
d) Marie Curie
[ANSWER: b]
'''

# Define the regex patterns for extracting the question, answers, and solution
pattern_question = r"(.*?)\n"
pattern_answers = r"[a-z]\) .*?(?=\n[a-z]\)|\[ANSWER:)"
pattern_solution = r"\[ANSWER: (\w)\]"

# Compile the regex patterns
regex_question = re.compile(pattern_question)
regex_answers = re.compile(pattern_answers, re.DOTALL)
regex_solution = re.compile(pattern_solution)

# Find all matches using the compiled regex patterns
question_matches = re.findall(regex_question, questions)
answer_matches = re.findall(regex_answers, questions)
solution_matches = re.findall(regex_solution, questions)

# Create a list of dictionaries to store the question, answers, and solution
multiple_choice = []
for i in range(len(question_matches)):
    question = question_matches[i].strip()
    answers = [answer.strip() for answer in answer_matches[i].split('\n')]
    solution = ord(solution_matches[i].lower()) - ord('a')
    question_dict = {
        'question': question,
        'answers': answers,
        'solution': solution
    }
    multiple_choice.append(question_dict)

# Print the list of dictionaries
print(multiple_choice)
