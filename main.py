import random
import argparse
import string


def get_inputs():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--amount", default=1, dest="amount",
                        help="The number of passwords to be generated.")
    parser.add_argument("-n", "--number", default=1, dest="number",
                        help="The amount of numbers to be contained in the password.")
    parser.add_argument("-u", "--upper-case", default=1, dest="upper_case",
                        help="The amount of capital letters to include in the password.")
    parser.add_argument("-l", "--lower-case", default=1, dest="lower_case",
                        help="The amount of lowercase letters to be included in the password.")
    parser.add_argument("-s", "--special-char", default=1, dest="special_char",
                        help="The amount of special characters to be included in the password.")
    parser.add_argument("-t", "--total-lenght", dest="total",
                        help="Password length, if used, other parameters are ignored and completely random passwords are generated.")
    parser.add_argument("-o", "--output-file", default="passwords.txt",
                        dest="passfile", help="The name of the file to save passwords.\nYou have to type the file extension!\nIf you set False, the file will not be written.")
    return parser.parse_args()


args = get_inputs()


def generate_char_list(number, upper_case, lower_case, special_char):
    number = int(number)
    upper_case = int(upper_case)
    lower_case = int(lower_case)
    special_char = int(special_char)
    char_list = []
    for i in range(number):
        char_list.append(random.choice(string.digits))
    for i in range(upper_case):
        char_list.append(random.choice(string.ascii_uppercase))
    for i in range(lower_case):
        char_list.append(random.choice(string.ascii_lowercase))
    for i in range(special_char):
        char_list.append(random.choice(string.punctuation))
    return char_list


def generate_password(char_list):
    password = "".join(str(i) for i in char_list)
    return password

def generate_passwords(amount):
    amount = int(amount)
    passwords = []
    for i in range(amount):
        if args.total:
            password = ""
            for i in range(int(args.total)):
                char_list = string.ascii_letters + string.digits + string.punctuation
                password += random.choice(char_list)
            passwords.append(password)
        else:
            char_list = generate_char_list(
                args.number, args.upper_case, args.lower_case, args.special_char)
            password = generate_password(char_list)
            passwords.append(password)
    return passwords

def generate_passwords_file(file_name,passwords):
    if file_name:
        with open(file_name,"w",encoding="utf-8") as f:
            f.write("\n".join(passwords))
    print(f"[+] Passwords saved in {file_name} file.")


passwords = generate_passwords(args.amount)
generate_passwords_file(args.passfile,passwords)