from Bio import SeqIO
import sys

fasta_file = open(sys.argv[1], 'rU')
for record in SeqIO.parse(fasta_file, 'fasta'):
    id = record.id
    seq = record.seq
    file_sub = open(id + '.fasta', 'w')
    file_sub.write(">" + str(id) + "\n" + str(seq))
    file_sub.close()

fasta_file.close()
