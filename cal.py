import random
import time

count = int(input('input the number of questions:'))
correct = 0
error = 0

start = time.time()
while (count - correct - error != 0):
    num1 = int(random.random() * 20)
    num2 = int(random.random() * 10)
    if num1 - num2 >= 0:
        answer = input(str(num1) + '-' + str(num2) + '=')
        if answer.isdigit():
            if num1 - num2 == int(answer):
                correct += 1
            else:
                error += 1
                count += 10
                print('wrong!')
        else:
            print('wrong input')
    elif num1 + num2 <= 20:
        answer = input(str(num1) + '+' + str(num2) + '=')
        if answer.isdigit():
            if num1 + num2 == int(answer):
                correct += 1
            else:
                error += 1
                count += 10
                print('wrong!')
        else:
            print('wrong input')
    else:
        pass
    if (correct+error) % 10 == 0:
        print('{} questions finished'.format(correct+error))
end = time.time()
print('correct number is {}'.format(correct))
print('error number is {}'.format(error))
print('time spent is {} mins and {} seconds'.format(int((end - start)/60), int(end - start)%60))