import re
#1
def find_urls(text):
  
    pattern = r'https?://[^\s]+'
    urls = re.findall(pattern, text)
    return urls
#2
def email_id(etext):
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(pattern, etext)
    return emails
#3
def find_hashtag(htext):
    pattern = r'#\w+'
    hashtags = re.findall(pattern, htext)
    return hashtags
#4
def find_mentions(mtext):
    pattern = r'@\w+'
    mentions = re.findall(pattern, mtext)
    return mentions
#5
def find_numbers(dtext):
    
    pattern = r'\d+'
    numbers = re.findall(pattern, dtext)
    return numbers

#6
def find_punctuations(ptext):
   
    # Pattern to match any character that is NOT a word character (\w) or whitespace (\s)
    pattern = r'[^\w\s]'
    punctuations = re.findall(pattern, ptext)
    return punctuations
#7 
def is_valid_pan(pan):
    
    pattern = r'^[A-Z]{5}[0-9]{4}[A-Z]$'
    return bool(re.match(pattern, pan))
#8
def remove_repetitive_chars(rtext):
    
    pattern = r'(.)\1+'
    # Replace repeated characters with a single occurrence
    result = re.sub(pattern, r'\1',rtext)
    return result
#9
def find_indian_mobile_numbers(itext):
  
    pattern = r'\b[789]\d{9}\b'
    mobile_numbers = re.findall(pattern, itext)
    return mobile_numbers
#10
def find_capital_words(utext):
    
    pattern = r'\b[A-Z][a-z]*\b'
    capital_words = re.findall(pattern, utext)
    return capital_words

# 1	To find a URL in a sentence:
example = "I love spreading times at https://www.w3schools.com/python/python_regex.asp"
found_urls = find_urls(example)
print("URL(s) found:", found_urls)
#2.	Get email id from the sentence: 
etext="My email id is xyz111@gmail.com"
found_emails=email_id(etext)
print(found_emails)

#3.	To find the hashtags
htext = "#Harsh is trending now in the Bennett University."
found_hashtags = find_hashtag(htext)
print("Hashtag(s) found:", found_hashtags)

#4.	To find the mentions in a sentence: @ – This symbol is used to mention someone in tweets. 
# So, to extract words associated with @ symbol use this code

mtext = "@Ajit, please help me"
found_mentions = find_mentions(mtext)
print("Mentions found:", found_mentions)

#5.	To find numbers in a sentence:
#example="8853147 sq. km of area washed away in floods"
dtext = "8853147 sq. km of area washed away in floods"
found_numbers = find_numbers(dtext)
print("Numbers found:", found_numbers)

#6.	To find punctuations in a sentence:
# example="Corona virus killed #24506 people. #Corona is un(tolerable)"
ptext = "Corona virus killed #24506 people. #Corona is un(tolerable)"
found_punctuations = find_punctuations(ptext)
print("Punctuations found:", found_punctuations)

#7.	To Validate PAN Number use the below code: Format: First 5 letters in CAPS+4 digits+Last letter in CAPS
#	Example1: "ABCED3193P"
#	Example2: "lEcGD012eg"

pexample1 = "ABCED3193P"
pexample2 = "lEcGD012eg"

print(f"{pexample1} is valid PAN:", is_valid_pan(pexample1))
print(f"{pexample2} is valid PAN:", is_valid_pan(pexample2))

#8.	Remove repetitive characters from sentence:
#	example="heyyy this is a verrrry loong texttt" 
ex = "heyyy this is a verrrry loong texttt"
cleaned_text = remove_repetitive_chars(ex)
print("Before:", ex)
print("After:", cleaned_text)
#9.	To find Indian mobile numbers:
#	Example= "9990001796 is a phone number of PMO office"

mexample = "9990001796 is a phone number of PMO office"
found_numbers = find_indian_mobile_numbers(mexample)
print("Indian mobile number(s) found:", found_numbers)

#10.	Extract words starting with a capital letter from the input text.
#	example="Ajit Doval is the best National Security Advisor so far."

uexample = "Ajit Doval is the best National Security Advisor so far."
result = find_capital_words(uexample)
print("Words starting with capital letter:", result)
