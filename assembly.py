'''
Usage:
    assembly.py [-i INPUT] [-o OUTPUT]

Options:
    -i INPUT   Name of the input .fasta-file [default: input.fasta]
    -o OUTPUT   Name of the output file [default: output.txt]
'''

from docopt import docopt
from graph_maker import graph_maker
from find_euler_path import find_euler_path
from read_fasta import read_fasta
from checker import checker


def main():
    args = docopt(__doc__)
    try:
        ktuples = read_fasta(args['-i'])
        graph, count_graph = graph_maker(ktuples)
        genome = find_euler_path(graph, count_graph)
        checker(genome, ktuples)
        print(genome)
    except Exception:
        print('There is no way to assembly the genome from this k-tuples')
    else:
        with open(args['-o'], 'w') as inp:
            inp.write(genome)


if __name__ == '__main__':
    main()
