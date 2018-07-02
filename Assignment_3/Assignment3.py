my_list = []

first_term = (input('Enter your name :'))
second_term = input('Enter you phone-number: ')

my_list.append(first_term)
my_list.append(second_term)

print(my_list)

my_list.append(['google', 'apple', 'facebook', 'microsoft', 'tesla'])
print(my_list)

a = my_list.count(0)
print(a)

stack = ["A", "B", "C"]
stack.append("R")
stack.append("I")
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)

queue = ['Ganesh', 'Ram', 'Tanny']
queue.append('Sara')
queue.append('Timcy')
print(queue)
print(queue.popleft())
print(queue)
print(queue.popleft())
print(queue)
