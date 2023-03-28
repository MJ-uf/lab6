#Michael Jovovich
def encoder(password):
    new_pass = ""
    for i in password:
        new_pass = new_pass + str((int(i) + 3) % 10)
    return new_pass
# def decoder(password):
#     new_pass = ""
#     for i in password:
#         new_pass = new_pass + str((int(i) - 3) % 10)
#     return new_pass

def main():
    cont = True
    while cont == True:
        print("""
Menu
-------------
1. Encode
2. Decode
3. Quit
""")
        menu_option = input("Please enter an option: ")
        if menu_option == "1":
            subject = input("Please enter your password to encode: ")
            encoded = encoder(subject)
            print(encoded)
        # elif menu_option == "2":
        #     print("The encoded password is " + encoded + ", and the original password is " + decoder(encoded) + ".")
        # elif menu_option == "3":
        #     break



main()

