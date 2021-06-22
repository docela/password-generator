import argparse
import random
import string


def get_length():
    parser = argparse.ArgumentParser(description='Generate a Password')
    parser.add_argument('--length', '-l', type=int, default=16, dest='length',
                        help='State the length of the password you want.')
    args = parser.parse_args()
    return args.length


def make_password(length):
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    alphabet = numbers + symbols + letters + numbers

    holder = random.sample(alphabet, k=length)

    password = "".join(holder)

    print(f"Your password is {password}")


length = get_length()

make_password(length)
