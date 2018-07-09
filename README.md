# redactor
Tool to remove email addresses, person entities, and phone numbers

## Installation
1. `git clone https://github.com/propublica/redactor.git && cd redactor`
2. Make virtualenv (`conda create --name <env> --file spec-file.txt`) or add to virtualenv (`conda install --file spec-file.txt`)
3. Install python wrapper to [Stanford CoreNLP](https://github.com/stanfordnlp/CoreNLP)
  
### Remove phone numbers
```
from redact import remove_phone_numbers

w_numbers = "My phone number is 123-456-7890"
no_numbers = remove_phone_numbers(string_w_numbers)
print(no_numbers) // "My phone number is <PHONE>"
```

### Remove email addresses

```
from redact import remove_email_addresses

w_email = "My email is name@propublica.org"
no_email = remove_email_addresses(w_email)
print(w_email) // "My email is <EMAIL>"
```

### Remove names of people

1. From terminal, `cd stanfordcorenlp && java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 15000` as per [the stanfordcorenlp readme](https://github.com/stanfordnlp/CoreNLP)
2. Run your program that uses `remove_persons`, e.g.:
```
from redact import remove_persons

w_people = "Adam is going to school today"
no_people = remove_persons(w_people)
print(w_email) // "<PERSON> is going to school today"
```
Note: avoid calling `remove_persons` in a for-loop since this would start and close the CoreNLP server each iteration. If you wish to use it in a for-loop take a look at [stanfordcorenlp](https://github.com/stanfordnlp/CoreNLP) and adjust to your data's structure. 
