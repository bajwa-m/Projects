import re
with open("dmel-all-chromosome-r6.02.fasta") as infile:
    infile_contents = infile.read()
    records = re.finditer(r"(>.*species=.*;){1,}(\n[ACTG]{4,}\n[ACTG]{4,}){1,}", infile_contents, re.M)
    for record in records:
        seq = re.finditer(r"([ATGC]{9}([ATGC]{10}GG))", record.group(2), re.M | re.S)
        header_count = 0
        for h in seq:
            if record.group(1):
                header_count += 1
            pos = h.start() + 1
            if header_count == 1:
                print("\n", record.group(1), "\n") 
            print(h.group(), "found at position ", str(pos))
