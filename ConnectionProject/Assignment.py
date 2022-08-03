import logging
import sys

logger = logging.getLogger()
# logger object

logger.setLevel(logging.INFO)
# setting level

formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s',
                              '%m-%d-%Y %H:%M:%S')
# applying format to log file

stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.DEBUG)
stdout_handler.setFormatter(formatter)

file_handler = logging.FileHandler('test1.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stdout_handler)


class Assignment:
    def __init__(self):
        num1 = int(input('Enter number'))
        self.num = num1
        logger.info('the number entered by user is {}'.format(self.num))

    def pos_neg(self):
        if self.num < 0:
            logger.info('the number is  negative')
        else:
            logger.info('the number is positive')

    def even_odd(self):
        if self.num % 2 == 0:
            logger.info('The number is EVEN')
        else:
            logger.info('The number is ODD')

    def prime_or_not(self):
        flag = False
        if self.num > 1:
            # check for factors
            for i in range(2, self.num):
                if (self.num % i) == 0:
                    # if factor is found set flag=True
                    flag = True
                    # break the loop
                    break
        # check for flag status either it is True
        if flag:
            logger.info('the number {} '.format(self.num) + ' is not prime')
        else:
            logger.info('the number {} '.format(self.num) + ' is prime')

    def prime_or_not_interval(self):

        lower_value = int(input("Please, Enter the Lowest Range Value: "))
        upper_value = int(input("Please, Enter the Upper Range Value: "))

        print("The Prime Numbers in the range are: ")
        for number in range(lower_value, upper_value + 1):
            if number > 1:
                for i in range(2, number):
                    if (number % i) == 0:
                        break
                else:
                    logger.info(number)


a = Assignment()
a.pos_neg()
a.even_odd()
a.prime_or_not()
a.prime_or_not_interval()

# a = Assignment()
# a.year_leap()
