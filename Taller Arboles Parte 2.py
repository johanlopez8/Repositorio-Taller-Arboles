# Johan Francisco López (2241548), Juan Felipez Hernandez (2241796)

from bigtree import Node

# Crear nodos
root = Node("A")

# Nivel 1
b = Node("B", parent=root)
c = Node("C", parent=root)
d = Node("D", parent=root)

# Nivel 2
e = Node("E", parent=b)
f = Node("F", parent=b)
g = Node("G", parent=c)
h = Node("H", parent=d)
i = Node("I", parent=d)

# Nivel 3
j = Node("J", parent=f)
k = Node("K", parent=g)
l = Node("L", parent=g)
m = Node("M", parent=h)

# Nivel 4
n = Node("N", parent=j)
o = Node("O", parent=l)

# Mostrar estructura del árbol
print(root.show())
