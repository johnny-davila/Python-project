from Bio import SeqIO
import matplotlib.pyplot as plt

def pattern(fasta, graph):
	ids = []
	seq = []
	TCF = "CTTTGAT"
	pattern = []
	leng = []
	a = SeqIO.parse(fasta, "fasta")
	for i in a:
		if i.seq.find("CTTTGAT")>-1:
			ids.append(i.id)
			seq.append(i.seq)
			x = str(i.seq)
			M = len(x)
			leng.append(M)
			N = x.count(TCF)
			pattern.append(N)
		else:
			pass
	fig = plt.figure()
	plt.scatter(leng, pattern, c="r", alpha=0.5)
	plt.title('Scatter plot')
	plt.xlabel('Length of the coding sequence')
	plt.ylabel('Number of TCF binding sites')
	plt.show()
	fig.savefig(graph)

pattern('HR_CDS.fasta', 'HR.png')
pattern('CT_CDS.fasta', 'CT.png')
pattern('DG_CDS.fasta', 'DG.png')
