#Requirement
#Implement features in the software development plan you have designed. You must utilise a range of programming concepts and structures using Python such as:
# - variables and variable scope
# - loops and conditional control structures
# - write and utilise simple functions
# - error handling
# - input and output
# - importing a Python package
# - using functions from a Python package
# R12	Apply DRY (Don’t Repeat Yourself) coding principles to all code produced.
# R13	Apply all style and conventions for the programming language consistently to all code produced.
# R14	Creates an application which runs without error and has features that are consistent with the development plan.
# R15	Design TWO tests which check that the application is running as expected.

# Each test should:
# - cover a different feature of the application
# - state what is being tested
# - provide at least TWO test cases and the expected results for each test case

# > An outline of the testing procedure and cases should be included with the source code of the application
# R16	Utilise source control throughout the development of the application by:
# - making regular commits (at least 20 commits) with a commit message that summarises the changes
# - pushing all commits to a remote repository
# R17	Utilise developer tools to facilitate the execution of the application:
# For example,
# - writing a script which turns the application into an executable


import exercises

print("Hello lets start building your program")
count = 0
program = {}
for x in range(1, 3):
    program["Day {0}".format(x)] = [input("Enter a exercise or press enter for a rest day: ")]
    count = 1
    next_ex = input("Do you want to add any other exercise to your program? yes or no")
    while next_ex == 'yes':
        program["Day {0}".format(x)] = program["Day {0}".format(x)] + [input("Enter a exercise")]
        count += 1 
        next_ex = input("Do you want to add any other exercise to your program yes or no? ")
        if next_ex == 'no':
            break
    else:
        continue


print(program)