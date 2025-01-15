class solution:
    def buscarMenor(self, arr):
        menor = arr[0]
        menor_indice = 0
        for i in range(1, len(arr)):
            if arr[i] < menor:
                menor = arr[i]
                menor_indice = i
        return menor_indice

    def orderedSelection(self, arr):
        novo_arr = []
        for i in range(len(arr)):
            menor = self.buscarMenor(arr)
            novo_arr.append(arr.pop(menor))
        return novo_arr


sm = solution()
a = [5, 2, 9, 6, 3]
print(sm.orderedSelection(a))
