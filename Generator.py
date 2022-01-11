from random import random, randint, choice


class Expression:
    pass


class Number(Expression):
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return str(self.num)


class BinaryExpression(Expression):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def __str__(self):
        return str(self.left) + " " + self.op + " " + str(self.right)


class ParenthesizedExpression(Expression):
    def __init__(self, exp):
        self.exp = exp

    def __str__(self):
        return "(" + str(self.exp) + ")"


e1 = Number(5)
e2 = BinaryExpression(
    Number(8), "+", ParenthesizedExpression(BinaryExpression(Number(7), "*", e1)))
SampleSpace = [chr(i) for i in range(65, 91)] + [i for i in range(1, 100)]

NoOfTestCases = 1e5


def randomExpression(prob):
    p = random()
    if p > prob:
        return Number(choice(SampleSpace))
    elif randint(0, 1) == 0:
        return ParenthesizedExpression(randomExpression(prob / 1.2))
    else:
        left = randomExpression(prob / 1.2)
        op = choice(["+", "-", "*", "/"])
        right = randomExpression(prob / 1.2)
        return BinaryExpression(left, op, right)


TestCasefile = open("testCASE", "w")
TestCasefile.writelines(
    f"{randomExpression(2)}\n"for i in range(int(NoOfTestCases)))
TestCasefile.close()
