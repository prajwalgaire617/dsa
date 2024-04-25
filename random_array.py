import random


def generate_random_array(min_length, max_length, min_value, max_value):
    length = random.randint(min_length, max_length)
    
    random_array = [random.randint(min_value, max_value) for _ in range(length)]
    return random_array


