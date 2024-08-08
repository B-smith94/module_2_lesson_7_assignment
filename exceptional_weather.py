#Task 1
temperature_in_fahrenheit = input("Temperature in Fahrenheit: ")

#Task 2
def temperature_conversion(temperature):
    try:
        celsius = round(((int(temperature) - 32) * 5/9), 2)
    except ValueError:
        print("Error: must input temperature as a whole number.")
#Task 3        
    else:
        print(f"{temperature}° Fahrenheit is {celsius}° Celsius.")
#Task 4    
    finally:
        print("Thank you for using this weather forcast application!")


temperature_conversion(temperature_in_fahrenheit)