import exercises

class ex_check:

    @classmethod
    def is_exercise(self, exercise):
        return exercise in exercises.exercises_all

    def valid_exercise():
        exercise = input("Did you want to add a shoulder, arm, chest, back, leg, core, corrective or cardio exercise? ")
        if exercise == "shoulder":
            return print(f"The Exercises available for this exercise are: {exercises.shoulders}")