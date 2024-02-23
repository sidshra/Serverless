import random

def random_fruit():
    fruits = ["orange","apple","kiwi","grapes","banana","pineapple","jackfruit"]
    return random.choice(fruits)

if __name__ == "__main__":
    print(f"You should eat some {random_fruit()}")