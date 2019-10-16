for flank_size in `seq 10 10 250` 1000
do
    make_gc_track --ref_fasta mm10_no_alt_analysis_set_ENCODE.fasta \
		  --chrom_sizes /mnt/data/annotations/by_release/mm10/mm10.chrom.sizes \
		  --outf gc_mm10_$flank_size\bp_flank.bigwig\
		  --flank $flank_size & 
done
