weather = input()
time_of_day = input()

if weather == "sunny":
    if time_of_day == "day":
        print("You can play with your car toy.")
    else:
        print("It's night, Time to sleep")

elif weather == "rainy":
    if time_of_day == "cloudy":
        print("You can play with your boat toy.")
    else:
        print("You can stay warm and have a cup of coffee.")

elif weather == "snowy":
    if time_of_day == "clear":
        print("You can play with your snowman toy.")
    else:  
        print("You can play with your teddy bear toy.")

else:
    print("You can stay inside and read a story book.")