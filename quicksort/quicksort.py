import random
import time


class Solution:
    # Pior caso: O(n^2) - Pivô sempre o primeiro elemento
    def quicksort_worst_case(self, arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[0]
        left = [x for x in arr[1:] if x <= pivot]
        right = [x for x in arr[1:] if x > pivot]

        return self.quicksort_worst_case(left) + [pivot] + self.quicksort_worst_case(right)

    # Melhor caso: O(n log n) - Pivô escolhido no meio
    def quicksort_best_case(self, arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2  # Escolhe o pivô no meio para evitar o pior caso
        pivot = arr[mid]
        left = [x for x in arr if x < pivot]
        right = [x for x in arr if x > pivot]
        middle = [x for x in arr if x == pivot]

        return self.quicksort_best_case(left) + middle + self.quicksort_best_case(right)


# Testando com uma lista grande

# Lista de 1000 elementos aleatórios
arr = [random.randint(1, 10000) for _ in range(1000)]

solver = Solution()

# Teste para o pior caso
# Para forçar o pior caso, ordenamos a lista antes
arr_sorted_worst = sorted(arr)
start = time.time()
solver.quicksort_worst_case(arr_sorted_worst)
end = time.time()
print(f"Tempo de execução (pior caso): {end - start:.6f} segundos")

# Teste para o melhor caso
start = time.time()
solver.quicksort_best_case(arr)
end = time.time()
print(f"Tempo de execução (melhor caso): {end - start:.6f} segundos")
