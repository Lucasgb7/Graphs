"""""
Fazer um programa que permita criar um grafo, com numero de vertices e arestas/arcos informados pelo usuário.
Apartir do grafo informado, verificar se o grafo é conexo ou não. E caso não seja conexo, identificar os sub-grafos 
fortemente conexos do grafo. Também deve ser possível verificar a sequencia dos vertices percorridos pelas buscas em Largura e Profundidade.
- A interface do programa fica a critério da equipe, mas deve priorizar a usabilidade (facilidade de informar os dados e visualizar os resultados).
Alunos:
    Lucas José da Cunha
    Luiz Alberto Zimmermann Zabel Martins Pinto
    
Disciplina: Grafos
Professor: Rudimar Luis Scaranto Dazzi
"""""
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from graphs import Graphs

def dfs(graph, vertice, visited): # Depth First Search (DFS) - Busca por Profundidade
    def dfs_iterativa(graph, vertice_root):
        visited.append(vertice_root)
        missing_visit = [vertice_root]
        while missing_visit: # Enquanto todos não foram visitados
            vertice = missing_visit.pop()
            for neighbour in graph[vertice]: # Para cada vizinho do vértice em questão
                if neighbour not in visited:
                    visited.append(neighbour)
                    missing_visit.append(neighbour)

    dfs_iterativa(graph, vertice) # Recursivamente retorna a função até que todos tenham sido visitados

def bfs(graph, vertice_root, visited): # Breadth First Search (BFS) - Busca por Largura
    queue = [] # Cria uma fila
    queue.append(vertice_root) # Add a raíz na fila
    while queue: # Enquanto houverem itens na fila
        vertice = queue.pop(0) # Remove o primeiro elemento da fila
        if vertice not in visited: # Verifica se o vértice foi visitado
            visited.append(vertice)
            for vertice_inside in graph[vertice]:   # Adiciona cada vértice a ser caminhado que não foi visitado
                if vertice_inside not in visited:
                    queue.append(vertice_inside)


def ftd(graph, vertice): # Fecho Transitivo Direto
    visited = []
    missing_visit = [vertice]

    def search(graph):
            while missing_visit:
                v = missing_visit[0]
                print(v)
                missing_visit.pop(0)

                visited.append(v)
                for y in range(length):
                    if(matriz[mapaNum[v]][y]):
                        if(mapaName[y] not in visited):
                            missing_visit.append(mapaName[y])
                search(graph)


    search(graph)
    print(visited)


def fti():
    pass




#INICIO DO PROGRAMA
directed = input("O grafo é direcional? (S-> Sim / N -> Não): ") # Definindo se o grafo é direcional
if directed is "S":
    direct = True
    G = nx.DiGraph() # Função gráfica para utilizar arcos (direcional)
else:
    direct = False
    G = nx.Graph() # Função gráfica para utilizar arestas (não direcional)



vertices = input("Informe os vértices (Ex: a,b,c,d): ") # Lendo os vértices do usuário
vertices = vertices.split(",") # Adicionando os vértices numa lista
length = len(vertices)

# Criando matriz de adjacência
matriz = np.zeros((length,length))

mapaNum = {} # Mapa para identificar as posições dos vértices na matriz de adjacência
mapaName = {}
for x in range(length): # Laço para definir posição dos vértices na matriz de adjacência
    mapaNum[vertices[x]] = x
    mapaName[x] = vertices[x]

edges = input("Informe as ligações.(Ex: a:b,c,d ; b:a,c,f):") # Lendo as ligações (arestas)
s = edges.split(";") # Dividindo os vértices de suas ligações

mapa = {}
for x in s:
     mapa[x.split(":")[0]] = x.split(":")[1].split(",")

edge =[] # Lista de ligações
for x in mapa: # Reorganizando as ligações
    for y in mapa[x]:
        print(x,y)
        edge.append((x,y))

print(edge)


for x, y  in edge: # Preenchendo a matriz de adjacência com suas respectivas ligações
    if(direct):
        matriz[mapaNum[x]][mapaNum[y]] = 1
    else:
        matriz[mapaNum[x]][mapaNum[y]] = 1
        matriz[mapaNum[y]][mapaNum[x]] = 1

print(matriz)

graph = Graphs(edge, direct) # Criando o grafo
print(graph.adj) # Lista de adjacências

ftd(graph, "a")

search = input("Deseja realizar uma busca? (S-> Sim / N -> Não): ")
if search is "S" or search is "s":
    vertice_root = input("Defina qual o vértice raíz para realização da busca: ")
    search_type = input("Deseja realizar busca de em Largura(L) ou Profundidade(P)?: ")
    visited = []
    if search_type == "L": # Busca do tipo largura
        bfs(graph, vertice_root, visited)
    elif search_type == "P":
       dfs(graph, vertice_root, visited) # Busca do tipo profundidade
    else:
        print("Digite uma letra correta!")

    print("Ordem de vértices a partir da raíz: ", visited)
else:
    print("Legal.")

G.add_nodes_from(vertices) # Definindo os vértices na biblioteca gráfica
G.add_edges_from(edge) # Adicionando as arestas/arcos no gráfico
nx.draw(G, with_labels="true")
plt.show() # display