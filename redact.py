# -*- coding: utf-8 -*-

import re
from stanfordcorenlp import StanfordCoreNLP

nlp = StanfordCoreNLP('http://localhost', port=9000)

'''From https://github.com/acrosson/nlp/blob/master/information-extraction.py'''
def remove_phone_numbers(string):
    result = re.sub(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})', lambda x: u'█'*len(x.group()), string)
    return result

'''From https://github.com/acrosson/nlp/blob/master/information-extraction.py'''
def remove_email_addresses(string):
	result = re.sub(r'[\w\.-]+@[\w\.-]+', lambda x: u'█'*len(x.group()), string) 
	return result

def remove_persons(string, skip_redaction=('trump', 'putin', 'beto', 'o\'rourke', 'denton', 'metzger', 'kemp')):
	person_count = 0

	for ent in nlp.ner(string):
		if ent[1] == 'PERSON' and ent[0].lower() not in skip_redaction:
			string = string.replace(ent[0], u'█'*len(ent[0]))
	return string
