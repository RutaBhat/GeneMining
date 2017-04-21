from ArticleGenes import ArticleGenes
from ExtractGeneHelpers import *

# Gene Link
# https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=gene&term=Ott%5BGene%20Name%5D
# https://www.ncbi.nlm.nih.gov/taxonomy/?term=human&report=taxid&format=text


def geneDictFromPMCID(pmcID):
	article = downloadArticle(pmcID)
	title = getTitleFromArticle(article)
	geneList = makeGeneListFromArticle(article)
	geneDict = getGeneIDFromEntrez(geneList)
	return [pmcID, title, geneDict]


#----------------------- Main Code -----------------------------------

# pmcID = 3068686   #5117602
# article = downloadArticle(pmcID)
# geneList = makeGeneListFromArticle(article)
# print "Original Gene List - " + str(len(geneList)) + " genes - " + str(geneList)
# print " "
# print "Getting Gene List..."
# print " " 
# geneDict = getGeneIDFromEntrez(geneList)

# print "Gene List After Entrez Search - " + str(len(geneDict)) + " genes - " + str(geneDict)
# print " "
# print "arg-5 Gene ID List" + str(geneDict['arg-5'])
# gene = getGeneDesc(830834)
# print(gene)
# organismName = getTaxonId(gene.getOrganism())
# print(organismName)
# print sampleText

[pmcID, title, geneDict] = geneDictFromPMCID(3068686)
totalGenes = ArticleGenes(pmcID, title, geneDict)
print("Article Gene Object - " + "\n" + str(totalGenes))

#_____________________________Output to CSV file ________________________

# somedict = geneDict
# fieldnames = {'Gene Names':"Gene Names",'Entrez Gene ID' : "Entrez Gene ID's"}

# with open('GeneNamesWithTheirIDs.csv','wb') as f:
#     w = csv.writer(f)
#     w.writerow([fieldnames[k] for k in fieldnames])
#     w.writerows(somedict.items())



