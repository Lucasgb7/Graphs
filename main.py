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
                if neighbour not in visited: # Se ainda não foi visitado
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
                if vertice_inside not in visited:   # Se ainda não foi visitado
                    queue.append(vertice_inside)


def ftd(graph, vertice): # Fecho Transitivo Direto (Verifica por linha)
    visited = []
    missing_visit = [vertice]

    def search(graph):
            while missing_visit:    # Enquanto todos não foram visitados
                v = missing_visit.pop(0)    # Remove o primeiro da lista
                for y in range(nVertices):
                    if(matrix_adj[map_Vposition[v]][y]):    # Verifica na linha, passando por cada coluna para verificar vértices ligados
                        if(map_name[y] not in visited and map_name[y] not in missing_visit): # Se estiver ligado mas não foi vistado
                            missing_visit.append(map_name[y])
                visited.append(v)


    search(graph)
    return visited


def fti(graph, vertice): # Fecho Transitivo Indireto (Verificar por coluna)
    visited = []
    missing_visit = [vertice]

    def search(graph):
            while missing_visit:
                v = missing_visit.pop(0)    # Remove o primeiro da lista
                for x in range(nVertices):  # Em cada coluna
                    if(matrix_adj[x][map_Vposition[v]]): # Verifica na coluna, descendo a linha se o vértice esta ligado
                        if(map_name[x] not in visited and map_name[x] not in missing_visit):    # Se estiver ligado e ainda não foi visitado
                            #print("Linha: ",map_name[x] ,"Coluna: ", v)
                            missing_visit.append(map_name[x])   # Coloca seu caminho para os que faltam visitar
                visited.append(v)


    search(graph)
    return visited

def intersection(lst1, lst2): # Função para extrair a interseção de duas listas
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

#a,b,c,d,e,f,g,h,i
#a:e,d;d:a,f;f:d,g;g:f,e,i;e:a,g,b;i:g,c,h;b:e,c;c:b,i,h;h:c,i


#a,b,c,d,e,f,g
#a:b,d;b:c;c:g;d:e,f;e:a,b,g,c;f:c;g:b,f

#a,b,c,d,e
#a:b,e;b:d;c:a;d:c,e;e:b

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
nVertices = len(vertices) # Número de vértices

# Criando matriz de adjacência
matrix_adj = np.zeros((nVertices, nVertices))

map_Vposition = {} # Mapa para identificar as posições dos vértices na matriz de adjacência
map_name = {} # Mapa para nomear as posições com os respectivos vértices
for x in range(nVertices): # Laço para definir posição dos vértices na matriz de adjacência
    map_Vposition[vertices[x]] = x
    map_name[x] = vertices[x]

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
        matrix_adj[map_Vposition[x]][map_Vposition[y]] = 1
    else:
        matrix_adj[map_Vposition[x]][map_Vposition[y]] = 1
        matrix_adj[map_Vposition[y]][map_Vposition[x]] = 1

print(matrix_adj)

graph = Graphs(edge, direct) # Criando o grafo
print(graph.adj) # Lista de adjacências

############### CONECTIVIDADE ###############
# Define o vértice raiz para inicialização de busca (dfs, bfs, ftd, fti)
vertice_root = input("Defina um vértice raíz para verificar conectividade ou para realixar busca: ")
ftd_graph = {vertice_root: ftd(graph, vertice_root)} # Armazena os FTD's dos vértices
fti_graph = {vertice_root: fti(graph, vertice_root)} # Armazena os FTI's dos vértices

print("FTD da raíz: ",ftd(graph, vertice_root))
print("FTI da raíz: ",fti(graph, vertice_root))
intersec_root = intersection(ftd_graph[vertice_root], fti_graph[vertice_root])
print("Interseção de FTD e FDI: ", intersec_root)
print("Grafo completo", vertices)

if(all(elem in intersec_root  for elem in vertices)): # Verifica se a interseção possui todos os vértices do grafo
    print("O grafo É conexo!")
else:
    print("O grafo NÃO é conexo!")

#a,b,c,d,e,f,g
#a:b,d;b:c;c:g;d:e,f;e:a,b,g,c;f:c;g:b,f

inter = []
for v in vertices:  # Para cada vértice
    ftd_graph[v] = ftd(graph, v)    # Fecho Transitivo Direto
    fti_graph[v] = fti(graph, v)    # Fecho Transitivo Indireto

    inter_sort = sorted(intersection(ftd_graph[v], fti_graph[v]))     # Conjunto de vertices ordenados para realizar a comparação
    if( inter_sort not in inter):
        inter.append(inter_sort)
        print("Subgrafo fortemente conexo do vértice ", v, ": ", inter_sort) # Interseção entre os dois fechos

###############  BUSCA  ###############
search = input("Deseja realizar uma busca? (S-> Sim / N -> Não): ")
if search is "S" or search is "s":
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