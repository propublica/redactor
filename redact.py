import re

from tqdm import tqdm
from stanfordcorenlp import StanfordCoreNLP


def remove_phone_numbers(string):
    result = re.sub(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})', '<PHONE>', string)
    return result

def remove_email_addresses(string):
	result = re.sub(r'[\w\.-]+@[\w\.-]+', '<EMAIL>', string) 
	return result

def remove_persons(string):
	nlp = StanfordCoreNLP('http://localhost', port=9000)
	print('Beginning redaction using Stanford package.')
	person_count = 0

	for ent in nlp.ner(string):
		if ent[1] == 'PERSON':
			string = string.replace(ent[0], '<PERSON>')

	end_time = datetime.datetime.now()
	time = end_time - start_time
	print('Stanford: Found %d persons' %person_count)
	print('Took %s time.' %str(end_time - start_time))

	nlp_stan.close()
	return data_list

