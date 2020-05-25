#average across 5 bases of the bigwig (with base at position 3)
import argparse
import pyBigWig
import pdb 
def parse_args():
    parser=argparse.ArgumentParser(description="smooth kmer bigwig track")
    parser.add_argument("-input_bigwig")
    parser.add_argument("-output_bigwig")
    #parser.add_argument("-chrom_sizes")
    parser.add_argument("--flank",type=int,default=2)    
    return parser.parse_args()

def main():
    args=parse_args()
    bw=pyBigWig.open(args.input_bigwig,'r')
    out_bw=pyBigWig.open(args.output_bigwig,'w')
    chroms=[i for i in bw.chroms().items()]
    print(chroms)
    interval_size=2*args.flank+1 
    #create the header in the output file.
    out_bw.addHeader(chroms)
    for entry in chroms:
        chrom=entry[0]
        chrom_size=entry[1]
        chrom_vals=bw.values(chrom,0,chrom_size)
        print("extracted current chromosome values from bigwig for chromosome:"+str(chrom))
        vals=[0.0]*args.flank
        for i in range(args.flank,chrom_size-args.flank):
            if i%1000000==0:
                print(str(i))
            cur_base=i
            start_pos=cur_base-args.flank
            end_pos=cur_base+args.flank+1
            vals.append(sum(chrom_vals[start_pos:end_pos])/interval_size)
        vals.append([0.0]*args.flank)
        #write to output bigwig
        out_bw.addEntries(chrom,0,values=vals,span=1,step=1)
        print("wrote bigwig entries for chrom:"+str(chrom))
    out_bw.close()
if __name__=="__main__":
    main()
    
