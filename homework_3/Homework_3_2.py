
# numbers = [2,5,13,7,6,4]
# size = 6
# sum = 0
# avg = 0
# index = 0
# while index < size:
#     sum = sum + numbers[index]
#     index = index + 1
# avg = sum/size
# print(avg)





def AVG (sum,list_numbers):
    avg = sum / len(list_numbers)
    return avg

def list_sum (list_numbers):
    index = 0
    sum = 0
    while index < len(list_numbers):
        sum = sum + int(list_numbers[index])
        index = index + 1
    return sum

list_numbers = input('Пожалуйста введите элементы массива через пробел :').split()

print(AVG(list_sum(list_numbers),list_numbers))
