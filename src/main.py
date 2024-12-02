import itertools
import math
import random

LEET_SUBSTITUTIONS = {
    'a': ['@', '4'],
    'b': ['8', '13', '|3'],
    'c': ['<', '(', '{', '['],
    'd': ['|)', '[)', '])'],
    'e': ['3', '€'],
    'f': ['|='],
    'g': ['9', '&'],
    'h': ['|-|', '#'],
    'i': ['1', '!', '|'],
    'j': ['_|', '</'],
    'k': ['|<', '|{'],
    'l': ['|', '7', '1'],
    'm': ['(V)', '/\\ /\\', '|V|', '^^'],
    'n': ['/\\/', '||', '^/'],
    'o': ['0', '()'],
    'p': ['|D', '|o', '|>'],
    'q': ['0_', '9', '(,)'],
    'r': ['|2', '12', '|?'],
    's': ['$', '5', '§'],
    't': ['7', '+', '-|-'],
    'u': ['|_|', 'µ', '()_'],
    'v': ['/', '||'],
    'w': ['//', '^/', '(n)', 'X/', 'V V'],
    'x': ['><', '%'],
    'y': ['`/', '¥', '|/'],
    'z': ['2', '7_']
}

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"
special_chars = """~!@#$%^&*()`_-+={}[]|\:;"'<>,.?/"""
random_set = letters + numbers + special_chars

def return_entropy(char):
    return len(char) * math.log2(len(set(char)))

def random_index(n):
    return random.sample([i for i in range(n)], n//2)

def return_strong_password(linuxword_ele: str, entropy: int) -> str:
    linuxword=[i for i in linuxword_ele]

    indexes = random_index(len(linuxword))

    for i in indexes:
        linuxword[i]=random.choice(LEET_SUBSTITUTIONS[linuxword[i].lower()])

    desired_password="".join(linuxword)
    while int(return_entropy(desired_password)) <= entropy:
        random_char = random.choice(random_set)
        desired_password += random_char

    print(f"Original Linuxword: {linuxword_ele} | Password: {desired_password} | Entropy: {return_entropy(desired_password)}")   
     
    return desired_password

def read_input(input_file):
    with open(input_file, "r") as words_file:
        return [line.strip() for line in words_file]

def write_output(output_file, passwords):
    with open(output_file, "w") as file:
        for password in passwords:
            file.write(password + '\n')

def main(input_file, output_file, entropy):
    passwords = read_input(input_file)
    improved_passwords = [return_strong_password(password, entropy=entropy) for password in passwords]
    write_output(output_file, improved_passwords)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: python main.py <input_file> <output_file> [<entropy(int)>]")
    else:
        entropy = int(sys.argv[3]) if len(sys.argv) > 3 else 60
        main(sys.argv[1], sys.argv[2], entropy)

