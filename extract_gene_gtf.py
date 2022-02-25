#!/usr/bin/python3

import sys
import gzip

in_fn = sys.argv[1]
out_fn = sys.argv[2]

print(in_fn)
print(out_fn)

#in_fn = "Salmo_salar-GCA_905237065.2-2021_07-genes.gtf.gz"
#out_fn = "gene.txt"

out_file = open(out_fn, 'w')

with gzip.open(in_fn,'rt') as f:
    for l in f:
        if l[0] == "#":
            continue
        tem = l.split("\t")
        if tem[2] == "gene":
            tem2 = tem[8].split(";")[0]
            gene_ID = tem2.split(" ")[1]
            res = tem[0] + "\t" + tem[3] + "\t" + tem[4] + "\t" + gene_ID + "\n"
            out_file.writelines(res)

f.close()
out_file.close()