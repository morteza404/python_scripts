from pathlib import Path

# write file

Path("test.txt").write_text("Hello")

# read file

print(Path("test.txt").read_text())