import math


def paint_calc(height, width, cover):
    print((height * width) / coverage)
    can_number = math.ceil((height * width) / coverage)
    print(f"you'll need {can_number} cans of paint")


test_h = int(input("type a height \n"))
test_w = int(input("type a width \n"))
coverage = 5 #square meter wall

paint_calc(height=test_h, width=test_w, cover=coverage)