# Generator functions em Python
# generator = (n for n in range(10000))

def generator(n=0):
    yield 1 # pausar            
    print('Continuando...')
    yield 2 # pausar
    print('Mais uma vez...')
    yield 3 # pausar
    print('Terminando...')
    return 'ACABOU'


gen = generator(n=0)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

for n in gen:
    print(n)



def numeros(n=0, maximum=10):
    while True:
        yield n
        n += 1

        if n > maximum:
            return


func = numeros()
for n in func:
    print(n)
