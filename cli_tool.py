import argparse

parser = argparse.ArgumentParser(description="say hello")

parser.add_argument("--username", "-u", type=str, required=True, help="Username")

parser.add_argument("--password", "-p", type=str, required=True, help="Password")

args = parser.parse_args()

username = args.username

password = args.password

print(f"username is : {username} , password is {password}")