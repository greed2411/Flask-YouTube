import random
import string


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    """ To generate random alphanumeric string of length 6 """
    return "".join(random.choice(chars) for _ in range(size))


if __name__ == "__main__":

    print("This script is supposed to be borrowed.")

else:

    id_generator()

