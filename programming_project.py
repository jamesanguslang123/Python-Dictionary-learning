import sys

userInput = input("Enter the diffculty of the project: Easy, Medium, Hard:  ")
program = {
    "name": "James",
    "languages": ["Python", "JavaScript", "Java", "C#", "C++"],
    "Difficulty": userInput,
    "completion": False
}

print(f"Project Name: {program['name'] }")
print(f"Difficulty: {program['Difficulty'] }")
print(f"Languages: {', '.join(program['languages']) }")
print(f"Completion Status: {'Completed' if program['completion'] else 'Not Completed'}")
