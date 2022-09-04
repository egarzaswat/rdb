from pysca import scaTools as sca

def show_processmsa_results(sequence):

    print("*****Final processed alignment parameters****")
    if sequence.get('Nseq'):
        print("Number of sequences: M = %i" % (sequence['Nseq']))
    else:
        print("Missing key Nseq")
    if sequence.get('effseqs'):
        print("Number of effective sequences: M' = %i" % (sequence.get('effseqs')))
    else:
        print("Missing key effseqs")
    if sequence.get('Npos'):
        print("Number of alignment positions: L = %i" % (sequence.get('Npos')))
    else:
        print("Missing key Npos")
    if sequence.get('ats'):
        print("Number of positions in the ats: %i" % (len(sequence.get('ats'))))
        structPos = [i for (i, k) in enumerate(sequence.get('ats')) if k != "-"]
        print("Number of structure positions mapped: %i" % (len(structPos)))
    else:
        print("Missing key ats")
    if sequence.get('distmat'):
        print(
            "Size of the distance matrix: %i x %i"
            % (len(distmat), len(distmat[0]))
            )
    else:
        print("Missing key distmat")

    print( '*' *40)

def seq_count_check(sequence):
    print( 'The number of effective sequences in this MSA is: '+str(int(round(sequence['effseqs']))))

    if int(sequence['effseqs']) >= 100:
        print ('This alignment has a sufficient number of effective sequences for analysis with SCA.')
    else:
        print('This alignment does not have enough effective sequences to confidently analyze with SCA.')
        
    print ('Npos (L) = '+ str(sequence['Npos'])) 

def display_phylogenetic_groupings(sequence):

    Dseq = sequence[0]
    #construct a dictionary of phylogenetic groups
    annot = dict()
    for i, h in enumerate(Dseq['hd']):
        hs = h.split('|')
        annot[hs[0]] = sca.Annot(hs[1], hs[2], hs[3].replace('.',''))

    # Most frequent taxonomic groups:
    atleast = 1
    for level in range(4):
        descr_list = [a.taxo.split(',')[level] for a in annot.values() \
                    if len(a.taxo.split(',')) > level]
        descr_dict = {k:descr_list.count(k) for k in descr_list \
                    if descr_list.count(k)>=atleast}
        print('\n Level %i:' % level)
        print(descr_dict)