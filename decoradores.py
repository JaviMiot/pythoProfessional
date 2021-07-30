def ladrar(func):
    def wrapper():
        print('guau guau')
        func()
    
    return wrapper

@ladrar
def grune():
    print('gr gr')

grune()

from datetime import datetime


def execution_time(func):
    def wrapper(*args, **kwargs):
        init_time = datetime.now()
        func(*args,**kwargs)
        final_time = datetime.now()
        total_elapsed = final_time - init_time
        print(f'Pasaron: {total_elapsed.total_seconds()} segundos')

    return wrapper

@execution_time
def random_function():
    for _ in range(1,100000000):
        pass

@execution_time
def suma(a:int, b:int) -> int:
    return a + b

suma(2,3)
random_function()