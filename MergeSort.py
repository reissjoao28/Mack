# Função para realizar a ordenação utilizando Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])  # Ordena a metade esquerda
    right_half = merge_sort(arr[mid:])  # Ordena a metade direita
    
    # Função para combinar duas listas ordenadas
    return merge(left_half, right_half)

# Função para combinar duas listas ordenadas
def merge(left, right):
    sorted_list = []
    i = j = 0
    
    # Compara os elementos de ambas as listas e os adiciona à lista ordenada
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    
    # Adiciona os elementos restantes, se houver
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    
    return sorted_list

# Lista a ser ordenada
arr = [10, 154, 8, 0, 9, 48, 7, 55, 5]

# Ordena a lista usando merge sort
sorted_arr = merge_sort(arr)

print("Lista ordenada:", sorted_arr)
