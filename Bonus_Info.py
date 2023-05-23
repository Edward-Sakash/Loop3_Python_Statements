import re

info = """Which of the following words contains all five vowels (a, e, i, o, u) exactly once?
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
[ANSWER: b]"""

# Compile regular expressions for question, answer, and solution
pattern = r"(?s)(.+?)\n\[(?:ANSWER: ([a-d])\])"
matches = re.findall(pattern, info)

# Create a list of dictionaries containing the extracted information
questions_list = []
for question, answer in matches:
    question_dict = {
        "question": question.strip(),
        "answer": answer
    }
    questions_list.append(question_dict)

# Print the list of dictionaries
for question in questions_list:
    print("Question:", question["question"])
    print("Answer:", question["answer"])
    print()
