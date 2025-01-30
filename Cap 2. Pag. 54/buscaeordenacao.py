def buscaMenor(arr, tipo='a'):
    menor = arr[0]
    _indice = 0
    for i in range(1, len(arr)):
        if tipo == 'a':
            if arr[i] < menor:
                menor = arr[i]
                _indice = i
        elif tipo == 'd':
            if arr[i] > menor:
                menor = arr[i]
                _indice = i
        else:
            return None

    return _indice


def ordenacaoPorSelecao(arr):
    novoArr = []
    for i in range(len(arr)):
        menor = buscaMenor(arr)
        novoArr.append(arr.pop(menor))
    return novoArr


print(ordenacaoPorSelecao([5, 3, 6, 2, 10]))
