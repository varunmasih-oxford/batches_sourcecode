# import main_code as mcode

# multiply_result = mcode.multiply(10, 20)
# print("Multiply Result from module:", multiply_result)


from main_code import multiply , sum_total

multiply_result = multiply(10, 20)
print("Multiply Result from module:", multiply_result)

sum_result = sum_total(10, 20)
print("sum Result from module:", sum_result)
