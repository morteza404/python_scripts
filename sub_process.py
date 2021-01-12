import subprocess

# subprocess.run(["df", "-h"])
# subprocess.run(["ls", "-ltrh"])

# turn off system

# import subprocess
# subprocess.run(["shutdown", "-h", "now"])


for i in range(0,101,10):
    with open("test.txt", "a") as target:
        target.write(str(i) + "\n")

subprocess.run(["shutdown", "-h", "now"])