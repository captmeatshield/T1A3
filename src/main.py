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
import exercise_check
# import exceptions
import exvalue
import pmaker

print("Hello lets start building your program")
# name = input("What is your name? ")
program = {}
for x in range(1, 3):
    exercise = input(f"Enter a exercise for Day {x} or press enter for a rest day: ")
    if exercise_check.Excheck.is_exercise(exercise) == True:
        program["Day {0}".format(x)] = [exercise]
    elif exercise == "":
        program["Day {0}".format(x)] = ["Rest"]
        print(f"Day {x} is a rest day.")
        continue
    else:
        print(f"{exercise} is not a valid exercise")
        program["Day {0}".format(x)] = []
    next_ex = input("Do you want to add any other exercise to your program? yes or no? ")
    while next_ex != 'no':
        exercise = input("Enter a exercise or type 'no' to finish: ")
        if exercise_check.Excheck.is_exercise(exercise) == True:
            program["Day {0}".format(x)] = program["Day {0}".format(x)] + [exercise]
        elif exercise == 'no':
            break
        else:
            print(f"{exercise} is not a valid exercise")
            exercise_check.Excheck.valid_exercise()
        if next_ex == 'no':
            break
    else:
        continue

# exercise_check.Excheck.day_volume(program)
sh_vol, ar_vol, ch_vol, ba_vol, le_vol, co_vol, corr_vol, ca_vol = exvalue.Value.get_value(program)

# pmaker.Pmaker.fprog(program)
print(sh_vol)




# f = open(f'{name}.txt', "w+")
# f.write(str(program))
# f.close()




print(program)