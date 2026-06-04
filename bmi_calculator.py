def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """Calculate BMI given weight in kilograms and height in meters."""
    if height_m <= 0:
        raise ValueError("height must be > 0")
    return weight_kg / (height_m * height_m)


def classify_bmi(bmi: float) -> str:
    """Return BMI category for a BMI value."""
    if bmi < 18.5:
        return "Underweight"
    if bmi < 25:
        return "Normal weight"
    if bmi < 30:
        return "Overweight"
    return "Obesity"


def _prompt_positive_float(prompt: str) -> float:
    while True:
        try:
            raw = input(prompt).strip()
            val = float(raw)
            if val <= 0:
                print("Please enter a positive number.")
                continue
            return val
        except ValueError:
            print("Please enter a valid number (e.g. 72.5).")


def main() -> None:
    print("BMI Calculator")
    print("Choose units: (M)etric kg/m or (I)mperial lb/in")
    choice = input("Units [M/I]: ").strip().lower()

    if choice.startswith("i"):
        weight_lb = _prompt_positive_float("Weight (lb): ")
        height_in = _prompt_positive_float("Height (in): ")
        weight_kg = weight_lb * 0.45359237
        height_m = height_in * 0.0254
    else:
        weight_kg = _prompt_positive_float("Weight (kg): ")
        height_m = _prompt_positive_float("Height (m): ")

    try:
        bmi = calculate_bmi(weight_kg, height_m)
    except ValueError as e:
        print("Error calculating BMI:", e)
        return

    category = classify_bmi(bmi)
    print(f"\nYour BMI is {bmi:.2f} — {category}")


if __name__ == "__main__":
    main()
