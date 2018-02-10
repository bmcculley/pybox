from multiprocessing.dummy import Pool as ThreadPool
from functools import partial

def say(a,b):
    print("%s, %s!"% (a, b))

names = ['Noah', 'Liam', 'Mason', 'Jacob', 'William', 'Ethan', 'James',
        'Alexander', 'Michael', 'Benjamin', 'Elijah', 'Daniel', 'Aiden', 'Logan',
        'Matthew', 'Lucas', 'Jackson', 'David', 'Oliver', 'Jayden' ]
        
pool = ThreadPool(10)

func = partial(say, "Hello")
pool.map(func, names)

pool.close()
pool.join()