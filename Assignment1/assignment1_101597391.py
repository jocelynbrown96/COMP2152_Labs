# COMP2152 Open Source Development Assignment 1: Sunday February 8th, 2026
# Jocelyn Brown, Student Number: 101597391

# -----------------------
# b. Create 4 variables:
gym_member = "Alix Alliton" # Data Type: String
preferred_weight_kg = 20.5 # Data Type: Float
highest_reps = 25 # Data Type: Integer
membership_active = True # Data Type: Boolean

# -----------------------
# c. Create a dictionary named workout_stats as per requirements:
# This dictionary maps key:value pairs of member names (data type --> String) to a tuple of mins spent on three different workout activities (data type --> Integer [int, int, int]):
workout_stats = {
    "Alix": (30, 45, 20), # ex. yoga, running, weightlighting
    "Jamie": (15, 10, 35),
    "Taylor": (20, 30, 15)
}

# -----------------------
# d. Using a loop, calculate the total workout minutes for each friend. Add new key-value pairs in the dictionary for each friend:
for friend, workout_minutes in workout_stats.items():
    total_workout_minutes = sum(workout_minutes)

    print(f"{friend} has worked out for a total of {total_workout_minutes} minutes.")
    # Adding new key-value pair to the dictionary:
    workout_stats[friend + "_total"] = total_workout_minutes

