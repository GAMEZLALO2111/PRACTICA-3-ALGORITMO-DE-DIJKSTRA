# -*- coding: utf-8 -*-
"""
Created on Sat Jun  7 11:50:48 2025

Cruz Eduardo Gamez Rodriguez
21110301
"""

import sys  # Importar el módulo sys para usar sys.maxsize
import matplotlib.pyplot as plt  # Importar matplotlib para gráficos
import networkx as nx  # Importar NetworkX para trabajar con grafos

V = 6  # Número de vértices en el grafo

def select_min_vertex(value, processed):
    # Inicializa el mínimo y el vértice a -1
    minimum = sys.maxsize
    vertex = -1
    for i in range(V):
        # Si el vértice no ha sido procesado y su valor es menor que el mínimo
        if not processed[i] and value[i] < minimum:
            vertex = i  # Actualizar el vértice y el mínimo
            minimum = value[i]
    return vertex  # Retorna el vértice con el valor mínimo

def dijkstra(graph):
    parent = [-1] * V  # Almacena la estructura del camino más corto
    value = [sys.maxsize] * V  # Valores iniciales de las distancias
    processed = [False] * V  # TRUE si el vértice ya está procesado

    # Nodo inicial
    value[0] = 0  # La distancia al nodo inicial es 0

    for _ in range(V - 1):
        u = select_min_vertex(value, processed)  # Seleccionar el mejor vértice usando un método greedy
        processed[u] = True  # Marcar el vértice como procesado

        # Relajar los vértices adyacentes
        for j in range(V):
            # Condiciones de relajación
            if graph[u][j] != 0 and not processed[j] and value[u] != sys.maxsize and (value[u] + graph[u][j] < value[j]):
                value[j] = value[u] + graph[u][j]  # Actualizar el valor de distancia
                parent[j] = u  # Actualizar el padre del vértice

    edges = []  # Lista para almacenar las aristas del camino más corto
    for i in range(1, V):
        print(f"U->V: {parent[i]}->{i}  wt = {graph[parent[i]][i]}")  # Imprimir caminos y pesos
        edges.append((parent[i], i, graph[parent[i]][i]))  # Guardar las aristas del camino más corto
    
    # Generar gráfica
    plot_graph(graph, edges)

def plot_graph(graph, edges):
    G = nx.Graph()  # Crear un grafo
    # Añadir nodos
    for i in range(V):
        G.add_node(i)
    
    # Añadir todas las aristas con sus pesos
    for i in range(V):
        for j in range(V):
            if graph[i][j] != 0:
                G.add_edge(i, j, weight=graph[i][j])

    # Posiciones para los nodos
    pos = nx.spring_layout(G)  # Usar layout de resorte para la posición

    # Dibujar todos los nodos
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10)
    # Añadir etiquetas a las aristas
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(i, j): graph[i][j] for i in range(V) for j in range(V) if graph[i][j] != 0})

    # Resaltar el camino más corto
    nx.draw_networkx_edges(G, pos, edgelist=[(u, v) for u, v, w in edges], edge_color='red', width=2)  # Resaltar en rojo

    # Cambiamos a un gráfico de dispersión
    plt.figure(figsize=(8, 6))  # Define el tamaño de la figura
    for u, v, w in edges:
        # Añadir un scatter para cada arista del camino más corto
        plt.scatter([u, v], [w, w], color='red', s=100, zorder=5)  # Plotear la conexión

    plt.title("Camino más corto usando Dijkstra", fontsize=15)  # Título del gráfico
    plt.xlabel("Nodos")  # Etiqueta de los ejes
    plt.ylabel("Peso de las aristas")
    plt.grid(True)  # Mostrar la cuadrícula
    plt.show()  # Mostrar la gráfica

# Grafo de entrada
graph = [
    [0, 1, 4, 0, 0, 0],
    [1, 0, 4, 2, 7, 0],
    [4, 4, 0, 3, 5, 0],
    [0, 2, 3, 0, 4, 6],
    [0, 7, 5, 4, 0, 7],
    [0, 0, 0, 6, 7, 0]
]

# Llamada a la función Dijkstra
dijkstra(graph)  # Ejecutar el algoritmo de Dijkstra
