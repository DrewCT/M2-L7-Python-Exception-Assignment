#Task 1 Start Begin by asking the user to enter the temperature in Fahrenheit.
while True:
    user_input = input("Enter the temperature in Fahrenheit: ")

#Task 2 Write a function that converts the Fahrenheit temperature to Celsius using the formula (Fahrenheit - 32) * 5/9.
    def fahrenheit_to_celsius(fahrenheit):
        try:
            fahrenheit = float(fahrenheit)
            celsius = (fahrenheit - 32) * 5/9
            return celsius
        except ValueError:
            return None
        finally:
            print("Thank you for using our weather forecast application! Stay safe!")
        
    result = fahrenheit_to_celsius(user_input)
 
#Task 3 implement an else block that prints the converted temperature in a user-friendly format. 

    if result is not None:
        print(f"{user_input} degrees Fahrenheit is {result:.2f} degrees Celsius.")
    else:
        print("Error: Please enter a valid number for the temperature. No Letters.")

    try_again = input("Would you like to try another temperature? (yes/no): ").lower()
    if try_again != "yes":
        break

