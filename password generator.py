#1st project in python

import random

lower = "abcdefghijklmnopqrstwxyz"

upper = "ABCDEFGHIJKLMNOPQRSTWXYZ"

symbols = "~`@#$%^&*()_+-"

all = lower + upper + symbols

length = int(input("Enter the length of the pasword: "))

password="".join(random.sample(all,length))

print("This is your password:",password)