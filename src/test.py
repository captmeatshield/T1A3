from fitness_tools.exercise.rm_estimator import RM_Estimator

new_reps = RM_Estimator(90.0, 4, 10)
print(new_reps.estimate_weight())

print(new_reps.__dict__)