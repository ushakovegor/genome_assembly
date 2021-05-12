def read_fasta(file):
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
    print(ans)
    return ans
