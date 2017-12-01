kmers = {}
text = "ACGCATGTTAACAACACTATTCCTCAGTGCGTAGTCCCAGACGGTACAACAACACTAAACAACACTATTCCTCAGTGTTCCTCAGTGACGCATGTTAACAACACTACGTAGTCCCAGACGGTACAACAACACTAACGCATGTTAACAACACTAGACGGTACAACAACACTATTCCTCAGTGACGCATGTTGACGGTACAACAACACTAACGCATGTTAACAACACTAAACAACACTAACGCATGTTGACGGTACCGTAGTCCCAGACGGTACCGTAGTCCCAACGCATGTTCGTAGTCCCAACGCATGTTTTCCTCAGTGGACGGTACAACAACACTACGTAGTCCCAGACGGTACGACGGTACACGCATGTTAACAACACTATTCCTCAGTGAACAACACTACGTAGTCCCAACGCATGTTACGCATGTTCGTAGTCCCATTCCTCAGTGCGTAGTCCCAACGCATGTTACGCATGTTCGTAGTCCCAAACAACACTACGTAGTCCCAGACGGTACGACGGTACTTCCTCAGTGTTCCTCAGTGAACAACACTAGACGGTACGACGGTACAACAACACTAGACGGTACTTCCTCAGTGTTCCTCAGTGAACAACACTACGTAGTCCCATTCCTCAGTGCGTAGTCCCACGTAGTCCCACGTAGTCCCAAACAACACTATTCCTCAGTGGACGGTACTTCCTCAGTGAACAACACTAACGCATGTTACGCATGTTTTCCTCAGTGGACGGTACCGTAGTCCCAGACGGTACCGTAGTCCCAGACGGTACTTCCTCAGTGGACGGTACACGCATGTTGACGGTACCGTAGTCCCACGTAGTCCCAGACGGTACGACGGTACGACGGTACGACGGTACGACGGTACCGTAGTCCCATTCCTCAGTGAACAACACTAAACAACACTATTCCTCAGTGGACGGTACTTCCTCAGTG"
k = 11

for i in range(len(text)-k+1):
	pattern = text[i:i+k]
	if pattern in kmers.keys():
		kmers[pattern] += 1
	else:
		kmers[pattern] = 1

printMax = ""
max = 0
for p,v in kmers.items():
	if v > max:
		printMax = p
		max = v
	else:
		if v == max:
			printMax += " " + p
print(printMax)