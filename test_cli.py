import argparse

parser = argparse.ArgumentParser(description="this is test cli tool")

parser.add_argument("--username", "-u", type=str, required=True, help="Username")

args = parser.parse_args()

username = args.username

print("correct username :)))" if username == "admin" else f"the username *{username}* is not correct !")