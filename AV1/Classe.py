class Grafo:
    def __init__(self):
        self.grafo = {}
    
    @property        
    def quantidadeVertices(self):
        return len(self.grafo)

    def adicionaVertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = []

    def adicionaAresta(self, vertice1, vertice2):
        if vertice1 in self.grafo:
            self.grafo[vertice1].append(vertice2)
        else:
            self.grafo[vertice1] = [vertice2]

        if vertice2 in self.grafo:
            self.grafo[vertice2].append(vertice1)
        else:
            self.grafo[vertice2] = [vertice1]
    
    def mostraGrafo(self):
        for vertice in self.grafo:
            print(f"{vertice} -> {', '.join([str(vizinho) for vizinho in self.grafo[vertice]])}")
    
    def grauVertice(self,vertice):
        if vertice in self.grafo:
            return len(self.grafo[vertice])
            
    def quantidadeArestas(self):
        total_graus = sum(self.grauVertice(vertice) for vertice in self.grafo)
        return total_graus / 2
    
    def dirac(self):
        if self.quantidadeVertices < 3:
            print("Grafo não Hamiltoniano pelo Teorema de Dirac")
            return
        
        for vertice in self.grafo:
            if self.grauVertice(vertice) < self.quantidadeVertices / 2:
                print("Grafo não Hamiltoniano pelo Teorema de Dirac")
                return

        print("Grafo Hamiltoniano pelo Teorema de Dirac")