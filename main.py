from math_function import add, multiply, divide

def main():
     data_1 = int(input(Enter input 1: ))
     data_2 = int(input(Enter input 2: ))
     operator = input(Enter operator: )

     if operator == +:
         result = add(data_1, data_2)
     elif operator == *:
         result = multiply(data_1, data_2)
        print(Invalid operator)
     elif operator == /:
         result = divide(data_1, data_2)
     else:
         print(Maaf ya, operator belum ditambahkan hehe)

 if name == main:
     main()
 
