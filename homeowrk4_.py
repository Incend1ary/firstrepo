from functools import reduce
n = int(input("введите число для вычисления факториала"))
def reduce_func(el1, el2):
    return el1*el2

new_list = [el for el in range(1,n+1)]
 # print(reduce(reduce_func, new_list))
gen = reduce(lambda el1, el2: el1 * el2, [el for el in range(1, n+1)])

print(gen)

# def fact_gen(n):
#     f_num = 1
#     if n == 0:
#         yield f'(n)! = 1'
#     for i in range(1, n+1):
#         f_num *= i
#         yield f'{i}! = {f_num}'
# for _ in fact_gen(n):
#     print(_)


