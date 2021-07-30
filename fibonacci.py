import time


class fibonacciIter:

    def __init__(self, num = None):
        self.num = num

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.count = 0
        return self

    def __next__(self):

        assert type(self.num) is int, 'num must be a integer'

        if not self.num or (self.count < self.num):
            if self.count == 0:
                self.count += 1
                return self.n1
            elif self.count == 1:
                self.count += 1
                return self.n2
            else:
                self.sum = self.n1 + self.n2
                self.n1, self.n2 = self.n2, self.sum
                self.count += 1
                return self.sum
        else:
            raise StopIteration

def fiboYield():
    count = 0
    n1, n2 = 0,1
    while True:
        if count == 0:
            count += 1
            yield n1
        elif count == 1:
            count += 1
            yield n2
        else:
            sum = n1 + n2
            n1, n2 = n2, sum
            count += 1
            yield sum


if __name__ == '__main__':
    fibo = fibonacciIter(1)
    for element in fibo:
        print(element)
        time.sleep(0.05)

    fiboy = fiboYield()
    print('Aqui es con generadores')
    print(next(fiboy))
    print(next(fiboy))
    print(next(fiboy))
    print(next(fiboy))

    print('generadores expresions')
    listfibo = (fibo*3 for fibo in fiboy)

    print(next(listfibo))
    print(next(listfibo))
    print(next(listfibo))
