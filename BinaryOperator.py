
from Operator import Operator

class BinaryOperator(Operator):

    def populate(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        return self

    def evaluate(self):
        return self.func(self.arg1, self.arg2)
