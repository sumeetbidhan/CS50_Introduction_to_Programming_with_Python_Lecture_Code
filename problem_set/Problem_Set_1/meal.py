def main():
    # Ask the user to input the time
    time_str = input("What time is it? ").strip()

    # Convert the time string to a float number of hours
    time = convert(time_str)

    # Check if it's breakfast time
    if 7 <= time <= 8:
        print("breakfast time")
    # Check if it's lunch time
    elif 12 <= time <= 13:
        print("lunch time")
    # Check if it's dinner time
    elif 18 <= time <= 19:
        print("dinner time")


def convert(time):
    # Split the time string into hours and minutes
    hours, minutes = time.split(":")
    # Convert hours and minutes to integers
    hours = int(hours)
    minutes = int(minutes)
    # Convert the time to a float number of hours
    return hours + minutes / 60.0


# This ensures that main() runs when the script is executed
if __name__ == "__main__":
    main()
