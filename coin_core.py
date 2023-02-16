import hashlib
import calendar
import time
current_GMT = time.gmtime()
time_stamp = calendar.timegm(current_GMT)

def generate_user_identification():
    wallet_balance = 0
    username = input("Enter username: ")
    password = input("Enter password: ")
    combined_data = username + " " + password + " " + wallet_balance

    user_key = hashlib.sha256(combined_data.encode()).hexdigest()
    private_key = hashlib.sha256(time_stamp.encode()).hexdigest()

    user_key_writer = open("/user_data/user_keys.txt", "a")
    user_key_writer.write(user_key)
    private_key_writer.write("\n")
    user_key_writer.close()

    private_key_writer = open("/user_data/user_keys.txt", "a")
    private_key_writer.write(private_key)
    private_key_writer.write("\n")
    private_key_writer.close()

    print("YOUR USER KEY: ", user_key)
    print("YOUR PRIVATE KEY: ", private_key)

def update_user_identification(user_key, new_user_key, private_key):
    with open("/user_data/private_keys.txt", 'r') as priv_keys:
        with open("/user_data/user_keys.txt", r) as usr_keys:
            private_keys = priv_keys.read()
            user_keys = usr_keys.read()
            if private_key in private_keys and user_key in user_keys:
                user_keys.close()
                file = open("/user_data/user_keys.txt", "r")
                replaced_content = ""
                for line in file:
                    line = line.strip()
                    new_line = line.replace(user_key, new_user_key)
                    replaced_content = replaced_content + new_line + "\n"
                file.close()

                write_file = open("/user_data/user_keys.txt", "w")
                write_file.write(replaced_content)
                write_file.close()

def generate_new_user_key(username, password, wallet_balance):
    combined_data = username + " " + password + " " + wallet_balance
    new_user_key = hashlib.sha256(combined_data.encode()).hexdigest()
    print("NEW USER KEY:")