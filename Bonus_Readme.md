Suppose you are given random multiple choice questions with the solution like:
​
1. Which of the following words contains all five vowels (a, e, i, o, u) exactly once?
   a) Exotic
   b) Aqueduct
   c) Outstanding
   d) Sequential
   [ANSWER: b]
​
2. What is the value of 2 + 2 x 2 - 2 ÷ 2?
   (a) 4
   (b) 5
   (c) 6
   (d) 7
   [ANSWER: c]
​
3. Identify the correct spelling of the word that means "a person who studies birds."
   A) Ornithologist
   B) Ornitologist
   C) Ornithollogist
   D) Ornothologist
   [ANSWER: a]
​
4. Which of the following is an example of an omnivorous animal?
   a)Lion
   b)Eagle
   c)Cow
   d)Bear
   [ANSWER: d]
​
5. How many sides does a heptagon have?
   a) 5
   b) 6
   c) 7
   d) 8
   e) 9
   [ANSWER: c]
​
6. Which planet in our solar system has the largest number of moons?
   a) Jupiter
   b) Saturn
   [ANSWER: a]
​
7. What is the chemical symbol for the element gold?
   a) Au
   b) Ag
   c) Pt
   d) Go
   [ANSWER: a]
​
8. Which of the following countries is not a member of the European Union?
   a) Germany
   b) Sweden
   c) Switzerland
   d) France
   [ANSWER: c]
​
9. Who wrote the novel "Pride and Prejudice"?
   a) Jane Austen
   b) Charlotte Brontë
   c) Emily Dickinson
   d) Virginia Woolf
   [ANSWER: a]
​
10. Which famous scientist developed the theory of general relativity?
    a) Isaac Newton
    b) Albert Einstein
    c) Nikola Tesla
    d) Marie Curie
    [ANSWER: b]
​
​
Please write a parser in Python which takes for each question:
1. the question
2. the answer
3. the solution
​
- use regex
Store the question, the answer, the solution in a list of dictionaries:
​
```python
print(multiple_choice) 
​
[
   {question: 'Which of the following words contains all five vowels (a, e, i, o, u) exactly once?',
   answers: ['Exotic',
            'Aqueduct',
            'Outstanding',
            'Sequential'],
   solution: 2 },
   ...
   ...
   ...