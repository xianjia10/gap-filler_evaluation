#!/usr/bin/env python
import sys
import math
if len(sys.argv) <3:
    print(f"usege:python {sys.argv[0]} reference_kmers filled_genome_kmers")
    exit(1)


def read_file(path):
    kmers=set()
    with open(path) as f:
        for line in f:
            line = line.split()
            kmers.add(line[0])
    return kmers


ref_kmer=read_file(sys.argv[1])
kmers=read_file(sys.argv[2])
completeness= len(kmers & ref_kmer) /len(ref_kmer) 
accuracy =len(kmers & ref_kmer)/len(kmers)
print("completeness %.4f"%completeness)
print("accuracy %.4f"%accuracy)



