from typing import List

def selectionSort(array, size) -> List[int]:
  for i in range(i,n-1):
    min = i
    for j in range(i+1,n):
      if A[min]>A[j]:
        min = j
      swap(A[i],A[min])

# Do not change the following code
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(selectionSort(data, len(data)))
