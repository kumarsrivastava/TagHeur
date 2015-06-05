#!/usr/bin/python
import csv
import datetime
import os.path
import nltk
from nltk.collocations import *
import re
import tempfile
import shutil


global tagbagFirstFile 
global tagbagSecondFile
print "*	*	*	*	*	*	*"
print "Thank you for choosing the semantic harmonization tool"
print "Let us begin with asking you some questions"
print "First, let's get some information about your first data source"



pathtofile1 = "demo.csv"
pathtofile3 = "demo2.csv"
pathtofile2 = "demo_copy.csv"
tagbagFirstFile = [""]
tagbagSecondFile = [""]


def processfirstfile():

	pathtofile1 = raw_input('Enter the path for your data file ?: ') 
	
	filesource_1 = raw_input('Where did this file come from?: ')
	removearticles(filesource_1)
	toeknizeTags(1, "Source", filesource_1)	
	
	fileparent_1 = raw_input('Which system or process was responsbile for creating this data?: ')
	removearticles(fileparent_1)
	toeknizeTags(1, "Parent", fileparent_1)	
	
	entities_1 = raw_input('what kind of entities does this data set describe ?: ')	
	removearticles(entities_1)
	toeknizeTags(1, "Entity", entities_1)	
	
	events_1 = raw_input('what kind of events does this data set describe ?: ')
	removearticles(events_1)
	toeknizeTags(1, "Entity", events_1)	
	
	application_1 = raw_input('Which application feeds into this data source ?: ')
	removearticles(application_1)
	toeknizeTags(1, "CreatingApplication", application_1)	
	
	consumers_1 = raw_input('Which application consumes this data source ?: ')
	removearticles(consumers_1)
	toeknizeTags(1, "Reader", consumers_1)	
	
	contents_1 = raw_input('Describe the contents of this data source ?: ')
	removearticles(contents_1)
	toeknizeTags(1, "Content", contents_1)
	
	#pathtofile1 = "demo.csv"
	
	
	outFile = open('/Users/Kumar/nltk_data/corpora/genesis/firstfileresponse.txt', 'w')
	outFile.write(fileparent_1 + " " +  entities_1 +  " " + events_1 + " " +  application_1 + " " +  consumers_1 + " " +  contents_1)
	outFile.close()

	responseTags = generateTags('/Users/Kumar/nltk_data/corpora/genesis/firstfileresponse.txt')
	print "\n"
	print "Tags Generated From User Answers (NLTK Output)"
	print responseTags
	print "\n"
		
	for tags in responseTags:
		tagbagFirstFile.append(tags)
		
	shutil.copy(pathtofile1, '/Users/Kumar/nltk_data/corpora/genesis/temp.csv')
		
	responseTags = generateTags('/Users/Kumar/nltk_data/corpora/genesis/temp.csv')
	print "\n"
	print "Tags Generated From Treating the Data File as a Document (NLTK Output)"
	print responseTags
	print "\n"
	
	for tags in responseTags:
		tagbagFirstFile.append(tags)
	
	count = 0
	isDate = False
	isNum = False
	headers = ""
	firstfile = open(pathtofile1, 'rb')
	try:
		namefile = os.path.basename(pathtofile1)
		tagbagFirstFile.append(namefile)
	except:
		print "unable to read filename"
		
	print "Preparing to run light weight inference"
	print "\n"
	
	spamreader = csv.reader(firstfile, delimiter=' ', quotechar='|')
	for row in spamreader:
		if count == 0:
			strs = ', '.join(row)
			headers = strs.split("	")
			for head in headers:
				tagbagFirstFile.append(head)
			count = 1
    		
    	else:
    		strs = ', '.join(row)
    		headers = strs.split("	")
    		for head in headers:
    			try:
    				if isinstance(int(head), (int, long, float, complex)):
    					isNum = True
    					#print "numcheckpassed"
    					
    			except:
    				#print "Numeric Check Failed"
    				isNum = False
    			
    			try:
    				if isinstance(datetime.datetime.strptime(head, '%m/%d/%Y').date(), datetime.date):
    					isDate = True
    					#print "datecheckpassed"
    				
    			except:
    				#print "Date Check Failed"	
    				isDate = False	
    			
    			
    			if isNum == False and isDate == False:
    				tagbagFirstFile.append(head)
    				
    			if isNum == True:
    				tagbagFirstFile.append("HasMeasures")
    				
    				print "Found Measures in the data"
    			if isNum == False:
    				tagbagFirstFile.append("HasDates")
    				print "Found Dates in the data"
				
				isDate = False
				isNum = False
				
    		#print ', '.join(row)
	print "***************Tags*********************"
	print tagbagFirstFile
	print "***************Tags*********************"
	
def processsecondfile():
	count = 0
	headers = ""
	isDate = False
	isNum = False
	
	pathtofile2 = raw_input('Enter the path for your data file ?: ') 
	
	filesource_2 = raw_input('Where did this file come from?: ')
	removearticles(filesource_2)
	toeknizeTags(2, "Source", filesource_2)	
	
	fileparent_2 = raw_input('Which system or process was responsbile for creating this data?: ')
	removearticles(fileparent_2)
	toeknizeTags(2, "Parent", fileparent_2)	
	
	entities_2 = raw_input('what kind of entities does this data set describe ?: ')	
	removearticles(entities_2)
	toeknizeTags(2, "Entity", entities_2)	
	
	events_2 = raw_input('what kind of events does this data set describe ?: ')
	removearticles(events_2)
	toeknizeTags(2, "Entity", events_2)	
	
	application_2 = raw_input('Which application feeds into this data source ?: ')
	removearticles(application_2)
	toeknizeTags(2, "CreatingApplication", application_2)	
	
	consumers_2 = raw_input('Which application consumes this data source ?: ')
	removearticles(consumers_2)
	toeknizeTags(2, "Reader", consumers_2)	
	
	contents_2 = raw_input('Describe the contents of this data source ?: ')
	removearticles(contents_2)
	toeknizeTags(2, "Content", contents_2)
	
	outFile = open('/Users/Kumar/nltk_data/corpora/genesis/secondfileresponse.txt', 'w')
	outFile.write(fileparent_2 + " " +  entities_2 +  " " + events_2 + " " +  application_2 + " " +  consumers_2 + " " +  contents_2)
	outFile.close()

	responseTags = generateTags('/Users/Kumar/nltk_data/corpora/genesis/secondfileresponse.txt')
	for tags in responseTags:
		tagbagSecondFile.append(tags)
	
	print "\n"
	print "Tags Generated From User Answers (NLTK Output)"
	print "\n"
	print responseTags
		
	shutil.copy(pathtofile2, '/Users/Kumar/nltk_data/corpora/genesis/temp.csv')
		
	responseTags = generateTags('/Users/Kumar/nltk_data/corpora/genesis/temp.csv')
	print "\n"
	print "Tags Generated From Treating the Data File as a Document (NLTK Output)"
	print "\n"
	print responseTags
	
	for tags in responseTags:
		tagbagSecondFile.append(tags)
	
	firstfile = open(pathtofile2, 'rb')
	try:
		namefile = os.path.basename(pathtofile2)
		tagbagSecondFile.append(namefile)
	except:
		print "unable to read filename"
	spamreader = csv.reader(firstfile, delimiter=' ', quotechar='|')
	
	print "Preparing to run light weight inference"
	print "\n"

	for row in spamreader:
		if count == 0:
			strs = ', '.join(row)
			headers = strs.split("	")
			for head in headers:
				tagbagSecondFile.append(head)
			count = 1
    		
    	else:
    		strs = ', '.join(row)
    		headers = strs.split("	")
    		for head in headers:
    			try:
    				if isinstance(int(head), (int, long, float, complex)):
    					isNum = True
    					#print "numcheckpassed"
    					
    			except:
    				#print "Numeric Check Failed"
    				isNum = False
    			
    			try:
    				if isinstance(datetime.datetime.strptime(head, '%m/%d/%Y').date(), datetime.date):
    					isDate = True
    					#print "datecheckpassed"
    				
    			except:
    				#print "Date Check Failed"	
    				isDate = False	
    			
    			
    			if isNum == False and isDate == False:
    				tagbagSecondFile.append(head)
    				
    			if isNum == True:
    				tagbagSecondFile.append("HasMeasures")
    				print "Found Measures in the data"
    			if isNum == False:
    				tagbagSecondFile.append("HasDates")
    				print "Found Dates in the data"
				
				isDate = False
				isNum = False
				
    		#print ', '.join(row)
    		
	print "***************Tags*********************"
	print tagbagSecondFile
	print "***************Tags*********************"


def harmonizeOnTags():
	
	intersectionList = set(tagbagSecondFile).intersection(tagbagFirstFile)
	
	print "*********************************************"
	if len(intersectionList) > 0.75*len(tagbagFirstFile) and len(intersectionList) > 0.75*len(tagbagSecondFile):
		print "HARMONIZATION SCORE: These data sets are very similar"
	elif len(intersectionList) > 0.50 *len(tagbagFirstFile) and len(intersectionList) > 0.50*len(tagbagSecondFile):
		print "HARMONIZATION SCORE: These data sets are somewhat similar"
	elif len(intersectionList) > 0.25*len(tagbagFirstFile) and len(intersectionList) > 0.25*len(tagbagSecondFile):
		print "HARMONIZATION SCORE: These data sets are slightly similar"
	else:
		print "HARMONIZATION SCORE: Not many similarities found in these data sets"
	print "*********************************************"
	
	print "Found the following matching tags"
	for tag in intersectionList:
		print tag
		
	print "*********************************************"
		
def generateTags(text):
	bigram_measures = nltk.collocations.BigramAssocMeasures()

	# change this to read in your data
	finder = BigramCollocationFinder.from_words(
	nltk.corpus.genesis.words(text))

	# only bigrams that appear 3+ times
	finder.apply_freq_filter(3) 
	
	# return the 5 n-grams with the highest PMI
	return finder.nbest(bigram_measures.pmi, 5)  

def removearticles(text):
	re.sub('\s+(a|an|and|the|to|from|if|)(\s+)', '\2', text)
  
def toeknizeTags(file, question, text):
	tagssplit = text.split(' ')
	for tags in tagssplit:
		newtag = question+ '_' + tags
		if file == 1:
			tagbagFirstFile.append(newtag)
		else:
			tagbagSecondFile.append(newtag)


def verifyTags(source):
	acceptAll = raw_input('Type Yes to Accept All Tags As Is: ')
	if acceptAll.lower() != "yes":
	
		if source == 1:
			for tags in tagbagFirstFile:
				tagverdict = raw_input('Type Yes to Accept or type to edit: ' + tags + ": ")
				if tagverdict.lower() == "yes":
					print "Verdict Recorded"
				else:
					tagbagFirstFile.append(tagverdict)
					tagbagFirstFile.remove(tags)
		else:
			for tags in tagbagSecondFile:
				tagverdict2 = raw_input('Type Yes to Accept or type to edit: ' + tags + ": ")
				if tagverdict2.lower() == "yes":
					print "Tag Verdict Recorded"
				else:
					print "Updated Tag Recorded"
					tagbagSecondFile.append(tagverdict2)
					tagbagSecondFile.remove(tags)
	
			
		
		
processfirstfile()
verifyTags(1)
processsecondfile()
verifyTags(2)
harmonizeOnTags()

