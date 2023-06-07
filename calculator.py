# IMPORTS
import argparse

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


def weight_range_calculator(bmi):
    if bmi < 18.5:
        category = "underweight"
    elif bmi <= 24.9:
        category = "normal"
    elif bmi <= 29.9:
        category = "overweight"
    else:
        category = "obese"

    return category


def main():
    parser = argparse.ArgumentParser(prog="calculator.py", usage="python3 %(prog)s [-h] [-H HEIGHT] [-W WEIGHT] ["
                                                                 "--units=metric]", description="This is simple BMI "
                                                                                                "calculator",
                                     epilog="Author: SoSaymon")
    parser.add_argument("-W", "--weight", type=float, help="Your weight. Example 68 or 149.1 (for imperial units)")
    parser.add_argument("-H", "--height", type=float, help="Your weight. Example 1.83 or 72 (for imperial units)")
    parser.add_argument("--units", type=str, default="metric", help="Units for your measurements (imperial or "
                                                                    "metric (default))")

    args = parser.parse_args()
    weight = args.weight
    height = args.height
    units = args.units

    bmi = 0.0

    if (weight is not None) and (height is not None):
        if units == "metric":
            bmi = calculate_bmi(height, weight)
        else:
            bmi = calculate_bmi(height, weight, "imperial")
    else:
        print("Hi, welcome in BMI calculator!")
        units = input("Do you want to use metric (m) or imperial (i) units? (M/I)\n")
        if units.lower() == "m":
            height = float(input("Please tell me your height in meters\nExample input: 1.83\n"))
            weight = float(input("Please tell me your weight in kilograms\nExample input: 70.5\n"))
            bmi = calculate_bmi(height, weight)
        elif units.lower() == "i":
            height = float(input("Please tell me your height in inches\nExample input: 72.2\n"))
            weight = float(input("Please tell me your weight in pounds\nExample input: 150\n"))
            bmi = calculate_bmi(height, weight, "imperial")

    weight_range = weight_range_calculator(bmi)

    print(f"Your BMI is {bmi} and you are {weight_range}")
    return 0


if __name__ == '__main__':
    main()
