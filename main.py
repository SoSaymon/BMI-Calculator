def calculate_square(height):
    return height * height


def calculate_bmi_metric(height, weight):
    height_square = calculate_square(height)
    return float(weight / height_square)


def main():
    print("Hi, welcome in BMI calculator!")
    height = float(input("Please tell me your height in m\nExample input: 1.83\n"))
    weight = float(input("Please tell me your weight in kg\nExample input: 70.5\n"))
    bmi = calculate_bmi_metric(height, weight)
    print(f"Your BMI is {bmi}")
    return 0


if __name__ == '__main__':
    main()
