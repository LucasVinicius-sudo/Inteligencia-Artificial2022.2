from collections import deque
#Cada letra na lista adjacencte que representa o gráfico , representa uma estação , ou seja E1 : A , E2 : B , E3: C e etc
#Retirado desse site : https://stackabuse.com/courses/graphs-in-python-theory-and-implementation/lessons/a-star-search-algorithm/
class Graph:


    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    # Função Heuristica
    def h(self, n):
        H = {
            'A': 1,
            'B': 1,
            'C': 1,
            'D': 1,
            'E': 1,
            'F': 1,
            'G': 1,
            'H': 1,
            'I': 1,
            'J': 1,
            'K': 1,
            'L': 1,
            'M': 1,
            'N': 1
        }

        return H[n]

    def a_star_algorithm(self, start_node, stop_node):

        open_list = set([start_node])
        closed_list = set([])


        g = {}

        g[start_node] = 0


        parents = {}
        parents[start_node] = start_node

        while len(open_list) > 0:
            n = None

            for v in open_list:
                if n == None or g[v] + self.h(v) < g[n] + self.h(n):
                    n = v;

            if n == None:
                print('Path does not exist!')
                return None


            if n == stop_node:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start_node)

                reconst_path.reverse()

                print('Path found: {}'.format(reconst_path))
                return reconst_path


            for (m, weight) in self.get_neighbors(n):
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight


                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)


            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None

def main():
    adjacency_list = {
        'A': [('B', 2)],
        'B': [('D', 4) ,('K',12)],
        'C': [('D', 7)],
        'D': [('H', 13),('M', 11)],
        'E': [('F',3),('G',2)],
        'I': [('K',12)],
        'H': [('L',7)],
        'M': [('N',5)]
    }

    graph1 = Graph(adjacency_list)
    graph1.a_star_algorithm('A','D')
main()
