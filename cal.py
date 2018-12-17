import random
import time

count = int(input('input the number of questions:'))
correct = 0
error = 0

start = time.time()
while (count - correct - error != 0):
    if (correct+error) % 10 == 0:
        print('{} questions left'.format(count-correct-error))
    num1 = int(random.random() * 20)
    num2 = int(random.random() * 20)
    if ((num1 - num2) > 10 or (0 < (num1 - num2) < 10 and num2 > 10)):
        answer = input(str(num1) + '-' + str(num2) + '=')
        if answer.isdigit():
            if num1 - num2 == int(answer):
                correct += 1
            else:
                error += 1
                print('wrong!')
        else:
            error += 1
    elif num1 + num2 <= 20:
        answer = input(str(num1) + '+' + str(num2) + '=')
        if answer.isdigit():
            if num1 + num2 == int(answer):
                correct += 1
            else:
                error += 1
                print('wrong!')
        else:
            error += 1
    else:
        pass
end = time.time()
print('correct number is {}'.format(correct))
print('error number is {}'.format(error))
print('time spent is {} mins and {} seconds'.format(int((end - start)/60), int(end - start)%60))