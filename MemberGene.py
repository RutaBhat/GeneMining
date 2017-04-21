from ExtractGeneHelpers import getGeneDesc, getTaxonId

class MemberGene(object):

	def __init__(self, geneID):
		geneDescDict = getGeneDesc(geneID)
		if geneDescDict != None:
			self.geneSymbol = geneDescDict['GeneSymbol'] if 'GeneSymbol' in geneDescDict else 'None'
			self.geneDesc = geneDescDict['GeneDesc'] if 'GeneDesc' in geneDescDict else 'None'
			self.primarySource = geneDescDict['PrimarySource'] if 'PrimarySource' in geneDescDict else 'None'
			self.locusTag = geneDescDict['LocusTag'] if 'LocusTag' in geneDescDict else 'None'
			self.geneType = geneDescDict['GeneType'] if 'GeneType' in geneDescDict else 'None'
			self.rnaName = geneDescDict['RNA-Name'] if 'RNA-Name' in geneDescDict else 'None'
			self.organism = geneDescDict['Organism'] if 'Organism' in geneDescDict else 'None'
			self.lineage = geneDescDict['Lineage'] if 'Lineage' in geneDescDict else 'None'
			self.aka = geneDescDict['AKA'] if 'AKA' in geneDescDict else 'None'
			# self.taxonId = getTaxonId(self.organism) if self.organism else 'None'
		else:
			self.geneSymbol = 'None'
			self.geneDesc = 'None'		
			self.primarySource = 'None'
			self.locusTag = 'None'
			self.geneType = 'None'
			self.rnaName = 'None'
			self.organism = 'None'
			self.lineage = 'None'
			self.aka = 'None'
			self.taxonId = 'None'

	def getSymbol(self):
		return self.geneSymbol

	def getDesc(self):
		return self.geneDesc

	def getPrimarySource(self):
		return self.primarySource

	def getLocusTag(self):
		return self.locusTag

	def getType(self):
		return self.geneType

	def getRnaName(self):
		return self.rnaName

	def getOrganism(self):
		return self.organism

	def getLineage(self):
		return self.lineage

	def getAka(self):
		return self.aka

	def getTaxonId(self):
		return self.taxonId

	def __str__(self):
		return "------------- " + self.geneSymbol + " -------------" + "\n" \
				+ "GeneDesc - " + self.geneDesc + "\n" \
				+ "GenePrimarySource - " + self.primarySource + "\n" \
				+ "Locus Tag - " + self.locusTag + "\n" \
				+ "GeneType - " + self.geneType + "\n" \
				+ "RNA Name - " + self.rnaName +  "\n" \
				+ "Organism - " + self.organism +  "\n" \
				+ "Lineage - " + self.lineage +  "\n" \
				+ "AKA - " + self.aka +  "\n" \
				+ "-----------------------------------------------" \



	