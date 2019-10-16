for flank_size in 1000
#for flank_size in `seq 10 10 250`
do
    make_gc_track --ref_fasta /mnt/data/annotations/by_release/hg38/GRCh38_no_alt_analysis_set_GCA_000001405.15.fasta \
		  --chrom_sizes /mnt/data/annotations/by_release/hg38/hg38.chrom.sizes \
		  --outf gc_hg38_$flank_size\bp_flank.bigwig\
		  --flank $flank_size & 
done
