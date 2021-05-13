def read_fasta(file):
    '''
    Read k-tuples from .fasta file

    Input:
        file - the name of .fasta file
    Output:
        ans - the list of all k-tuples
    '''
    ans = []
    ktuple = ''
    inputs = open(file, 'r')
    for line in inputs:
        if line[0] == '>':
            if ktuple != '':
                ans.append(ktuple)
                ktuple = ''
        else:
            ktuple += line.strip()
    if ktuple != '':
        ans.append(ktuple)
    k = len(ans[0])
    for ktuple in ans:
        if len(ktuple) != k:
            raise ValueError
    return ans
