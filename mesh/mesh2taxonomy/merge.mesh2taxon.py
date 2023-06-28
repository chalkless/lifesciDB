#!/usr/bin/env python 
 
import argparse 
 
parser = argparse.ArgumentParser()
parser.add_argument('--taxon', '-t')
parser.add_argument('--mesh', '-m')
parser.add_argument('--outdate', '-o')
args = parser.parse_args()

f_taxon   = args.taxon
f_mesh    = args.mesh
f_outdate = args.outdate

txid2rank = {}
id_outdate = {}


with open(f_taxon) as h_taxon:
    for l_taxon in h_taxon:
        line = l_taxon.rstrip()

        ele = line.split('\t')

        txid2rank[ele[0]] = ele[1]
 
if f_outdate: 
    with open(f_outdate) as h_outdate:   
        for l_outdate in h_outdate:
            line = l_outdate.rstrip()
            ele = line.split('\t')
            id_outdate[ele[0]] = ele[2]

with open(f_mesh) as h_mesh:
    for l_mesh in h_mesh:
        line = l_mesh.rstrip()

        ele = line.split('\t')

        if ele[3] in id_outdate:
            txid = id_outdate[ele[3]]
        else:
            txid = ele[3] 
         
        if txid in txid2rank:
            rank = txid2rank[txid]
        else:
            rank = "\t".join(("-", "-"))

        ele.append(rank) 
 
        print("\t".join(ele)) 
 

