def count_nucleotides(string):
    counts = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
    for char in string:
        if char in counts:
            counts[char] += 1
    return counts

def main():
    input_string = input("Enter a DNA sequence: ").upper()
    nucleotide_counts = count_nucleotides(input_string)
    print("Counts of nucleotides:")
    for nucleotide, count in nucleotide_counts.items():
        print(f"{nucleotide}: {count}")

