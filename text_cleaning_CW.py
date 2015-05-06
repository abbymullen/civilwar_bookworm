import re
import json
import warnings
import uuid
import dateutil.parser
from datetime import *
DEFAULT = datetime(1798,1,1)



def snippetyielder(filename):
	"""
	This function takes a text file with many small documents in it, and returns those documents broken out into 
	individual units. I used the citation at the end of each document as the breaking point. I had to use a custom
	break because the OCR of the text file incorporates almost every non-printing character in its read."""
	text = open(filename, "r")
	a = text.readlines()
	p = "".join(a) 	  #detecting the breaks between documents and identifying them to break the docs with


	docbreak = re.sub(r".*([1\?RU]+[ce][j~p]+o[rtd\*]+ .[2Jf].*)",r"DOCBREAK \1",p)
	docbreak = re.sub(r"(.*[lL]ett.*fro[mn].*)",r"DOCBREAK \1",docbreak)
	docbreak = re.sub(r".*(Petition .f.*)",r"DOCBREAK \1",docbreak)
	docbreak = re.sub(r".*(Order o[/f].*)",r"DOCBREAK \1",docbreak)
	docbreak = re.sub(r".*(General order of.*)",r"DOCBREAK \1",docbreak)
	docbreak = re.sub(r".*(Special order of.*)",r"DOCBREAK \1",docbreak)
	docbreak = re.sub(r".*(Unofficial letter of.*)",r"DOCBREAK \1",docbreak)
	docbreak = re.sub(r".*(Letter of .*)",r"DOCBREAK \1",docbreak)
	docbreak = re.sub(r".*([\[I\]]\s*T[cue]legram.*)",r"DOCBREAK \1",docbreak)
	docbreak = re.sub(r".*(\[Enclosure.+\].*)",r"DOCBREAK \1",docbreak)
	docbreak = re.sub(r".*(Extracts* from .*)",r"DOCBREAK \1",docbreak)
	docbreak = re.sub(r".*(A[hb]stract[of ]*log.*)",r"DOCBREAK \1",docbreak)
	docbreak = re.sub(r".*(Instructions from.*)",r"DOCBREAK \1",docbreak)
	docbreak = re.sub(r".*(A[hb]stract of statement.*)",r"DOCBREAK \1",docbreak)
	docbreak = re.sub(r".*(Instructions* of.*)",r"DOCBREAK \1",docbreak)
	docbreak = re.sub(r".*(Memorandum from.*)",r"DOCBREAK \1",docbreak)
	docbreak = re.sub(r".*([llifM]+emorandum of.*)",r"DOCBREAK \1",docbreak)
	docbreak = re.sub(r".*(Communication from.*)",r"DOCBREAK \1",docbreak)
	docbreak = re.sub(r".*(Statement of circumstances.*)",r"DOCBREAK \1",docbreak)
	docbreak = re.sub(r".*(Further report of.*)",r"DOCBREAK \1",docbreak)
	docbreak = re.sub(r".*(Second report of.*)",r"DOCBREAK \1",docbreak)
	docbreak = re.sub(r".*(Additional report of.*)",r"DOCBREAK \1",docbreak)
	docbreak = re.sub(r".*(Detailed repor[~t] of.*)",r"DOCBREAK \1",docbreak)
	docbreak = re.sub(r".*(General report of.*)",r"DOCBREAK \1",docbreak)
	docbreak = re.sub(r".*(Deposition of.*)",r"DOCBREAK \1",docbreak)
	# docbreak = re.sub(r"(DOCBREAK)+",r"DOCBREAK\n",docbreak) 	
	docbreaks = docbreak.split("DOCBREAK") 	  #yielding one document at a time
	for doc in docbreaks:
		if re.search(r".+",doc): 	
			yield doc 	

class Regexdate():
 	def __init__(self,string):
		self.string = string 
 	"""  Initialized with a portion of a string suspected to contain a date. 	 	 	 
 	""" 	 	 	   

	def find_year(self): 	
		"""
		Pulls out a year without recourse to datetime and corrects small OCR problems
		""" 	 	 
	 	year = re.search(r"[I1][\dG]{3}",self.string)
	 	if year: 	 	 	  
	 		if re.search(r"(\d{4})",year.group()):
	 			return year.group()
	 		if re.search(r"I\d{3}",year.group()):
	 			year = re.sub(r"I(\d{3})",r"1\1",year.group())
	 			return year
	 		if re.search(r"(\d[G\d]{3})",year.group()):
	 			year = re.sub(r"G",r"6",year.group())
	 			return year

	 	return "Unknown" 	 	 	  

	def find_month(self):
	 	month = re.search(r"([A-Z][A-Za-z]+)\s*\d{1,2},*\s*[I1][\dG]{3}",self.string)
	 	if month:
	 		month = month.group(1)
		 	if re.search(r"J[AaNn].*",month):
		 		return "01"
		 	if re.search(r"F[EBeb].*",month):
		 		return "02"
		 	if re.search(r"M[ARar].*",month):
		 		return "03"
		 	if re.search(r"A[PRpr].*",month):
		 		return "04"
		 	if re.search(r"M[AYay].*",month):
		 		return "05"
		 	if re.search(r"J[UNun].*",month):
		 		return "06"
		 	if re.search(r"J[ULul].*",month):
		 		return "07"
		 	if re.search(r"A[Uun].*",month):
		 		return "08"
		 	if re.search(r"S[Ee].*",month):
		 		return "09"
		 	if re.search(r"O[Cc].*",month):
		 		return "10"
		 	if re.search(r"N[Oo].*",month):
		 		return "11"
		 	if re.search(r"D[Ee].*",month):
		 		return "12"
		 	return month
		return ""

	def find_day(self):
		day = re.search(r"([A-Z][A-Za-z]+)\s*(\d{1,2}),*\s*[I1][\dG]{3}",self.string)
		if day:
			day = day.group(2)
			return day
		return ""

#defining a class to pull out stuff from the snippets
class Document():
	def __init__(self, doc):
		self.doc = doc

	def test(self):
		return self.doc + 'BREAK\n'

	def raw_text(self): 
		"""
		This takes a string (a document) and returns a string clean of all headers and citations
		"""
		
		 #eliminating more headers
		raw_text = re.sub(r".*OPERATIONS O[PF].*",r"",self.doc)
		raw_text = re.sub(r"Page \d+",r"",raw_text)
		raw_text = re.sub(r".*B[lL]OCK.*",r"",raw_text)
		raw_text = re.sub(r".*WEST GULF.*",r"",raw_text)
		raw_text = re.sub(r".*NAVAL FORCES ON.*",r"",raw_text)
		raw_text = re.sub(r"\s",r" ", raw_text) #eliminating tabs etc. 	 	  
		return raw_text
	

	def get_date(self):
		"""
		Right now this takes a string and returns a year; hopefully someday it will return a more specific date.
		"""
		head = self.raw_text()[:300] 	 	 
		parser = Regexdate(head) 	 		
		year = parser.find_year()		
		month = parser.find_month()
		day = parser.find_day()
		if day:
			return year + "-" + month + "-" + day	
		if year:
			return year
		return "Unknown"

	def author(self):
		"""
		Takes a string--the first bit of the document--and returns the author
		Accomplishes this through extracting data from formulaic headings on documents
		Tries to account for non-letter documents such as daily journal entries
		"""
		author = re.search(r"([Ff]rom\s)(.+) ([tT]\s*o)([^,]+),",self.raw_text()[:150])
		report = re.search(r".*[Rr]eport of ([^,]+),",self.raw_text()[:150])
		order = re.search(r".*[Oo]rder of ([^,]+)[,.]* to",self.raw_text()[:250])
		order2 = re.search(r".*[Oo]rder of ([^,]+),",self.raw_text()[:250])
		logbook = re.search(r".*[lL]og of ([^,]+)[,.]",self.raw_text()[:250])
		if order:
			order = order.group(1)
			return order
		if order2:
			order2 = order2.group(1)
			return order2
		if logbook:
			logbook = logbook.group(1)
			return logbook
		if report:
			report = report.group(1)
			return report
		if author: 	
			author = author.group(2) 
			author = re.sub(r"([^,]*),.*",r"\1",author)	 
			return author
		
		return "Unknown"

	def recipient(self):
		"""
		Takes a string, the first bit of a document, and returns the recipient of the document if there is one
		Tries to account for non-letter documents by recording an alternate "recipient"
		"""
		recipient = re.search(r"([Tt]\s*o )(.*)(from.*)",self.raw_text()[:250])
		
		if recipient: 	
			recipient = recipient.group(2) 	
			recipient = re.sub(r"(\w+\s*\w+),.*",r"\1",recipient) #attempting to clear out titles and such
			# recipient = re.sub(r"([sS]ecre[a-z]+ of the \w+).*","Secretary of the Navy",recipient) 	
			return recipient
		return "Unknown" 		
	
	def id(self): 	
		"""
		randomly generated ID
		""" 	 	 	 
		self.id = uuid.uuid4().hex
		return self.id


	def metadata(self): 	 	 	 	 
		metadata = { 	 	 	 	 	 	 
			"filename":self.id(), 	 	 	 	 	 	 
			"author":self.author(), 	 	 	 	 	 	 
			"recipient":self.recipient() 	 	 	 	 
			}
		return json.dumps(metadata) 	 	 	 	 		

	def does_this_look_suspicious(self):
		pass


if __name__=="__main__":
	f = open("input.txt", "a")
	j = open("jsoncatalog.txt", "a")
	for snippet in snippetyielder("CW_all.txt"):
		doc = Document(snippet)
		# f.write(doc.get_date() + '\t' + doc.raw_text()[:250] + '\n')
		f.write("ID_" + doc.id() + '\t'	+ doc.raw_text() + '\n')
		data = {'searchstring': doc.get_date() + doc.raw_text()
			, 'author': doc.author()
			, 'recipient': doc.recipient()
			, 'date': doc.get_date()
			, 'filename': "ID_" + doc.id
			, 'full_text': doc.raw_text()
		} 
		data_string = json.dumps(data)
		j.write(data_string + '\n')
		
	j.close()
	f.close()
