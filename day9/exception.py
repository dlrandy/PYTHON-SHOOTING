# try:
#   print(9/0)
# except ZeroDivisionError :
#   print('you can not divide by zero')
# # print(8/0)1

# print('Give me two numbers, and i will divide them.')
# print('Enter q to quit.')

# while True:
#   first = input('\nFirst num: ')
#   if first == 'q':
#     break
#   second = input('\n Second number')
#   if second == 'q':
#     break
#   try:
#     answer = int(first) /int(second)
#   except ZeroDivisionError:
#     print('you can not divide by 0 ')
#   else:
#     print(answer)


# filename = 'alice.txt'

# try:
#   with open(filename, encoding='utf-8') as f:
#     contents = f.read()
# except FileNotFoundError:
#   print(f"the file {filename} does not exist")



title = 'alice in   land'
print(title.split())



