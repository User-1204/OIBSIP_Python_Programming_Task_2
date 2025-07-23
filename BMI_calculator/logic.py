# logic.py
# BMI calculation and category logic

def calculate_bmi(weight, height):
    return round(weight / (height ** 2), 2)  # Formula: weight/height²

def categorize_bmi(bmi):
    # Return category and suggestion based on BMI value
    if bmi < 18.5:
        return "Underweight", "Consider a proper nutritious diet and consult a professional."
    elif bmi < 24.9:
        return "Normal weight", "Great job! Maintain your healthy habits."
    elif bmi < 29.9:
        return "Overweight", "Try regular exercise and mindful eating."
    else:
        return "Obese", "Consider seeking advice from a health professional."
