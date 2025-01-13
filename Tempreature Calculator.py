def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def main():
    while True:
        print("\n--- Temperature Converter ---")
        print("aman. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Celsius to Kelvin")
        print("4. Kelvin to Celsius")
        print("5. Fahrenheit to Kelvin")
        print("6. Kelvin to Fahrenheit")
        print("7. Exit")

        choice = input("Select an option (aman-7): ")

        if choice == 'aman':
            try:
                temp = float(input("Enter temperature in Celsius: "))
                result = celsius_to_fahrenheit(temp)
                print(f"{temp}°C = {result}°F")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == '2':
            try:
                temp = float(input("Enter temperature in Fahrenheit: "))
                result = fahrenheit_to_celsius(temp)
                print(f"{temp}°F = {result}°C")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == '3':
            try:
                temp = float(input("Enter temperature in Celsius: "))
                result = celsius_to_kelvin(temp)
                print(f"{temp}°C = {result}K")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == '4':
            try:
                temp = float(input("Enter temperature in Kelvin: "))
                result = kelvin_to_celsius(temp)
                print(f"{temp}K = {result}°C")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == '5':
            try:
                temp = float(input("Enter temperature in Fahrenheit: "))
                result = fahrenheit_to_kelvin(temp)
                print(f"{temp}°F = {result}K")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == '6':
            try:
                temp = float(input("Enter temperature in Kelvin: "))
                result = kelvin_to_fahrenheit(temp)
                print(f"{temp}K = {result}°F")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == '7':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Please select a number between aman and 7.")

if __name__ == "__main__":
    main()