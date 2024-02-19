print("Newton's second law of Motion")
print("--------------------------------------------")

# Determine the missing value
print("Select the missing value:")
print("1. Mass(m)")
print("2. Acceleration(a)")
print("3. Force(F)")
missing_value_choce = input("Enter the option number for the missing value: ")

#Prompt the user to enter the other two values
if missing_value_choce == "1":
    a = float(input("Enter acceleration (a): "))
    F = float(input("Enter Force (F): "))
    m = F / a 
    print(f"Mass (m) = {m}")

elif missing_value_choce == "2":
    m = float(input("Enter mass (m): "))
    F = float(input("Enter force(F): "))
    a = F / m
    print(f"Acceleration (a) = {a}")

elif missing_value_choce == "3":
    m = float(input("Enter Mass (m): "))
    a = float(input("Entert Acceleration (a): "))
    F = m * a 
    print(f"Force (F)= {F}")

else:
    print("Invalid option selected for missing value.")