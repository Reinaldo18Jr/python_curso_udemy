# Controlando a quantidade de argumentos posicionais e nomeados em funções
# *args -> ilimitado de argumentos posicionais
# **kwargs -> ilimitado de argumentos nomeados

# Positional-Only Parameters (/) = Tudo antes da barra deve ser apenas posicional
# Keyword-Only Arguments (*) = * sozinho não suga valores.

def soma(x, y, /, a, b):
    print(x + y + a + b)

soma(2, 2, 2, b=2)


def subtrai(a, b, /, *, c):
    print(a - b - c)

subtrai(1, 2, c=3)
