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

def dfs(graph, vertice, visited):
    def dfs_iterativa(graph, vertice_root):
        visited.append(vertice_root)
        missing_visit = [vertice_root]
        while missing_visit:
            vertice = missing_visit.pop()
            for neighbour in graph[vertice]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    missing_visit.append(neighbour)

    dfs_iterativa(graph, vertice)

def bfs(graph, vertice_root, visited):
    queue = []
    queue.append(vertice_root)
    while queue:
        vertice = queue.pop(0)
        if vertice not in visited:
            visited.append(vertice)
            for vertice_inside in graph[vertice]:   # Adiciona cada vértice a ser caminhado que não foi visitado
                if vertice_inside not in visited:
                    queue.append(vertice_inside)


def transD(graph, vertice):
    visitados = []
    aVisitados = [vertice]

    def search(graph):
            while aVisitados:
                v = aVisitados[0]
                aVisitados.remove(0)
                visitados.append(v)
                for y in range(length):
                    if(matriz[mapaNum[v]][y]):
                        if(mapaName[y] not in visitados):
                            aVisitados.append(mapaName[y])
                search(graph)


    search(graph)
    print(aVisitados)

directed = input("O grafo é direcional? (S-> Sim / N -> Não): ") # Definindo se o grafo é direcional
if directed is "S":
    direct = True
    G = nx.DiGraph()
else:
    direct = False
    G = nx.Graph()



vertices = input("Informe os vértices (Ex: a,b,c,d): ")
vertices = vertices.split(",")

length = len(vertices)

#Criando matriz
matriz = np.zeros((length,length))

mapaNum = {}
mapaName = {}
for x in range(length):
    mapaNum[vertices[x]] = x
    mapaName[x] = vertices[x]

edges = input("Informe as ligações.(Ex: a:b,c,d ; b:a,c,f):")
s = edges.split(";")

mapa = {}
for x in s:
     mapa[x.split(":")[0]] = x.split(":")[1].split(",")

edge =[]
for x in mapa:
    for y in mapa[x]:
        print(x,y)
        edge.append((x,y))

print(edge)


for x, y  in edge:
    if(direct):
        matriz[mapaNum[x]][mapaNum[y]] = 1
    else:
        matriz[mapaNum[x]][mapaNum[y]] = 1
        matriz[mapaNum[y]][mapaNum[x]] = 1

print(matriz)

graph = Graphs(edge, direct) # Criando o grafo
print(graph.adj) # Lista de adjacências

search = input("Deseja realizar uma busca? (S-> Sim / N -> Não): ")
if search is "S" or search is "s":
    vertice_root = input("Defina qual o vértice raíz para realização da busca: ")
    search_type = input("Deseja realizar busca de em Largura(L) ou Profundidade(P)?: ")
    visited = []
    if search_type == "L":
        bfs(graph, vertice_root, visited)
    elif search_type == "P":
       dfs(graph, vertice_root, visited)
    else:
        print("Digite uma letra correta!")

    print("Ordem de vértices a partir da raíz: ", visited)
else:
    print("Legal.")

G.add_nodes_from(vertices) # Definindo os vértices na biblioteca gráfica
G.add_edges_from(edge)
nx.draw(G, with_labels="true")
plt.show() # display