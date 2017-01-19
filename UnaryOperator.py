
from Operator import Operator

class UnaryOperator(Operator):

    def populate(self, arg):
        self.arg = arg
        return self

    def evaluate(self):
        return self.func(self.arg)