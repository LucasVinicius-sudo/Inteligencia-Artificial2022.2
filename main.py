#Solução Utilizando iterative deepeng search , com isso conseguimos achar a solução otima
#Este algoritmo é uma adaptação deste que está no github : https://github.com/aroques/missionaries-and-cannibals
#além de se basear no livro da disiciplna
from missionaries_and_cannibals import iterative_deepening_search
from missionaries_and_cannibals import MissionariesAndCannibals


def main():
    problem = MissionariesAndCannibals()
    result = iterative_deepening_search(problem)

    if(result):
        print_result(result)

def print_result(result):
    for i,node in enumerate(result.path):
        if node.depth % 2 == 0:
            sign = "+"
        else:
            sign = "-"
        print('{}{}'.format(sign, node.action))
        print('---------------')
        print(' {}'.format(node.state.wrong_side))

if __name__ == '__main__':
    main()
