import exercises
import main

while True:
    try:
        x = main.exercise
        x = 1 / x
    except ValueError:
        print('Input must be a string')
    
    else:
        print("Else reached")
        break