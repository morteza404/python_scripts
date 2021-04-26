lst = [
    "10773071083053167893", 
    "18332816095601421308",
    "16226829804004675359",
    "8465542114351460185" ,
    "13818752972373742501",
    "9557017816636751727",
    "10773071083053167893",
]
print("last digit\n")

for i in lst:
    total = int(i[-1]) 
    print(total)

print("\nsum of last 2 digits\n")

for i in lst:
    total = int(i[-2]) + int(i[-1]) 
    print(total)

print("\nsum of last 3 digits\n")

for i in lst:
    total = int(i[-3]) + int(i[-2]) + int(i[-1]) 
    print(total)

print("\nsum of last 4 digits\n")

for i in lst:
    total = int(i[-4]) + int(i[-3]) + int(i[-2]) + int(i[-1]) 
    print(total)

