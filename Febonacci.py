# def Febonacci(n):
#     if n == 1 :
#         result = 1
#     elif n == 2 :
#         result = 1
#     else:
#         result = Febonacci(n - 1) + Febonacci(n - 2)
#     return result 

# if __name__ == "__main__":
#     print Febonacci(3)
import time

result_dict = {}
def Febonacci_optimized(n):
    if n not in result_dict:
        result = Febonacci_optimized(n - 1) + Febonacci_optimized(n - 2) if n >= 3 else 1
        result_dict[n] = result
    else:
        result = result_dict[n]
    return result

def Febonacci(n):
    if n == 1 :
        result = 1
    elif n == 2 :
        result = 1
    else:
        result = Febonacci(n - 1) + Febonacci(n - 2)
    return result 

if __name__ == "__main__":
    start = time.time()
    print Febonacci_optimized(100)
    end = time.time()
    duration = end - start
    print duration