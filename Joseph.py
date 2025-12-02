import sys


# Used for math functions like square root, although not used in these simple formulas
# import math

# --- Formula Functions ---
# Each function asks for input, calculates, and prints the result.

def distance_speed_time():
    # Formula: d = s * t (Distance)
    print("\n--- Formula: d = s * t (Distance) ---")
    # Use float() to allow for decimal inputs
    s = float(input("Enter Speed (s): "))
    t = float(input("Enter Time (t): "))
    d = s * t
    print(f"\nResult: Distance (d) = {d:.2f}")


def work_force_distance():
    # Formula: W = F * d (Work)
    print("\n--- Formula: W = F * d (Work) ---")
    F = float(input("Enter Force (F): "))
    d = float(input("Enter Distance (d): "))
    W = F * d
    print(f"\nResult: Work (W) = {W:.2f}")


def power_work_time():
    # Formula: P = W / t (Power)
    print("\n--- Formula: P = W / t (Power) ---")
    W = float(input("Enter Work (W): "))
    t = float(input("Enter Time (t): "))
    # Basic check to prevent division by zero
    if t == 0:
        print("\nError: Time (t) cannot be zero!")
        return
    P = W / t
    print(f"\nResult: Power (P) = {P:.2f}")


def density_mass_volume():
    # Formula: rho = m / V (Density)
    print("\n--- Formula: rho = m / V (Density) ---")
    m = float(input("Enter Mass (m): "))
    V = float(input("Enter Volume (V): "))
    if V == 0:
        print("\nError: Volume (V) cannot be zero!")
        return
    rho = m / V
    print(f"\nResult: Density (rho) = {rho:.2f}")


def pressure_force_area():
    # Formula: P = F / A (Pressure)
    print("\n--- Formula: P = F / A (Pressure) ---")
    F = float(input("Enter Force (F): "))
    A = float(input("Enter Area (A): "))
    if A == 0:
        print("\nError: Area (A) cannot be zero!")
        return
    P = F / A
    print(f"\nResult: Pressure (P) = {P:.2f}")


# --- Main Program Logic (Runs Once) ---

def run_calculator_once():
    """This function controls the user interaction and executes the chosen formula."""

    # Dictionary maps user choice (string) to a tuple (Name, Function)
    options = {
        '1': ("Distance (d = s * t)", distance_speed_time),
        '2': ("Work (W = F * d)", work_force_distance),
        '3': ("Power (P = W / t)", power_work_time),
        '4': ("Density (rho = m / V)", density_mass_volume),
        '5': ("Pressure (P = F / A)", pressure_force_area)
    }

    print("\n--- Intro to Python Physics Calculator ---")
    print("Choose a formula to calculate:")

    # Print the menu options
    for key, (name, _) in options.items():
        print(f"[{key}] {name}")

    # Get user input
    choice = input("Select a number (1-5): ").strip()

    if choice in options:
        try:
            # Execute the function for the chosen formula
            options[choice][1]()
        except ValueError:
            # Catch error if user types letters instead of numbers for parameters
            print("\nError: Invalid input. Please enter only numerical values.")
    else:
        print("\nError: Invalid selection. Program ending.")


# Start the program and exit immediately after running the function
if __name__ == "__main__":
    run_calculator_once()
    sys.exit()