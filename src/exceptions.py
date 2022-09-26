import exercises
import main

if __name__ == '__main__':
    while True:
        try:
            x = main.exercise
            x = 1 / x
        except ValueError:
            print('Input must be a string')
        
        else:
            print("Else reached")
            break
        