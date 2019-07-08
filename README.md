# redactor
Simple tool to remove email addresses, person entities, and phone numbers. Code by [@liliachang](https://github.com/liliachang), light editing by [@schwanksta](https://github.com/schwanksta).

## Installation
1. Make a virtualenv and activate it. Something like: `virtualenv redactor && cd redactor && . bin/activate`
2. Clone the repo. Something like: `git clone https://github.com/propublica/redactor.git && cd redactor`
3. Install the requirements. Something like: `pip install -r requirements.txt`
4. Run Stanford's CoreNLP server if you're going to use the name redactor. This is slow to start, but is fast enough if you keep it running. The fastest way is to run it in a docker container. Handily, there's a repo for it, so you can just run `docker run -p 9000:9000 nlpbox/corenlp`

### Remove phone numbers
```
from redact import remove_phone_numbers

w_numbers = "My phone number is 123-456-7890"
no_numbers = remove_phone_numbers(w_numbers)
print(no_numbers) # "My phone number is ████████████"
```

### Remove email addresses

```
from redact import remove_email_addresses

w_email = "My email is name@propublica.org"
no_email = remove_email_addresses(w_email)
print(no_email) # "My email is ███████████████████"
```

### Remove names of people

```
from redact import remove_persons

w_people = "Adam is going to school today"
no_people = remove_persons(w_people)
print(w_email) # "████ is going to school today"
```