from queue import PriorityQueue


class AgenteBaseadoEmObjetivo:
    def __init__(self, grafo, objetivo):
        self.grafo = grafo
        self.objetivo = objetivo

    def funcao_de_custo(self, caminho):
        custo_total = 0
        for i in range(len(caminho) - 1):
            custo_total += self.grafo[caminho[i]][caminho[i + 1]]
        return custo_total

    # Implementando a busca de custo uniforme
    def busca_de_custo_uniforme(self):
        fila_de_prioridade = PriorityQueue()
        fila_de_prioridade.put((0, 'A'))
        visitados = set()

        while not fila_de_prioridade.empty():
            (custo, estado_atual) = fila_de_prioridade.get()
            if estado_atual not in visitados:
                visitados.add(estado_atual)

                if estado_atual == self.objetivo:
                    return custo

                for proximo_estado in self.grafo[estado_atual]:
                    if proximo_estado not in visitados:
                        custo_proximo_estado = custo + self.grafo[estado_atual][proximo_estado]
                        fila_de_prioridade.put((custo_proximo_estado, proximo_estado))

        return float('inf')

    # Implementando o método de busca do caminho mínimo
    def buscar_caminho_minimo(self):
        fila_de_prioridade = PriorityQueue()
        fila_de_prioridade.put((0, ['A']))

        while not fila_de_prioridade.empty():
            (custo, caminho) = fila_de_prioridade.get()
            estado_atual = caminho[-1]

            if estado_atual == self.objetivo:
                return caminho

            for proximo_estado in self.grafo[estado_atual]:
                novo_caminho = list(caminho)
                novo_caminho.append(proximo_estado)
                custo_proximo_estado = self.funcao_de_custo(novo_caminho)
                fila_de_prioridade.put((custo_proximo_estado, novo_caminho))

        return None


# Definindo o ambiente como um grafo
grafo = {
    'A': {'B': 2, 'C': 1},
    'B': {'D': 4, 'E': 2},
    'C': {'F': 4},
    'D': {'G': 2},
    'E': {'G': 3},
    'F': {'G': 5},
    'G': {}
}

# Criando um agente e buscando o caminho mínimo e custo mínimo
agente = AgenteBaseadoEmObjetivo(grafo, 'G')
caminho_minimo = agente.buscar_caminho_minimo()
custo_minimo = agente.funcao_de_custo(caminho_minimo)

# Exibindo os resultados
print("O caminho mínimo é:", caminho_minimo)
print("O custo mínimo é:", custo_minimo)
