def checker(genome, ktuples):
    '''
    Checks the result of assembly for correctness

    Input: 
        genome - the result of assembly
        ktuples - the input list of k-tuples
    Output:
        None
    '''
    gen_len = len(ktuples[0]) + len(ktuples) - 1
    if len(genome) != gen_len:
        raise ValueError
