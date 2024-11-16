import subprocess

user_input = input("Enter a username: ")

subprocess.call("echo " + user_input, shell=True)
