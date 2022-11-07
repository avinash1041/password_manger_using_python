from cryptography.fernet import Fernet


# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key", "wb") as key_file:
#         key_file.write(key)

# write_key()

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key() 
fer = Fernet(key)

# key + password = text to encrypt = random text
# randorm text + key = password = text to encrypt       

def view():
    with open("password.txt", 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, pasw = data.split("|")
            print("User: ", user, "| pasw: ", 
                  fer.decrypt(pasw.encode(encoding='utf-8').decode()))
            
            
# def view():
#     with open('password.txt', 'r') as f:
#         for line in f.readlines():
#             data = line.rstrip()
#             user, passw = data.split("|")
#             print("User:", user, "| Password:",
#                   fer.decrypt(passw.encode()).decode())

def add():
    name = input("Account Name: ")
    pwd = input("Enter password: ")
    with open('password.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input("would you like to add a new passowrd or view existing one(view,add)?, press q to quit? ").lower()
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("invalid mode.")
        continue
