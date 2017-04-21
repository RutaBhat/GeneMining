from bs4 import BeautifulSoup
#using bs4 because it is so far the best parsing module available amongst others to find various tags with html document
import enchant 
# cant use urllib because ncbi blocked it so cant use that to get the html version of the article so need newspaper module
import newspaper# used to parse the document and get it into html format
from newspaper import Article
import re
import string
from Bio import Entrez #needed to check genes against Entrez Database
import csv #needed to output the reuslts into a csv format
from MemberGene import Gene #gene class file


# Gene Link
# https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=gene&term=Ott%5BGene%20Name%5D
# https://www.ncbi.nlm.nih.gov/taxonomy/?term=human&report=taxid&format=text


def getTaxonId(organismName):
	if ' ' in organismName:
		organismName.replace(' ', '%20')
	url = "https://www.ncbi.nlm.nih.gov/taxonomy/?term=" + organismName + "&report=taxid&format=text"
	taxonId = Article(url, language='en')
	taxonId.download()
	taxonId = BeautifulSoup(taxonId.html)
	taxonId = taxonId.find('pre').getText()
	return taxonId


def searchForArticleGivenGeneName(query):
	'''Given gene Name as query it will return the list of relevant article Id's which have the gene.
	'''

	Entrez.email = 'rutabhat05@gmail.com'
	handle = Entrez.esearch(db = 'pmc',
							sort = 'relevance',
							retmax = '20',
							retmode = 'xml',
							term = 'query')
	results = Entrez.read(handle)
	return results

# articleIdList = search('ABO')
# print(articleIdList['IdList'])
def search(query):
	'''Given gene name as query it will return the list of geneId's associated with that gene name.
	'''
	Entrez.email = 'rutabhat05@gmail.com'
	handle = Entrez.esearch(db = 'gene', 
							sort = 'relevance',
							retmax = '20', 
							retmode = 'xml', 
							term = query + '[Gene Name]')
	results = Entrez.read(handle)
	return results

def getGeneIDFromEntrez(geneList):
	'''Given a gene list it will check each word in gene list with entrez database and will return a 
		dictionary with all the genes and the gene Id's associated with that gene name.
	'''
	tempDict = dict()
	for gene in geneList:
		res = search(gene)
		if "IdList" in list(res) and len(res['IdList']) > 0:
			tempDict[gene] = res['IdList']

	return tempDict

def downloadArticle(PMCID):
	'''This will download the article and convert it to html based on the given pmc id.
	'''
	url = 'https://www.ncbi.nlm.nih.gov/pmc/articles/PMC' + str(PMCID) + "/"
	a = Article(url, language='en')
	a.download()
	article = BeautifulSoup(a.html)
	return article

def makeGeneListFromArticle(article):
	''' This function will get all the italicized words from the given html article as they could be genes and will return a gene list.
	'''
	geneList = []
	italicsList = article.findAll('em',text = True)
	for word in italicsList:
		encodedString = word.text.encode("utf-8")
		if "\\" not in encodedString.encode('string-escape') and "/" not in encodedString and '(' not in encodedString and ')' not in encodedString:
			geneList.append(encodedString)

	return list(set(geneList))

def getGeneDesc(geneID):
	'''This will take the gene ID of a particular gene and will return the description associated with that gene (summary which is present in NCBI gene database).
	'''
	url = "https://www.ncbi.nlm.nih.gov/gene/?term=" + str(geneID)
	a = Article(url, language='en')
	a.download()
	article = BeautifulSoup(a.html)
	# article.find('div',{"id" : "summaryDiv"})
	article = article.select('div#summaryDiv')
	article = article[0].text.encode('utf-8')
	articleList = article.split('\n')
	articleTemp = articleList[:]
	geneDesc = dict()

	for word in articleTemp:
		if '' == word:
			articleList.remove(word)
	# print(articleList)
	for i in range(0,len(articleList),2):
		if 'symbol' in articleList[i] or 'Symbol' in articleList[i]:
			geneDesc['GeneSymbol'] = articleList[i+1]
		elif 'description' in articleList[i]:
			geneDesc['GeneDesc'] = articleList[i+1]
		elif 'Primary' in articleList[i]:
			geneDesc['PrimarySource'] = articleList[i+1]
		elif 'Locus' in articleList[i]:
			geneDesc['LocusTag'] = articleList[i+1]
		elif 'type' in articleList[i]:
			geneDesc['GeneType'] = articleList[i+1]
		elif 'RNA' in articleList[i]:
			geneDesc['RNA-Name'] = articleList[i+1]
		elif 'Organism' in articleList[i]:
			geneDesc['Organism'] = articleList[i+1]
		elif 'Lineage' in articleList[i]:
			geneDesc['Lineage'] = articleList[i+1]	
		elif 'known' in articleList[i]:
			geneDesc['AKA'] = articleList[i+1]											

	return Gene(geneDesc)

def scrapeGenesfromPMC(pmcID):


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
gene = getGeneDesc(830834)
print(gene)
organismName = getTaxonId(gene.getOrganism())
print(organismName)
# print sampleText

#_____________________________Output to CSV file ________________________

# somedict = geneDict
# fieldnames = {'Gene Names':"Gene Names",'Entrez Gene ID' : "Entrez Gene ID's"}

# with open('GeneNamesWithTheirIDs.csv','wb') as f:
#     w = csv.writer(f)
#     w.writerow([fieldnames[k] for k in fieldnames])
#     w.writerows(somedict.items())



