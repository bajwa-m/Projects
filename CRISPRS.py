import re
from collections import defaultdict
#Program to get potential CRISPRS of length 21 ending in "-GG" with 
#last 10 non-GG nucleotides being unique. Output shown below code.

with open("dmel-all-chromosome-r6.02.fasta") as infile:
    infile_contents = infile.read()
    records = re.finditer(r"(>.*species=.*;){1,}(\n[ACTG]{4,}\n[ACTG]{4,}){1,}", infile_contents, re.M)
    for record in records:
        crisprs = re.finditer(r"([ATGC]{9}([ATGC]{10}GG))", record.group(2), re.M | re.S)
        header_count = 0
        for crispr in crisprs:
            if record.group(1):
                header_count += 1
                dict1={crispr.group(2):crispr.group(1)}
                dict_increm = defaultdict(int)
                dict_increm[crispr.group(2)] += 1 
            pos = crispr.start() + 1
            if header_count == 1:
                print("\n", record.group(1), "\n") 
            for key in dict_increm:
                if dict_increm[key]==1  :
                    print(dict1[key], key, "found at position: ", str(pos))
#Output: 
