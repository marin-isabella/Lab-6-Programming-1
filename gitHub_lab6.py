'''
	Author: Isabella Marin
	Lab Partner: Aadithi Arjun
	gitHub_lab6.py
	Paired-programming to learn how to use git
'''

# encode function done by author, Isabella Marin
def encode(password):
    # initialize empty string for encoded password
    encoded_password = ""
    # loop through the digits in the string password input by user
    for digit in str(password):
        new_password = int(digit) + 3               # convert characters in string password to integers & add 3 to each
        encoded_password += str(new_password)       # convert the new password back to a string and add to empty string

    return encoded_password

# decode function done by lab partner, Aadithi Arjun
def decode(password):
    decoded_password =" "
    # loop through the digits in the string password input by user
    for digit in str(password):
        new_password = int(digit) - 3               # convert characters in string password to integers & add 3 to each
        decoded_password += str(new_password)
    return decoded_password
if __name__ == '__main__':

    run = True
    while run:
        # Display menu options
        print("\nMenu")
        print(f"-" * 13)
        print("1. Encode\n2. Decode\n3. Quit")

        # Prompt user for input
        choice = int(input("\n\nPlease enter an option: "))

        # when user inputs 1 as their choice, ask them for a password to encode
        if choice == 1:
            password = input("Please enter your password to encode: ")           # password is a string
            # call the encode function with the argument, password
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")

        if choice == 2:
            # validate that there was an encoded password to display encoded and original password
            if encoded_password is not None:
                decoded_password = decode(encoded_password)
                print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")

        if choice == 3:
            break        # exits program; breaks out of loop

        # validate that user inputs correct option otherwise break out of while loop
        if choice < 1 and choice > 3:
            run = False

