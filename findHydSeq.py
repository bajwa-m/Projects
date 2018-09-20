import re

with open("test.fasta") as file:
    file_contents=file.read()
    matches=re.findall(r">.*\n.*\n",file_contents)
    for match in matches:
        records=re.finditer(r"(>.*;)\n(.*)", match)
        for record in records:
            hyd_seq=re.finditer(r"[VILMFWCA]{8,}",record.group(2))
            header_count=0
            for h in hyd_seq:
                if record.group(1):
                    header_count+=1
                pos=h.start()+1
                if header_count==1:
                    print("\n", record.group(1),"\n") 
                print(h.group(), "found at position ", str(pos))
"""Output:
 >P30450 | Homo sapiens (Human). | NCBI_TaxID=9606; | 365 |    Name=HLA-A; Synonyms=HLAA; 

AVVAAVMW found at position  325

 >A7MBM2 | Homo sapiens (Human). | NCBI_TaxID=9606; | 1401 |    Name=DISP2; Synonyms=DISPB, KIAA1742; 

VAVLMLCLAVIFLC found at position  170
LLALVAIFF found at position  493
IWICWFAALAA found at position  705
LALALAFA found at position  970"""
