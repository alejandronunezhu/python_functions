def convert(time: str) -> float:
    hours, minutes = time.split(":")
    return int(hours) + int(minutes) / 60

def main() -> None:
    time = input("Time: ")
    total = convert(time)

    if 7 <= total <= 8:
        print("breakfast time")
    elif 12 <= total <= 13:
        print("lunch time")
    elif 18 <= total <= 19:
        print("dinner time")
    else:
        print("fasting time")

if __name__ == "__main__":
    main()
