#!/usr/bin/env python3

def func(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} = {value}")

func(user="morteza", password="123", role="admin")
