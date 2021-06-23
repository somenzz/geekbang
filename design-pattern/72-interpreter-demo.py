from abc import ABCMeta
from numbers import Real
import re
from collections import deque

class Expression(metaclass=ABCMeta):
    def interpret(self, stats: dict) ->bool:
        pass

class BoolExpression(Expression):

    def __init__(self, express: str):
        self.express = express

    def interpret(self, stats: dict) ->bool:
        if self.express == 'True':
            return True
        return False


class GreaterExpression(Expression):

    def __init__(self, express:str = None, key:str = None, value: Real = None):
        if express:
            elements = re.split(r"\s+", express)
            if len(elements) == 3 and elements[1] == '>':
                self.key = elements[0]
                self.value = float(elements[2])
            else:
                raise Exception("Invalid GreaterExpression")
        elif key and value:
            self.key = key
            self.value = value
        else:
            raise Exception("GreaterExpression init error")


    def interpret(self, stats: dict) ->bool:
        if self.key in stats:
            return stats[self.key] > self.value
        return False



class LessExpression(Expression):

    def __init__(self, express:str = None, key:str = None, value: Real = None):
        if express:
            elements = re.split(r"\s+", express)
            if len(elements) == 3 and elements[1] == '<':
                self.key = elements[0]
                self.value = float(elements[2])
            else:
                raise Exception("Invalid LessExpression")
        elif key and value:
            self.key = key
            self.value = value
        else:
            raise Exception("LessExpression init error")


    def interpret(self, stats: dict) ->bool:
        if self.key in stats:
            return stats[self.key] < self.value
        return False



class EqualExpression(Expression):

    def __init__(self, express:str = None, key:str = None, value: Real = None):
        if express:
            elements = re.split(r"\s+", express)
            if len(elements) == 3 and elements[1] == '==':
                self.key = elements[0]
                self.value = float(elements[2])
            else:
                raise Exception("Invalid EqualExpression")
        elif key and value:
            self.key = key
            self.value = value
        else:
            raise Exception("EqualExpression init error")


    def interpret(self, stats: dict) ->bool:
        if self.key in stats:
            return stats[self.key] == self.value
        return False


class AndExpression(Expression):

    def __init__(self, express:str):
        self.express_list = []
        strExpressions = re.split(r"\s+&&\s+", express)
        for express in strExpressions:
            if '>' in express:
                self.express_list.append(GreaterExpression(express))
            elif '<' in express:
                self.express_list.append(LessExpression(express))
            elif '==' in express:
                self.express_list.append(EqualExpression(express))
            elif 'True' == express or 'False' == express:
                self.express_list.append(BoolExpression(express))


    def interpret(self, stats: dict) ->bool:
        for expression in self.express_list:
            if expression.interpret(stats) == False:
                return False
        return True



class OrExpression(Expression):

    def __init__(self, express:str):
        self.express_list = []
        strExpressions = re.split(r"\s+\|\|\s+", express)
        for express in strExpressions:
            self.express_list.append(AndExpression(express))



    def interpret(self, stats: dict) ->bool:
        for expression in self.express_list:
            if expression.interpret(stats) == True:
                return True
        return False



class AlertRuleInterpreter:

    def __init__(self, ruleExpression: str):
        self.expression = OrExpression(ruleExpression)

    def interpret(self, stats: dict) -> bool:
        return self.expression.interpret(stats)


## 有括号需要借助栈

class ComplexAlertRuleInterpreter:


    def __init__(self, ruleExpression: str):
        self.expression = ruleExpression

    def interpret(self, stats: dict) -> bool:

        stack = deque()
        for express in re.split(r"\s+", self.expression):
            if express == '(':
                stack.append(express)
                continue
            elif express == ')':
                #取出括号内容，并计算
                tmp_express = deque()
                while len(stack) > 0:
                    tmp = stack.pop()
                    if tmp == '(':
                        break
                    else:
                        tmp_express.appendleft(tmp)
                #计算结果
                result = AlertRuleInterpreter(" ".join(tmp_express)).interpret(stats)
                stack.append(str(result))
                continue

            else:
                stack.append(express)

        return AlertRuleInterpreter(" ".join(stack)).interpret(stats)



if __name__ == "__main__":
    # rule = "key1 > 100 && key2 < 30"
    rule = "key1 > 101 && ( ( key2 < 30 || ( key3 < 100 || key4 == 88 ) ) || False ) && True"

    interpreter = ComplexAlertRuleInterpreter(rule)
    stats = {}
    stats["key1"] = 120
    stats["key3"] = 121
    stats["key4"] = 88
    alert = interpreter.interpret(stats)
    print(alert)
