distance_meters = float(input("Enter the distance in meters: "))
time = float(input("Enter time in minutes: "))
speed = ((distance_meters / 1000) / (time / 60))
print("speed is", speed, "km/h")
