# CONSTS
IMPERIAL_BMI_MULTIPLIER = 703


def calculate_square(height):
    return height * height


def calculate_bmi(height, weight, units="metric"):
    bmi = 0
    height_square = calculate_square(height)
    if units == "metric":
        bmi = float(weight / height_square)
    elif units == "imperial":
        bmi = float((weight / height_square) * IMPERIAL_BMI_MULTIPLIER)

    return round(bmi, 2)


def main():
    print("Hi, welcome in BMI calculator!")
    units = input("Do you want to use metric (m) or imperial (i) units? (M/I)\n")
    bmi = 0.0
    if units.lower() == "m":
        height = float(input("Please tell me your height in meters\nExample input: 1.83\n"))
        weight = float(input("Please tell me your weight in kilograms\nExample input: 70.5\n"))
        bmi = calculate_bmi(height, weight)
    elif units.lower() == "i":
        height = float(input("Please tell me your height in inches\nExample input: 72.2\n"))
        weight = float(input("Please tell me your weight in pounds\nExample input: 150\n"))
        bmi = calculate_bmi(height, weight, "imperial")

    print(f"Your BMI is {bmi}")
    return 0


if __name__ == '__main__':
    main()

# TODO
# passing arguments
# detecting whether given in cm or m
# version for passing arguments and without passing args
# add obese index
