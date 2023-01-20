from pyDatalog import pyDatalog
import random

pyDatalog.create_terms('factorial,N,X, Z, res, Sum, Average, random_sum')

#test
factorial[N]=N*factorial[N-1]
factorial[1]=1
print(factorial[4]==N)
print('\n\n\n')
f = open('output.txt','w')

# Сумма арифметической  прогрессии Sn = ((a1+an)*2n)/4 = ((1+888888)*2*888888)/4
Sum[X] = ((1 + X) * 2*X) / 4
print("Sum 1..888888: ")
print(Sum[888888] == X)
result = 'Sum 1..888888:\n' + (str)(Sum[888888] == X) + '\n' + '--'*5 + '\n'*2
f.write(result)

# Среднее арифметической  прогрессии (888888+1)/2
Average[X] = (X + 1) / 2
print("Average 1..888888: ")
print(Average[888888] == X)
result = 'Average 1..888888:\n' + (str)(Average[888888] == X) + '\n' + '--'*5 + '\n'*2
f.write(result)

# Сумма рандомных случайных чисел от 1 до 888888
rand_numbers = [random.choice(range(888888)) for i in range(100)]
(res["random_sum"] == sum_(Z, for_each=Z)) <= Z.in_(rand_numbers)
print("Random sum: ")
print(res["random_sum"] == X)
result = 'Random sum:\n' + (str)(res["random_sum"] == X) + '\n' + '--'*5 + '\n'*2
f.write(result)

# Медиана
print("Median: ")
print(rand_numbers[50])
result = 'Median:\n' + (str)(rand_numbers[50]) + '\n' + '--'*5 + '\n'*2
f.write(result)
f.close()
