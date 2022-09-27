import exercises
import exercise_check
# import exceptions
import exvalue
import pmaker
from fitness_tools.exercise.rm_estimator import RM_Estimator


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
sh_vol, ar_vol, ch_vol, ba_vol, le_vol, core_vol, corr_vol, card_vol = exvalue.Value.get_value(program)

# pmaker.Pmaker.fprog(program)
print(sh_vol)




# f = open(f'{name}.txt', "w+")
# f.write(str(program))
# f.close()




print(program)