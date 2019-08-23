import argparse
import pyBigWig
import pysam
import pdb 
def parse_args():
    parser=argparse.ArgumentParser("generated genome-wide bigwig track of GC content")
    parser.add_argument("--ref_fasta")
    parser.add_argument("--chrom_sizes")
    parser.add_argument("--outf")
    parser.add_argument("--flank",type=int,default=50,help="n bases on either of side of chromosome position to incorporate in calculation of gc content, i.e. n=50 gives 100 bp window")
    return parser.parse_args()


def make_bigwig_header(chrom_size_dict):
    header=[]
    for chrom in chrom_size_dict:
        header.append((chrom,chrom_size_dict[chrom]))
    return header 

def main():
    args=parse_args()
    
    #open reference fasta file 
    ref=pysam.FastaFile(args.ref_fasta)

    #parse chrom sizes file into dictionary & get bigwig header
    chrom_sizes=open(args.chrom_sizes,'r').read().strip().split('\n')
    chrom_size_dict=dict()
    for line in chrom_sizes:
        tokens=line.split('\t')
        chrom_size_dict[tokens[0]]=int(tokens[1])
        
    bigwig_header=make_bigwig_header(chrom_size_dict)
    print(bigwig_header)
    #open output bigwig 
    outf=pyBigWig.open(args.outf,'w')
    outf.addHeader(bigwig_header)
    
    window_size=2*args.flank
    for chrom in chrom_size_dict:        
        #get size of current chrom 
        cur_chrom_size=chrom_size_dict[chrom]
        
        #get sequence of current chrom
        cur_seq=ref.fetch(chrom,0,chrom_size_dict[chrom]).lower()
        print("got chromosome sequence for chrom:"+str(chrom))
        vals=[0.0]*(args.flank)

        for pos in range(args.flank,cur_chrom_size-args.flank):
            if pos %1000000==0:
                print(pos)
            window_seq=cur_seq[pos-args.flank:pos+args.flank]
            g_count=window_seq.count('g')
            c_count=window_seq.count('c')
            gc_fract=(g_count+c_count)/window_size
            vals.append(gc_fract)
        vals=vals+([0.0]*args.flank)
        print(len(vals))
        print(cur_chrom_size) 
        assert len(vals)==cur_chrom_size
        
        #write values to bigwig
        outf.addEntries(chrom,0,values=vals,span=1,step=1)
        print("wrote bigwig entries for chrom:"+str(chrom))
    outf.close() 
        
            
if __name__=="__main__":
    main()
    
