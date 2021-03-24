dna = input("Enter DNA sequence: ")

# making a list out of nucleotides in dna_list.
dna_list = []      # Defining DNA list.
for nt in dna:
    dna_list.append(nt)

rna_list = []  # Defining RNA list.


# Reverse-Complement
def reverse_complement(dna_list):
    complement_list = []
    rev_comp_list = []
    for nt in dna_list:
        if nt == "A":
            complement_list.append("T")
        elif nt == "T":
            complement_list.append("A")
        elif nt == "U":
            complement_list.append("A")
        elif nt == "G":
            complement_list.append("C")
        elif nt == "C":
            complement_list.append("G")
        elif nt == "Y":
            complement_list.append("R")
        elif nt == "R":
            complement_list.append("Y")
        elif nt == "S":
            complement_list.append("S")
        elif nt == "W":
            complement_list.append("W")
        elif nt == "K":
            complement_list.append("M")
        elif nt == "M":
            complement_list.append("K")
        elif nt == "B":
            complement_list.append("V")
        elif nt == "D":
            complement_list.append("H")
        elif nt == "H":
            complement_list.append("D")
        elif nt == "V":
            complement_list.append("B")
        elif nt == "N":
            complement_list.append("N")

        rev_comp_list = complement_list[::-1]
    return rev_comp_list


dna_list_1 = dna_list
dna_list_2 = reverse_complement(dna_list)


# Now, codons

codon_list_1 = []               # For codon +1
codon_list_2 = []               # For codon +2
codon_list_3 = []               # For codon +3
# Reverse wale
codon_list_4 = []               # For codon -1
codon_list_5 = []               # For codon -2
codon_list_6 = []               # For codon -3

for i in range(0, len(dna_list_1), 3):
    codon = tuple(dna_list_1[i:i+3])
    codon_list_1.append(codon)

for i in range(1, len(dna_list_1), 3):
    codon = tuple(dna_list_1[i:i+3])
    codon_list_2.append(codon)

for i in range(2, len(dna_list_1), 3):
    codon = tuple(dna_list_1[i:i+3])
    codon_list_3.append(codon)

for i in range(0, len(dna_list_2), 3):
    codon = tuple(dna_list_2[i:i+3])
    codon_list_4.append(codon)

for i in range(1, len(dna_list_2), 3):
    codon = tuple(dna_list_2[i:i+3])
    codon_list_5.append(codon)

for i in range(2, len(dna_list_2), 3):
    codon = tuple(dna_list_2[i:i+3])
    codon_list_6.append(codon)

codon_list_ki_list = [codon_list_1, codon_list_2, codon_list_3, codon_list_4, codon_list_5, codon_list_6]


# Function for converting codons into their protein.

def codon_to_protein(codon_list):
    protein_list = []
    is_repeatable = True
    protein_string_orf_list = []



    is_start = False   # Checks if Start codon is presenst.
    is_stop = False    # Checks if Stop codon is present.

    for codon in codon_list:
        if codon == ("T", "T", "T") or codon == ("T", "T", "C"):
            protein_list.append("F")
        elif codon == ("T", "T", "A") or codon == ("T", "T", "G"):
            protein_list.append("L")
        elif codon == ("T", "C", "T") or codon == ("T", "C", "C") or codon == ("T", "C", "A") or codon == ("T", "C", "G"):
            protein_list.append("S")
        elif codon == ("T", "A", "T") or codon == ("T", "A", "C"):
            protein_list.append("Y")
        elif codon == ("T", "G", "T") or codon == ('T', 'G', 'C'):
            protein_list.append("C")
        elif codon == ('T', 'G', 'G'):
            protein_list.append("W")
        elif codon == ('C', 'T', 'T') or codon == ('C', 'T', 'C') or codon == ('C', 'T', 'G') or codon == ('C', 'T', 'A'):
            protein_list.append("L")
        elif codon == ('C', 'C', 'C') or codon == ('C', 'C', 'T') or codon == ('C', 'C', 'G') or codon == ('C', 'C', 'A'):
            protein_list.append("P")
        elif codon == ('C', 'A', 'T') or codon == ('C', 'A', 'C'):
            protein_list.append("H")
        elif codon == ('C', 'A', 'A') or codon == ('C', 'A', 'G'):
            protein_list.append("Q")
        elif codon == ('C', 'G', 'T') or codon == ('C', 'G', 'G') or codon == ('C', 'G', 'C') or codon == ('C', 'G', 'A'):
            protein_list.append("R")
        elif codon == ('A', 'T', 'G'):
            protein_list.append("___start___M")
        elif codon == ('A', 'T', 'T') or codon == ('A', 'T', 'C') or codon == ('A', 'T', 'A'):
            protein_list.append("I")
        elif codon == ('A', 'C', 'T') or codon == ('A', 'C', 'G') or codon ==  ('A', 'C', 'A') or codon ==  ('A', 'C', 'C'):
            protein_list.append("T")
        elif codon == ('A', 'A', 'T') or codon == ('A', 'A', 'C'):
            protein_list.append("N")
        elif codon == ('A', 'A', 'A') or codon == ('A', 'A', 'G'):
            protein_list.append("K")
        elif codon == ('A', 'G', 'T') or codon == ('A', 'G', 'C'):
            protein_list.append("S")
        elif codon == ('A', 'G', 'A') or codon == ('A', 'G', 'G'):
            protein_list.append("R")
        elif codon == ('G', 'C', 'T') or codon == ('G', 'C', 'G') or codon == ('G', 'C', 'A') or codon == ('G', 'C', 'C'):
            protein_list.append("A")
        elif codon == ('G', 'T', 'T') or codon == ('G', 'T', 'C') or codon == ('G', 'T', 'G') or codon == ('G', 'T', 'A'):
            protein_list.append("V")
        elif codon == ('G', 'A', 'T') or codon == ('G', 'A', 'C'):
            protein_list.append("D")
        elif codon == ('G', 'A', 'A') or codon == ('G', 'A', 'G'):
            protein_list.append("E")
        elif codon == ('G', 'G', 'G') or codon == ('G', 'G', 'C') or codon == ('G', 'G', 'A') or codon == ('G', 'G', 'T'):
            protein_list.append("G")
        elif codon == ('T', 'G', 'A') or codon == ('T', 'A', 'G') or codon == ('T', 'A', 'A'):
            protein_list.append("___stop___")


    protein_string = "".join(aa for aa in protein_list)

    while is_repeatable == True:
        if "___start___" in protein_string:
            first_start_codon = protein_string.index("___start___")
            protein_string = protein_string[first_start_codon:]
            if "___stop___" in protein_string:
                first_stop_codon = protein_string.index("___stop___")
                protein_string_orf = protein_string[11:first_stop_codon]
                protein_string_orf_list.append(protein_string_orf)
                #print("\n\tandar wale loop me hu")
                protein_string = protein_string[first_stop_codon + 10:]
                #return (protein_string_orf_list)
                continue                            # Agar 6 me se har ek ke sare orf chahye to chontinue yaha aana chahiye (i.e. andar wale if *me*).


        #for orf in protein_string_orf_list:
            #print( orf)
        return (protein_string_orf_list)            # Agar har 6 ke chahiye to return yaha aana chahiye (i.e. bahar waleif ke _else_ wali jagah).


# Driver code

for any_codon_list in codon_list_ki_list:
    orf_list = codon_to_protein(any_codon_list)
    for orf in orf_list:
        # Save output in file
        output_file = open("output.txt", "a")       # Note: add location of your choice
        output_file.write(orf)
        output_file.write("\n")

        # print result
        print(orf)
