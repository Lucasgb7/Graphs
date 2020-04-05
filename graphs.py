from collections import defaultdict

class Graphs(object):
    """ Implementação básica de um grafo. """

    def __init__(self, edges, directed=False):
        """Inicializa as estruturas base do grafo."""
        self.adj = defaultdict(set)
        self.directed = directed
        self.add_edge(edges)


    def get_vertices(self):
        """ Retorna a lista de vértices do grafo. """
        return list(self.adj.keys())


    def get_arestas(self):
        """ Retorna a lista de arestas do grafo. """
        return [(k, v) for k in self.adj.keys() for v in self.adj[k]]


    def add_edge(self, edges):
        """ Adiciona arestas ao grafo. """
        for u, v in edges:
            self.add_arch(u, v)


    def add_arch(self, u, v):
        """ Adiciona uma ligação (arco) entre os nodos 'u' e 'v'. """
        self.adj[u].add(v)
        # Se o grafo é não-direcionado, precisamos adicionar arcos nos dois sentidos.
        if not self.directed:
            self.adj[v].add(u)


    def exist_edge(self, u, v):
        """ Existe uma aresta entre os vértices 'u' e 'v'? """
        return u in self.adj and v in self.adj[u]

    def __len__(self):
        return len(self.adj)


    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self.adj))


    def __getitem__(self, v):
        return self.adj[v]

