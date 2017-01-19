
class Operator(object):

    def __init__(self, func):
        self.func = func
        self.args = []

    def __str__(self):
        print('{func} : {args}'.format(func=self.func, args=self.args))

    def __repr__(self):
        return '{func} : {args}'.format(name=self.name, func=self.func, args=self.args)

    def populate(self, *args):
        self.args = args

    def evaluate(self):
        args = self.args
        return self.func(args)
