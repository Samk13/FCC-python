# get largest and smallest in an array
# smallest = None
# largest = None
# total = 0
# count = 0
# for itervar in [3,41, 12, 9, 74, 15,2,1,300 ]:
#     if smallest is None or itervar < smallest:
#         smallest = itervar
#     if largest is None or itervar > largest:
#         largest = itervar
#     count += 1
#     total += itervar
# print("\n")
# print("---------")
# print("---------")
# print("count", count, '||')
# print("total", total, '||')
# print("smallest", smallest, '||')
# print("largest", largest, '||')
# print("---------")
# print("---------")

# # Exercices
# num = 0
# tot = 0
# while True:
#     sval = input('Enter a number: ')
#     if sval == 'done':
#         print('num', num)
#         print('total', tot)
#         break
#     try:
#         fval = float(sval)
#     except:
#         print('invalid input')
#         continue
#     print(fval)
#     num += 1
#     tot += fval

# stringCont = 0
# while True:
#     string = input('enter a string: ')
#     if string == 'done':
#         break
#     for i in string:
#         stringCont += 1
#     print(len(string))
#     print('total chars count -> ',stringCont)

# intermediate strings

# string = "  banan sana a   "
# fail = -1
# # print(string.upper().len(string))
# if string.find('sa') != fail:
#     newstring = string.replace('sana', 'SAMr').strip()
#     print(newstring.startswith('b'))
#     print(len(newstring))
# else:
#     print('here')

# i = string.find("nana")
# print(i)

# Excercise

str = "X-DSPAM-Confidance: 0.8475 "
strStart = str.find(':')
print(float(str[strStart +1:].strip()))
# 0.8475
