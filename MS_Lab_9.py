#myself: Mishka Sonavadekar, partner: Alex Kellogg

#importing Alex K.'s decode function
import AK_decode

#encode function
def encode(password):
    new_pass = ''
    if len(password) <= 8:
        for i in range(0, len(password)):
            item = str(int(password[i]) + 3)
            item = item[-1]
            new_pass += item
    return new_pass

if __name__ == "__main__":
    while True:
        print("Menu\n-------------")
        print("1. Encode\n2. Decode\n3. Quit\n")
        choice = int(input("Please enter an option: "))

        if choice == 3:
            break
        elif choice == 1:
            password = input("Please enter your password to encode: ")
            password = encode(password)
            print("Your password has been encoded and stored!\n")
        elif choice == 2:
            new_pass = AK_decode.decode(password)
            print(f"The encoded password is {password}, and the original password is {new_pass}.")
