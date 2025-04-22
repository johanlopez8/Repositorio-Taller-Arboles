
# Johan Francisco López (2241548), Juan Felipez Hernandez (2241796)

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

class Arbol:
    def __init__(self, raiz):
        self.raiz = Nodo(raiz)

    def agregar_hijo(self, nodo_padre, valor_hijo):
        nuevo_hijo = Nodo(valor_hijo)
        nodo_padre.hijos.append(nuevo_hijo)
        return nuevo_hijo

    def peso(self, nodo=None):
        if nodo is None:
            nodo = self.raiz
        return 1 + sum(self.peso(hijo) for hijo in nodo.hijos)

    def orden(self, nodo=None):
        if nodo is None:
            nodo = self.raiz
        max_orden = len(nodo.hijos)
        for hijo in nodo.hijos:
            max_orden = max(max_orden, self.orden(hijo))
        return max_orden

    def altura(self, nodo=None):
        if nodo is None:
            nodo = self.raiz
        if not nodo.hijos:
            return 1
        return 1 + max(self.altura(hijo) for hijo in nodo.hijos)

# Ejemplo de uso
if __name__ == "__main__":
    arbol = Arbol("A")
    b = arbol.agregar_hijo(arbol.raiz, "B")
    c = arbol.agregar_hijo(arbol.raiz, "C")
    d = arbol.agregar_hijo(b, "D")
    e = arbol.agregar_hijo(c, "E")
    f = arbol.agregar_hijo(c, "F")
    g = arbol.agregar_hijo(c, "g")

    print("Peso del árbol:", arbol.peso())
    print("Orden del árbol:", arbol.orden())
    print("Altura del árbol:", arbol.altura())
