def calculate_bmi(weight_kg, height_m):
    """
    Calculates the Body Mass Index (BMI).

    Args:
        weight_kg (float): Weight in kilograms.
        height_m (float): Height in meters.

    Returns:
        float: The calculated BMI.
    """
    if height_m <= 0:
        raise ValueError("Height cannot be zero or negative.")
    return weight_kg / (height_m ** 2)

def classify_bmi(bmi):
    """
    Classifies BMI into categories based on standard ranges.

    Args:
        bmi (float): The calculated BMI value.

    Returns:
        str: The BMI category (e.g., "Underweight", "Normal weight").
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25.0 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    print("--- BMI Calculator (Command-Line) ---")

    while True:
        try:
            weight_str = input("Enter your weight in kilograms (kg): ")
            weight_kg = float(weight_str)
            if weight_kg <= 0:
                print("Weight must be a positive number. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input for weight. Please enter a number.")

    while True:
        try:
            height_str = input("Enter your height in meters (m): ")
            height_m = float(height_str)
            if height_m <= 0:
                print("Height must be a positive number. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input for height. Please enter a number.")

    try:
        bmi = calculate_bmi(weight_kg, height_m)
        category = classify_bmi(bmi)

        print(f"\nYour BMI is: {bmi:.2f}") # Format to 2 decimal places
        print(f"You are classified as: {category}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()