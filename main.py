
import operators
from BinaryOperator import BinaryOperator
from UnaryOperator import UnaryOperator

from concurrent.futures import ProcessPoolExecutor, as_completed
import random
import itertools

def main():
    stats = [0, 0]
    workers = 8
    with ProcessPoolExecutor(max_workers=workers) as executor:
        futures = []
        for i in range(0, workers):
            incr = 10000 // workers
            mini = incr * i
            maxi = mini + incr
            futures.append(executor.submit(calcTrain, mini, maxi))
        for f in as_completed(futures):
            fstats = f.result()
            stats[True] += fstats[True]
            stats[False] += fstats[False]
    print('True:', stats[True], 'False:', stats[False])

def calcTrain(mini, maxi):
    stats = [0, 0]
    for num in range(mini, maxi):
        seq = getSequence(num)
        sym = operators.SYMBOL_MAP
        x = False
        for q in itertools.permutations(seq):
            for i in itertools.product(operators.BINARY_OPS, repeat=3):
                for u in itertools.product(operators.CLAUSE_UNARY_OPS, repeat=3):
                    for s in itertools.product(operators.SINGLE_UNARY_OPS, repeat=4):
                        op1 = i[0]
                        op2 = i[1]
                        op3 = i[2]

                        s1 = UnaryOperator(s[0]).populate(q[0])
                        s2 = UnaryOperator(s[1]).populate(q[1])
                        s3 = UnaryOperator(s[2]).populate(q[2])
                        s4 = UnaryOperator(s[3]).populate(q[3])

                        # s1 = seq[0]
                        # s2 = seq[1]
                        # s3 = seq[2]
                        # s4 = seq[3]

                        c1 = BinaryOperator(op1).populate(s1, s2)
                        c1 = UnaryOperator(u[0]).populate(c1)
                        c2 = BinaryOperator(op2).populate(c1, s3)
                        c2 = UnaryOperator(u[1]).populate(c2)
                        c3 = BinaryOperator(op3).populate(c2, s4)
                        c3 = UnaryOperator(u[2]).populate(c3)
                        try:
                            if c3.evaluate() == 10:
                                x = True
                                #printSolution(seq, sym, c3, op1, op2, op3)
                                break
                        except ZeroDivisionError:
                            continue

        print(seq, ' : ', x)
        stats[x] += 1
    print('True:', stats[True], 'False:', stats[False])
    return stats

def printSolution(seq, sym, c3, op1, op2, op3):
    print("(({} {} {}) {} {}) {} {} = {}".format(seq[0], sym[op1], seq[1], sym[op2], seq[2], sym[op3], seq[3], c3.evaluate()))

def getSequence(num):
    if num < 10:
        return [0, 0, 0, num]
    if num < 100:
        l = [0, 0]
        l.extend(list(map(int, list(str(num)))))
        return l
    if num < 1000:
        l = [0]
        l.extend(list(map(int, list(str(num)))))
        return l
    return list(map(int, list(str(num))))

if __name__ == '__main__': main()