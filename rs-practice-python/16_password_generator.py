"""
---------------------------------------------------------
Exercise 16 :
---------------------------------------------------------
Write a password generator in Python. Be creative with
how you generate passwords-strong passwords have a mix
of lowercase letters, uppercase letters, numbers, and
symbols. The passwords should be random, generating a
new password every time the user asks for a new password.
Include your run-time code in a maine method.
---------------------------------------------------------
Extra :
---------------------------------------------------------
    1. Ask the user how strong they want their password
    to be. For week passwords, pick a word or two from a
    list.
---------------------------------------------------------
 """
import random

pass_combination = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

pass_length = 8

pass_output = "".join(random.sample(pass_combination, pass_length))

print(pass_output)

