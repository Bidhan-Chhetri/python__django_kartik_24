car = {
        "brand1": "toyota",
        "brand2": "nissan",
        "brand3": "tesla",
        "brand4": "honda",
        "brand5": "bugatti",
        "brand6": "audi"
       }

car_name = input("Enter the car name: ")

found = False

for key, value in car.items():
    if car_name == value:
        print(f"{value.capitalize()} is in the dictionar.")
        found = True
        break

if found == False:
    print("Enter another car the entred car is not in dictionary.")