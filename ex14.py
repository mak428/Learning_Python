from sys import argv

script, user_name = argv

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input()

print(f"Where do you live {user_name}?")
lives = input()


print("What kind of computer do you have?")
computer = input()

print (f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is. And you have {computer} computer. Nice.
""")
