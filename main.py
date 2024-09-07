# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


rna_dict = {'G': 'C', 'T': 'A', 'C': 'G', 'A': 'U'}

dna_nucleotides = ('A', 'C', 'G', 'T')

rna_out = []

count_A = 0
count_T = 0
count_C = 0
count_G = 0


def read_dna_seq():
    with open(r"C:\Users\Shery\OneDrive\Documents\Alu-1.txt", encoding="utf-8") as f:
        read_dna = str(f.read())
    return read_dna


def transcribe_dna(dna_seq):
    try:
        for i in dna_seq:
            if i in dna_nucleotides:
                rna_out.append(rna_dict.get(i))
                nucleotide_densities(i)
        return print("Success!\n")
    except Exception as e:
        return print(f"Error: {e}\n")


def nucleotide_densities(nucleotide):
    global count_A, count_T, count_C, count_G
    match nucleotide:
        case 'A':
            count_A += 1
        case 'T':
            count_T += 1
        case 'C':
            count_C += 1
        case 'G':
            count_G += 1
        case _:
            return "Error!\n"


def main():
    transcribe_dna(read_dna_seq())
    print("DNA Nucleotide Densities: A={0}, T={1}, C={2}, G={3} \n".format(count_A, count_T, count_C, count_G))
    print("RNA Output: " + ''.join(rna_out))



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
