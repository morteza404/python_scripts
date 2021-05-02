#!/usr/bin/env python3

def switch(num):
    return {
             1 : "shanbeh",
             2 : "yekshanbeh",
             3 : "doshanbeh",
             4 : "seshanbeh",
             5 : "charshanbeh",
             6 : "panshanbeh",
             7 : "jomeh"
    }.get(num,f"the {num} dosnt exist.")

print(switch(6))