def convert(time):
    final = ""
    x = time.split(":")
    first = x[0]
    second = x[1]
    final += first
    second = int(second)
    second = (second/60) * 10
    second = str(second)
    final += second
    final = float(final)
    final = final/10
    return final


def main():
    time = input("What time is it?")
    time = convert(time)
    time = float(time)
    if (time >= 7) and (time < 8):
        return("breakfast time")
    elif (time > 12) and (time <= 13):
        return("lunch time")
    elif (time > 18) and (time < 19):
        return("dinner time")

if __name__ == "__main__":
    print(main())


