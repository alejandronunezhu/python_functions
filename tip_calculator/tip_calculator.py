def main() -> None:
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d: str) -> float:
    float_amount = ""
    for char in d[1:-1]:
        float_amount += char
    return float(float_amount)

def percent_to_float(p: str) -> float:
    float_percent = ""
    for char in p[0:-1]:
        float_percent += char
    return float(float_percent) / 100

main()
