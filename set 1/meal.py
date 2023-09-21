def main():
    time = input("What time it is? ")
    ct = convert(time)
    if ct >= 7 and ct <= 8:
        print("Breakfast time")
    elif ct >= 12 and ct <= 13:
        print("Lunch time")
    elif ct >= 18 and ct <= 19:
        print("Dinner time")


def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours) + (float(minutes) / 60)
    return hours


if __name__ == "__main__":
    main()