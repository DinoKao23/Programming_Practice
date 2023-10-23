

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    remove_d = d.removeprefix("$").removesuffix(".00")
    int_d = int(remove_d)
    return int_d


def percent_to_float(p):
    remove_p = p.removesuffix("%")
    int_d = float(remove_p) *0.01
    return int_d


main()