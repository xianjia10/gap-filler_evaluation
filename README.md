# gap-filler_evaluation

## Usage
You need to run jellyfish before you can run this python script.https://github.com/gmarcais/Jellyfish

```shell{}
jellyfish count -m 21 -s 1G -t 16 -C reference.fasta

# for HiFi reads alignments, we recommand use unique kmer.
jellyfish dump -c -U 1 mer_counts.jf > ref.kmer

```

```shell
 $ python evaluation.py
usege:python ./evaluation.py reference_kmers filled_genome_kmers
```