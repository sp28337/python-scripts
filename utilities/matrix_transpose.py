a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Транспонирование матрицы (поворот)
AA = [[row[i] for row in a] for i in range(len(a[0]))]
# Распаковка матрицы
A = [x for row in a for x in row]

print(a)
print(AA)
print(A)
