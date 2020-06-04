import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s : %(name)s : %(message)s")

file_handler = logging.FileHandler("sample.log")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(stream_handler)

logger.addHandler(file_handler)


def add(x, y):
    return x+y


def sub(x, y):
    return x - y


def mul(x,y):
    return x * y


def div(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        logger.exception("Try to divide by zero")
    else:
        return result

num1 = 10
num2 = 0

add_result = add(num1, num2)
logger.debug("Add : {} + {} = {}".format(num1, num2, add_result))

sub_result = sub(num1, num2)
logger.debug("Sub : {} - {} = {}".format(num1, num2, sub_result))

mul_result = mul(num1, num2)
logger.debug("Mul: {} * {} = {}".format(num1, num2, mul_result))

div_result = div(num1, num2)
logger.debug("Div: {} / {} = {}".format(num1, num2, div_result))




