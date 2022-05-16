#def for printing genes.txt into lists in 1 list.
f = open("genes.txt","r")
w = f.read()
f.close()
z= w.split()

#def checks if the gene is correct or false
def hello(x):
    k=3
    o=6
    for i in x:
        if x[0:3]=="ATG":
            if len(x)%3==0:
                if x[len(x)-3:]=="TAA" or x[len(x)-3:]=="TAG" or x[len(x)-3:]=="TGA":
                    if x[k:o]!='TAA' and x[k:o]!='TAG' and x[k:o]!='TGA' and x[k:o]!='ATG':                        
                        k+=3
                        o+=3
                        for w in i:
                            if w=='A' or w=='T' or w=='C' or w=='G':
                                return "true"
                            else:
                                return "false"        
                    else:
                        return "false" 
                        
                else:
                    return "false"
            else:
                return "false"
        else:
            return "false"
    else:
        return "false"
o=[]
l=[]   
#check if 3 letters in genes is true(gene is true) it continue to translate each 3 codons to a letter:   
for i in z:
    l=[]
    if hello(i)=="true":
        for b in range (0,len(i),3):
            l.append(i[b:b+3])
        for j in l:         
            if j=='GCA' or j=='GCC' or j=='GCG' or j=='GCT':
                o.append('A')
            if j=='TGC' or  j=='TGT':
                o.append("C")
            if j=='GAC' or j=='GAT':
                o.append("D")
            if j=='GAA' or j=='GAG':
                o.append("E")
            if j=='TTT' or j=='TTC':
                o.append("F")
            if j=='GGA' or j=='GGC' or j=='GGG' or j=='GGT':
                o.append("G")
            if j=='CAC' or j=='CAT':
                o.append("H")
            if j=='ATA' or j=='ATC' or j=='ATT':
                o.append("I")
            if j=='AAA' or j=='AAG':
                o.append("K")
            if j=='CTA' or j=='CTC' or j=='CTG' or j=='CTT' or j=='TTA' or j=='TTG':
                o.append("L")
            if j=='AAC' or  j=='AAT':
                o.append('N')
            if j=='CCA' or j=='CCC' or j=='CCG' or j=='CCT':
                o.append('P')
            if j=='CAA' or j=='CAG':
                o.append('Q') 
            if j=='ATG':
                o.append('M')
            if j=='AGA'or j=='AGG' or j=='CGA' or j=='CGC' or j=='CGG' or j=='CGT':
                o.append("R")
            if j=='AGC' or j=='AGT' or j=='TCA' or j=='TCC' or j=='TCG' or j=='TCT':
                o.append('S')
            if j=='ACA' or j=='ACC' or j=='ACG' or j=='ACT' :
                o.append('T')
            if j=='GTA' or j=='GTC' or j=='GTG' or j=='GTT' :
                o.append('V')
            if j=='TGG':
                o.append('V')
            if j=='TAC' or j=='TAT':
                o.append('Y')
            if j=='TAA' or j=='TAG' or j=='TGA':
                o.append('\n')                
    else:
        o.append('illegal gene'+'\n')
#it joins the letters to a word and adds the wl(codons translate)to the txt proteins
wl=(''.join(o))  
x2=open('proteins.txt','w')
x2.write(wl)
x2.close()

       