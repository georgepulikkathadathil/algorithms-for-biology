'''
This file contains just the functions from the classify functions exercise. 
Primarily, this is to make the code easier to run, test, and debug.
'''

def reverse_compliment(dna_sequence):
    '''
    This function takes a string representing a dna sequence 
    as input, and returns its reverse complement.
    '''
    compliments = {
        'T': 'A',
        'A': 'T',
        'C': 'G',
        'G': 'C'
    }

    rev_comp = []
    for c in dna_sequence[::-1]:
        rev_comp.append(compliments[c])
    
    return ''.join(rev_comp)


def count_occurance(genome, pattern):
    '''
    This function accepts two strings, one representing the genome
    of an organism (or a part of the genome) and another representing
    some smaller DNA/RNA pattern. It returns the number of times this
    pattern occurs within the provided genome.
    '''
    count = 0
    final_search_position = len(genome) - len(pattern) + 1
    
    for start_position in range(final_search_position):
        match = True
        for i, c in enumerate(pattern):
            if genome[start_position + i] != c:
                match = False
                break

        if match:
            count += 1
        
    return count


def unique_kmers(genome, k):
    '''
    This function takes in a string representing the genome of an
    organism (or section of a genome) and an integer value k. It 
    returns a list of all the unique substrings of length k
    (often called k-mers) contained in that genome.
    '''
    kmers = []
    final_kmer_position = len(genome) - k + 1
    
    for start_position in range(final_kmer_position):
        # Hint: Consider this line carefully... 
        kmer = genome[start_position:start_position + k]
        
        # Looping to check if this kmer is already in the list
        new_kmer = True
        for known_kmer in kmers:
            if known_kmer == kmer:
                new_kmer = False
                break

        if new_kmer:
            kmers.append(kmer)
    
    return kmers


def count_kmers(genome, k):
    '''
    This function accepts a string representing a genome
    and an integer k. It returns a dictionary which maps
    each occurring k-mer to the number of times that k-mer
    occurs within the genome.

    Note that it uses the above function, and so you 
    must consider that functions complexity in determining
    this functions complexity.
    '''
    all_kmers = unique_kmers(genome, k)

    kmer_counts = {}
    for kmer in all_kmers:
        # Start by assuming we don't encounter this kmer
        # (we know we will, but this makes the code cleaner)
        kmer_counts[kmer] = 0
        
        # Loop over the full genome searching for this kmer
        stop_position = len(genome) - k + 1
        for start_position in range(stop_position):
            inner_kmer = genome[start_position:start_position + k]
            
            if inner_kmer == kmer:
                kmer_counts[kmer] += 1

    return kmer_counts

