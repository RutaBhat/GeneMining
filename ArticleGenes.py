from Gene import Gene

class ArticleGenes(object):

	def __init__(self, pmcID, title, geneDict):
		self.pmcID = pmcID
		self.title = title
		self.geneList = []
		for key in geneDict:
			gene = Gene(key,geneDict[key])
			print(gene)
			self.geneList.append(gene)

	def getArticleTitle(self):
		return self.title

	def getPMCID(self):
		return self.pmcID

	def getGeneList(self):
		return self.geneList

	def __str__(self):
		return "------ Article - " + self.title + " -------------" + "\n" \
				+ "PMC ID - " + str(self.pmcID) + "\n" \
				+ "GeneList - " + str(self.geneList) + "\n" \
				+ "-----------------------------------------------" \
