class MemberGene(object):

	def __init__(self,geneDict):
		self.geneSymbol = geneDict['GeneSymbol'] if 'GeneSymbol' in geneDict else 'None'
		self.geneDesc = geneDict['GeneDesc'] if 'GeneDesc' in geneDict else 'None'
		self.primarySource = geneDict['PrimarySource'] if 'PrimarySource' in geneDict else 'None'
		self.locusTag = geneDict['LocusTag'] if 'LocusTag' in geneDict else 'None'
		self.geneType = geneDict['GeneType'] if 'GeneType' in geneDict else 'None'
		self.rnaName = geneDict['RNA-Name'] if 'RNA-Name' in geneDict else 'None'
		self.organism = geneDict['Organism'] if 'Organism' in geneDict else 'None'
		self.lineage = geneDict['Lineage'] if 'Lineage' in geneDict else 'None'
		self.aka = geneDict['AKA'] if 'AKA' in geneDict else 'None'		

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


	