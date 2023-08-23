# for i in range(1,11):
#     print (i)
#     
#     
# print("\n")
# 
# for j in [1,2,3]:
#     print(j)
#     
# print("\n")
#     
# for i in range (0,20,2):
#     print (i)
#     
# print("\n")    
# def pattern(num):
#           for i in range(num):
#               print("*" * 4)
#     
# pattern(5)


def contains_a(input_string):
    for letter in input_string:
        if letter == 'a':
            return True
    return False

# Example usage
user_input = input("Enter a string: ")
result = contains_a(user_input)