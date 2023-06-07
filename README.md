# BMI Calculator

This is a simple command-line program that calculates the Body Mass Index (BMI) based on your height and weight. The BMI is a measure of body fat based on an individual's weight and height. It provides an estimation of whether you have a healthy body weight for your height.

## Usage

To use the BMI calculator, run the `calculator.py` script with the following command-line arguments:

```bash
python3 calculator.py [-h] [-H HEIGHT] [-W WEIGHT] [--units=metric]
```

### Arguments

The script accepts the following arguments:

- `-h, --help`: Show the help message and exit.
- `-W WEIGHT, --weight WEIGHT`: Your weight in kilograms (or pounds for imperial units).
- `-H HEIGHT, --height HEIGHT`: Your height in meters (or inches for imperial units).
- `--units {metric,imperial}`: Units for your measurements. Use `metric` for kilograms and meters (default), or `imperial` for pounds and inches.

## Examples

Here are some examples of how to use the BMI calculator:

1. Calculate BMI using metric units:
    ```bash
    python3 calculator.py --weight 70.5 --height 1.83
    ```
2. Calculate BMI using imperial units:
    ```bash
    python3 calculator.py --weight 155 --height 72 --units imperial
    ```
3. If you don't provide the weight and height as command-line arguments, the program will prompt you to enter them interactively:
    ```bash
       python3 calculator.py
    ```
## Results

After calculating the BMI, the program will display the result, along with the corresponding weight category:

```bash
Your BMI is [BMI_VALUE] and you are [WEIGHT_CATEGORY].
```
## Contribution

Contributions to the BMI Calculator are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make the necessary changes and commit them.
4. Push your changes to your fork.
5. Submit a pull request.

Please ensure that your code follows the existing style and conventions used in the project. Also, remember to write tests for any new functionality you add.

## License

This project is licensed under the [MIT License](LICENSE).


## Contact

If you have any questions or suggestions regarding the BMI Calculator, please feel free to reach out:

- Author: SoSaymon
- Email: [szymon.chirowski@protonmail.com](mailto:szymon.chirowski@protonmail.com)
