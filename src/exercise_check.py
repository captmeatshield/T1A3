import exercises

class Excheck:

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
    
    def day_volume(self):
        for k, v in self.items():
            if len(v) > 7:
                print(f"{k} has too many exercises for a day")
            elif len(v) > 1 and len(v) < 4:
                print(f"{k} has few exercises you may want to consider adding volume")
            else:
                continue
    
    def week_volume(self):
        for k, v in self.items():
            pass