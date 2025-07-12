import random

def load_choices(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]

def random_choice(choices):
    return random.choice(choices)
