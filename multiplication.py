number = int(input("Enter the number for which you want multiplication number:"))

i = 1
while i <= number:
    product = 0
    limit_number = int(input("enter the number till you want to multiply:"))

    for j in range (1, limit_number +1):
        product = number * j
        print (f"{number}*{j}={product}")
        i += 1