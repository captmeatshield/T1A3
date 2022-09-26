import exercises

class ex_check:

    @classmethod
    def is_exercise(self, exercise):
        return exercise in exercises.exercises_all
