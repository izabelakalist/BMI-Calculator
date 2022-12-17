name_1 = 'Ola'
height_m1 = 1.62
weight_kg1 = 52

name_2 = "Ola's brother"
height_m2 = 1.75
weight_kg2 = 75

name_3 = "Ola's friend "
height_m3 = 2.0
weight_kg3 = 100


def bmi_calculator(name, height_m, weight_kg):
    bmi = weight_kg / (height_m ** 2)
    print("bmi: ")
    print(bmi)
    if bmi < 25:
        return name + " is not overweight"
    else:
        return name + "is overweight"


result_1 = bmi_calculator(name_1, height_m1, weight_kg1)
result_2 = bmi_calculator(name_2, height_m2, weight_kg2)
result_3 = bmi_calculator(name_3, height_m3, weight_kg3)
print(result_1)
print(result_2)
print(result_3)


