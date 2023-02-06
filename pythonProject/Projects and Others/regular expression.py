import re

mystr = '''Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +44 (20) 7235 8281
Fax: +44 (20) 7235 8727
Email: tata@tata.co.uk
Website: www.europe.tata.com
Directions: View map
Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +1 (703) 243 9787
Fax: +1 (703) 243 9791
66-66
455-4545
Email: northamerica@tata.com 
Website: www.northamerica.tata.com
Directions: View map fass
harry bhai lekin
bahut hi badia aadmi haiaiinaiiiiiiiiiiii'''

# findall,search,split,sub,finditer
# patt = re.compile(r'fass')
# patt = re.compile(r'.aadm')
# patt = re.compile(r'^Tata')  # return start with
# patt = re.compile(r'iiiii')  # return end with
# patt = re.compile(r'ai*')  # return with a and all i
# patt = re.compile(r'ai+')
# patt = re.compile(r'ai{2}')  # return only specified occurrence of i
# patt = re.compile(r'(ai){2}')
# patt = re.compile(r'(ai){1}|t')  # either ai or t

# special sequences
# patt = re.compile(r'\ATata')
# patt = re.compile(r'\bTata')
# patt = re.compile(r'Fax\b')
# patt = re.compile(r'27\b')
patt = re.compile(r'\d{5}-\d{4}')

matches = patt.finditer(mystr)
for match in matches:
    print(match)
    # print(mystr[447:452])

# task -> given a string with lot of indian phone numbers starting from +91 search all the phone nu using \b
