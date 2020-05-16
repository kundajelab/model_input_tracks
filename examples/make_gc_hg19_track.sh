#for flank_size in 1000
for flank_size in `seq 10 10 250` 1000
do
    make_gc_track --ref_fasta /users/annashch/male.hg19.fa \
		  --chrom_sizes /mnt/data/annotations/by_release/hg19/hg19.chrom.sizes \
		  --outf gc_hg19_$flank_size\bp_flank.bigwig\
		  --flank $flank_size & 
done
