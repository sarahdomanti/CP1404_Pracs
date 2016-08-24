def main():
    score = float(input("Enter score: "))
    print(check_score(score))


def check_score(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Pass"
    else:
        return "Excellent"


main()
