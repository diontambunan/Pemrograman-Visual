#Dion Sandy Ara Tambunan
#20051397056
#2020MIB

class Matrix:
  def __init__(self, data):
    self.data = data
  def __repr__(self):
    return repr(self.data)  
  def __add__(self, other):
    data = []

    for j in range(len(self.data)):
        data.append([])
        for k in range(len(self.data[0])):
            data[j].append(self.data[j][k] + other.data[j][k])

    return Matrix(data)

x = Matrix([[1,4,6],[8,2,5],[7,9,3]])
y = Matrix([[1,4,6],[8,2,5],[7,9,3]])
print(x + y)