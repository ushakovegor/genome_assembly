def checker(genome, ktuples):
    gen_len = len(ktuples[0]) + len(ktuples) - 1
    if len(genome) != gen_len:
        raise ValueError