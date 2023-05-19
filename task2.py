def calculateBMI(weight, heightInCM):
    try:
        height = heightInCM / 100
        return weight / height ** 2
    except ZeroDivisionError:
        raise ValueError("Height must be a non-zero positive value.")

def main():
    try:
        weight = int(input("Enter the weight in kg: "))
        if weight <= 0:
            raise ValueError("Weight must be a positive value.")
        

            
        heightInCM = int(input("Enter your height in cm: "))
        if heightInCM <= 0:
            raise ValueError("Height must be a positive value.")
            
        bmi = calculateBMI(weight, heightInCM)
        print("BMI: {:.2f}".format(bmi))

        if bmi < 18.5:
            print("The person is underweight")
        elif bmi <= 25:
            print("The person's weight is in the normal range")
        else:
            print("The person is overweight")

    except ValueError as e:
        print("Invalid input:", str(e))

main()

