class Grafo:
    def __init__(self):
        self.grafo = {}

    @property        
    def quantidadeVertices(self):
        return len(self.grafo)
    
    @property
    def vertices(self):
        return list(self.grafo.keys())
    
    @property
    def arestas(self):
        lista_arestas = set()
        for vertice, vizinhos in self.grafo.items():
            for vizinho in vizinhos:
                if (vizinho, vertice) not in lista_arestas:
                    lista_arestas.add((vertice, vizinho))
        return list(lista_arestas)

    def adicionaVertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = []

    def adicionaAresta(self, vertice1, vertice2):
        if vertice1 not in self.grafo:
            self.grafo[vertice1] = []
        if vertice2 not in self.grafo:
            self.grafo[vertice2] = []
        if vertice2 not in self.grafo[vertice1]:
            self.grafo[vertice1].append(vertice2)
        if vertice1 not in self.grafo[vertice2]:
            self.grafo[vertice2].append(vertice1)
    
    def mostraGrafo(self):
        for vertice in self.grafo:
            print(f"{vertice} -> {', '.join(map(str, self.grafo[vertice]))}")
    
    def grauVertice(self, vertice):
        return len(self.grafo.get(vertice, []))
            
    def quantidadeArestas(self):
        return sum(self.grauVertice(vertice) for vertice in self.grafo) / 2
    
    def dirac(self):
        if self.quantidadeVertices < 3:
            return "Grafo não Hamiltoniano pelo Teorema de Dirac"
        
        for vertice in self.grafo:
            if self.grauVertice(vertice) < self.quantidadeVertices / 2:
                return "Grafo não Hamiltoniano pelo Teorema de Dirac"

        return "Grafo Hamiltoniano pelo Teorema de Dirac"
        
    def ore(self):
        if self.quantidadeVertices < 3:
            return "Grafo não Hamiltoniano pelo Teorema de Ore"
        
        for v1 in self.grafo:
            for v2 in self.grafo:
                if v1 != v2 and v2 not in self.grafo[v1]:
                    if self.grauVertice(v1) + self.grauVertice(v2) < self.quantidadeVertices:
                        return "Grafo não Hamiltoniano pelo Teorema de Ore"
                    
        return "Grafo Hamiltoniano pelo Teorema de Ore"
    
    def bondyChvatal(self):
        pass
       
       