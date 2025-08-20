# 🧮 BMI Calculator (Command-Line)

A simple Python program to calculate **Body Mass Index (BMI)** based on user input and classify the result into standard weight categories.

---

## 📋 Features

* Accepts user input for **weight (kg)** and **height (m)**
* Validates inputs to ensure they are positive numbers
* Calculates BMI using the standard formula
* Classifies the BMI into:

  * Underweight
  * Normal weight
  * Overweight
  * Obesity
* Handles errors gracefully

---

## 💡 How BMI is Calculated

The Body Mass Index is calculated using the formula:

```
BMI = weight (kg) / (height (m) ^ 2)
```

---

## 🔧 Requirements

* Python 3.6 or higher

No external packages are required.

---

## 🚀 How to Run

1. Save the script to a file, e.g., `bmi_calculator.py`

2. Open a terminal and navigate to the directory containing the file.

3. Run the program using:

```bash
python bmi_calculator.py
```

4. Follow the on-screen prompts to enter your weight and height.

---

## 🧪 Example Output

```
--- BMI Calculator (Command-Line) ---
Enter your weight in kilograms (kg): 70
Enter your height in meters (m): 1.75

Your BMI is: 22.86
You are classified as: Normal weight
```

---

## ⚠️ Input Validation

* The program ensures that both weight and height are **positive numbers**.
* If invalid data is entered (e.g., text or negative numbers), the user will be prompted again.

---

## 📁 File Structure

```
bmi_calculator.py    # Main script with BMI calculation logic
README.md            # Documentation
```



Let me know if you'd like to include unit tests, support for height in centimeters, or convert this into a GUI or web app.
