def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    withoutDollar = d.replace("$", "")
    return float(withoutDollar)


def percent_to_float(p):
    withoutPercent = p.replace("%", "")
    withoutPercent = int(withoutPercent)
    withoutPercent /= 100
    return float(withoutPercent)


main()
