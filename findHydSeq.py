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