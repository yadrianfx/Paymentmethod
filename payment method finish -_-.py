print("- - - - - - - - - - - ")
print("-   Payment method   -")
print("- - - - - - - - - - - ")
print("You can pay with Visa, PayPal or Paysafecard, what you prefer?:")
which =input("1- PayPal / 2- Visa / 3- Paysafecard / 4- Mastercard / 5- Bitcoin / 6- Apple Pay / 7- Exit!: ")
if which == "1":
    print("Okey, now tell me your Email and your password")
    name = input("Name (example:Juan Luis):")
    email = input("Email (example:juanluis2000@gmail.com):")
    password = input("Password (example:juanluis1234):")
    print ("Thanks for all!", name , ",",email)
    print("----------------------------------")
if which == "2":
    print("Tell me your credentials")
    titular = input("Titular name and surname (example:Juan Luis):")
    digits = input("Digits (example:1111-2222-3333-4444): ")
    cvc = input("CVC (example:123):")
    expiration = input("Data expiration (example:11/22):")
    print("Thanks for all!", titular )
    print("-------------------------")
if which == "3":
    print("Code of the Paysafecard")
    name =input("Name and surname (example:Juan Luis):")
    code = input("Digits (16 digits, example:1111-2222-3333-4444):")
    print("Thanks for all!", name)
    print("--------------------")
if which == "4":
    print("Tell me your credentials")
    titular = input("Titular name and surname (example:Juan Luis):")
    digits = input("Digits (example:1111-2222-3333-4444): ")
    cvc = input("CVC (example:123):")
    expiration = input("Data expiration (example:11/22):")
    print("Thanks for all!", titular)
    print("-------------------------")
if which =="5":
    print("Tell me your wallet ID")
    wallet = input("ID connected with metamask (example: 0xDE647F2d4E831D05c3C5FbC7E2d0ad3af2922C39): ")
    print(wallet)
    conf = input("Is this your wallet? Yes(Y) or No(N): ")
    if conf == "Y":
        print("Okey, thank you!")
    if conf == "N":
        wallet2 = input("Put it again, be careful and put it right:")
        conf2 = input("Is this your wallet? Yes(Y) or No(N): ")
    if conf2 == "Y":
        print("Okey, thank you!")
    print("-------------------------")
if which == "6":
    email = input("Email connected to Apple: ")
    id = input("Apple ID: ")
    print("-------------------------")
if which == "7":
    print("Okay, see you soon!")
    print("--------------")
print("Made by Adrián García 1BCSºC :D")



    
   
             
