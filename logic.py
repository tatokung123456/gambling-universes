# random

import random

answers = ["Yes! No need to ask!", "Nah", "Meh:/", "Maybe;)", "I dont know, go ask AI"]

while True:
    question = input("Ask me!('quit' to exit): ")
    if question.lower() == 'quit':
        break
    print("I think...: ", random.choice(answers))
