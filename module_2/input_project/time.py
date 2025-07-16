hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code below.

# Step 1: Add duration to minutes
total_mins = mins + dura

# Step 2: Figure out how many extra hours in the minutes

extra_hour = total_mins // 60  # how many full hours in total_minutes
final_mins = total_mins % 60 # what's left after taking out full hours


# Step 3: Add extra hours to start_hour
final_hour = (hour + extra_hour) % 24  # wrap around 24-hour clock

print(final_hour, ":", final_mins)