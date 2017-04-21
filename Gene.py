from MemberGene import MemberGene

class Gene(object):

	def __init__(self, geneName, geneIdList):
		self.geneName = geneName
		self.memberGeneList = []
		for geneID in geneIdList:
			memberGene = MemberGene(int(geneID))
			self.memberGeneList.append(memberGene)

	def getGeneName(self):
		return self.geneName

	def getMemberGenes(self):
		return self.memberGeneList

	def __str__(self):
		memberString = ''
		for member in self.memberGeneList:
			memberString += str(member)
		return "------ Gene - " + self.geneName + " -------------" + "\n" \
				+ "Member Genes - " + "\n" \
				+ memberString + "\n" \
				+ "-----------------------------------------------" \


