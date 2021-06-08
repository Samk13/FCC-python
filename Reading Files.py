# try:
#     handle = open('tests.txt')
# except:
#     print('-----------------------------------')
#     print('\n X File cannot be open or format is not supported!\n')
#     print('-----------------------------------')
#     quit()
# count = 0
# for i in handle:
#     if i.strip(). startswith('sam'):
#         count += 1
#         print('\n',i.strip())
# print('\n accurencies -> ',count, '\n')

# 07 - 01 EX - Python

try:
    textFile = open('test.txt')
except:
    print('-----------------------------------')
    print('\n X File cannot be open or format is not supported!\n')
    print('-----------------------------------')
    quit()
for line in textFile:
    print(line.strip().upper())