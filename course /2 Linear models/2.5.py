class MyLineReg:
    def __init__(self, n_iter=100, learning_rate=0.1):
        self.n_iter = n_iter
        self.learning_rate = learning_rate

    def __str__(self):
        return f'MyLineReg class: n_iter={self.n_iter}, learning_rate={self.learning_rate}'


try:
    params = eval(input())
    model = MyLineReg(params['n_iter'], params['learning_rate'])
    print(model)
except (EOFError, KeyError):
    model = MyLineReg()
    print(model)
