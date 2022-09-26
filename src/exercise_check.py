import exercises

class ex_check:

    @classmethod
    def is_exercise(self, exercise):
        return exercise in exercises.exercises_all

    def valid_exercise():
        exercise = input("Did you want to add a shoulder, arm, chest, back, leg, core, corrective or cardio exercise? ")
        if exercise == "shoulder":
            return print(f"The Exercises available for this exercise are: {exercises.shoulders}")
        elif exercise == "arm":
            return print(f"The Exercises available for this exercise are: {exercises.arms}")
        elif exercise == "chest":
            return print(f"The Exercises available for this exercise are: {exercises.chest}")
        elif exercise == "back":
            return print(f"The Exercises available for this exercise are: {exercises.back}")
        elif exercise == "leg":
            return print(f"The Exercises available for this exercise are: {exercises.legs}")
        elif exercise == "core":
            return print(f"The Exercises available for this exercise are: {exercises.core}")
        elif exercise == "corrective":
            return print(f"The Exercises available for this exercise are: {exercises.corrective}")
        elif exercise == "cardio":
            return print(f"The Exercises available for this exercise are: {exercises.cardio}")
        else:
            return print("Invalid input")


        
