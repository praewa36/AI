
def get_input(prompt, type_cast=str):
    """Get user input and convert to the specified data type."""
    while True:
        try:
            return type_cast(input(prompt))
        except ValueError:
            print(f"Invalid input. Please enter a {type_cast.__name__}.")

def compute_dosetpoint(minute_number, dosafe_values, doave_values):
    doset_values = {}
    for basin in range(1, 5):  # Basins 1 to 4
        for zone in range(1, 4):  # Zones 1 to 3
            key = f"{basin}{zone}"
            doset_values[key] = 1.667 * doave_values[str(zone)] * minute_number
    
    # Adjust based on the safe DO values
    for key, value in doset_values.items():
        if value < dosafe_values[key]:
            doset_values[key] = dosafe_values[key]
    
    return doset_values

def cli_program():
    print("Welcome to the DO Setpoint Calculation Program!")
    
    while True:
        minute_number = get_input("Enter the current minute number (0-1439): ", int)
        
        dosafe_values = {}
        for key in ["11", "12", "13", "21", "22", "23", "31", "32", "33", "41", "42", "43"]:
            dosafe_values[key] = get_input(f"Enter dosafe value for {key}: ", float)
        
        doave_values = {}
        for key in ["1", "2", "3"]:
            doave_values[key] = get_input(f"Enter doave value for zone {key}: ", float)
        
        computed_dosetpoints = compute_dosetpoint(minute_number, dosafe_values, doave_values)
        
        print("\nComputed DO Setpoints:")
        for key, value in computed_dosetpoints.items():
            print(f"Basin {key[0]}, Zone {key[1]}: {value:.2f}")
        
        continue_choice = get_input("\nDo you want to compute another set of DO setpoints? (yes/no): ", str).lower()
        if continue_choice != "yes":
            print("Thank you for using the DO Setpoint Calculation Program!")
            break

if __name__ == "__main__":
    cli_program()
