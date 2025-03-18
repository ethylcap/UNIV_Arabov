# a= int(input())
# b= int(input())
# a, b = b, a
# print(a , b)

# s= int(input())
# m=s//60
# print(m)

# x= float(input())
# y = float(input())
# z= x<0 and y>0
# print(z)

# a, b = int(input()), int(input())
# c = (a + a*b)/(a**2 + a*b) + (a**2+b**2)/(a+b)
# print(c)

# from math import *
# x = float(input())
# y = (1+sin(2*x))/((sin(x)-cos(x))**2)
# print(y)

# from math import *
# l = float(input())
# s = l**2 / (pi*4)
# print(s)

# num = float(input())
# print(num//100)

# def chess(x1, y1, x2, y2):
#     return abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1
# print(chess(3, 4, 4, 5))

# a= int(input())
# b= int(input())
# if a>b:
#     a,b=b,a
# print(a,b)


# def new_direction(current, command):
#     directions = ['С', 'З', 'Ю', 'В'] 
#     index = directions.index(current) 

#     if command == 1:
#         index = (index + 1) % 4  
#     elif command == -1:
#         index = (index - 1) % 4

#     return directions[index]

# print(new_direction('С', 1))   
# print(new_direction('С', -1))  
# print(new_direction('Ю', 1))   
# print(new_direction('В', -1))  
# print(new_direction('З', 0)) 


# def f(x):
#     if x <= 7:
#         return 3 * x - 9
#     else:
#         return 1 / (x**2 - 4)
# print(f(2))

# def replace_numbers(m, n):
#     if m != n:
#         max_val = max(m, n)
#         return [max_val, max_val]
#     return [0, 0]

# print(replace_numbers(5, 7)) 
# print(replace_numbers(4, 4))

# def near_point(a, b, c):
#     return "b" if abs(b - a) < abs(c - a) else "c"
# print(near_point(3, 6, 8)) 

# def over_mass(volume1, mass1, volume2, mass2):
#     density1 = mass1 / volume1
#     density2 = mass2 / volume2
#     return 1 if density1 > density2 else 2
# print(over_mass(3, 9, 2, 10))

# def find_month(n):
#     months = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]
#     return months[(n - 1) % 12]
# print(find_month(14))

# a= float(input())
# n= int(input())
# S=1
# for _ in range(n):
#     S*=a
# print(S)


# p= float(input())
# S=1000
# k=1
# while (S<1100):
#     k+=1
#     S+=(S*p)/100
# print(k)

# def buy_cattle():
#     for bulls in range(11):  
#         for cows in range(21):  
#             calves = 100 - bulls - cows 
#             if calves >= 0 and (bulls * 10 + cows * 5 + calves * 0.5) == 100:
#                 print(f"Быки: {bulls}, Коровы: {cows}, Телята: {calves}")
# buy_cattle()

# from math import *

# def n_sin(x, n):
#     result = sin(x)
#     for _ in range(n - 1):
#         result = sin(result)
#     return result

# x = float(input())
# n = int(input())
# print(n_sin(x, n))


# from math import *

# def sum_r(epsilon=0.001):
#     total_sum = 0
#     n = 0
#     while True:
#         term = factorial(n) / factorial(2 * n)
#         if term < epsilon:
#             break
#         total_sum += term
#         n += 1
#     return total_sum

# print(sum_r())

# def round_numbers(numbers):
#     rounded = [round(num) for num in numbers]
#     return rounded, sum(rounded)

# N = int(input())
# numbers = [float(input()) for _ in range(N)]

# rounded_list, total_sum = round_numbers(numbers)
# print(rounded_list, total_sum)



# def sum_of_divisors(n):
#     total = 1 
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             total += i
#             if i != n // i:
#                 total += n // i
#     return total

# def find_numbers(N):
#     pairs = []
#     checked = set()
    
#     for a in range(2, N + 1):
#         if a in checked:
#             continue
#         b = sum_of_divisors(a)
#         if b > a and b <= N and sum_of_divisors(b) == a:
#             pairs.append((a, b))
#             checked.add(b)
#     return pairs

# N = int(input())
# print(find_numbers(N))


# from math import *

# def triangle_area(a):
#     return (sqrt(3) / 4) * a ** 2

# def hexagon_area(a):
#     return 6 * triangle_area(a)

# a = 1
# area = hexagon_area(a)
# print(f"Площадь шестиугольника со стороной {a}: {area}")

# def Simm(S, i, j):
#     if i >= j:
#         return True
#     if S[i] != S[j]:
#         return False
#     return Simm(S, i + 1, j - 1)

# S = "abccba"
# i, j = 0, len(S) - 1
# result = Simm(S, i, j)
# print(result)