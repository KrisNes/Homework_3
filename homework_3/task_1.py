
# numbers_1 = [2,5,13,7,6,4]
# size_1 = 6 
# sum_1 = 0
# avg_1 = 0 
# index = 0
# while index<size_1:
#     sum_1=sum_1+numbers_1[index]
#     index=index+1
# avg_1=sum_1/size_1
# print(avg_1)



# def sum_full (sum_1,numbers_1,index,size_1):
#     while index<size_1:
#         sum_1 = sum_1 + numbers_1[index]
#         index=index+1
#     return sum_1

# def average (sum_1,size_1):
#     avg=sum_1/size_1
#     return avg

# numbers_1 = [2,5,13,7,6,4]
# size_1 = 6 
# sum_1 = 0
# avg_1 = 0
# index = 0
# new_sum = sum_full (sum_1,numbers_1,index,size_1)
# new_avg = average (new_sum,size_1)
# print(new_avg)



def count_max (numbers_1,index_1,maximum,count_maximal):
    while index_1 < len(numbers_1):
        if numbers_1[index_1] > maximum:
            maximum = numbers_1[index_1]
            count_maximal = 1
        else:
            if numbers_1[index_1] == maximum:
                count_maximal = count_maximal + 1
        index_1 = index_1 + 1 
    return count_maximal

numbers_1 = [1,8,3,8,2,6,8,8]
index_1 = 0 
maximum = numbers_1[index_1]
count_maximal = 0 
result = count_max(numbers_1,index_1,maximum,count_maximal)
print(result)


