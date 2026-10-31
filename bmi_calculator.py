def get_valid_input(prompt):
    """Continuously prompts the user until a valid positive number is entered."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Error: Please enter a positive number greater than 0.")
                continue
            return value
        except ValueError:
            print("Error: Invalid input. Please enter numeric values only.")

def classify_bmi(bmi):
    """Categorizes the BMI value based on standard health ranges."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Normal"
    elif 25 <= bmi <= 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("--- Command Line BMI Calculator ---")
    
    # 1. Prompt for input with validation
    weight = get_valid_input("Enter your weight in kg: ")
    height = get_valid_input("Enter your height in meters (e.g., 1.75): ")
    
    # 2. Calculate BMI (Weight / Height^2)
    bmi = weight / (height ** 2)
    
    # 3. Classify result
    category = classify_bmi(bmi)
    
    # 4. Display formatted results
    print(f"\nResult: Your BMI is {bmi:.2f}")
    print(f"Health Category: {category}")

if __name__ == "__main__":
    main()
