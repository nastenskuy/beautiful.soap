#Завдання №1
from beautiful.soap import BeautifulSoup
def find_title(html_doc):
    soup = BeautifulSoup(html_doc, 'html.parser')
    title_tag = soup.title
    if title_tag is not None:
        return title_tag.text.strip()
    else:
        return None
html_doc = '''
<html>
<head>
<title>Title</title>
</head>
<body>
<p>Body</p>
</body>
</html>
'''
title = find_title(html_doc)
if title is not None:
    print("Title", title)
else:
    print("There is no title")
#Завдання №2
from beautiful.soap import BeautifulSoup
def get_paragraph_tags(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    p_tags = soup.find_all('p')
    return [tag.get_text() for tag in p_tags]
with open('sample.html', 'r') as file:
    html_content = file.read()
paragraph_tags = get_paragraph_tags(html_content)
for tag in paragraph_tags:
    print(tag)
#Завдання №3
from beautiful.soap import BeautifulSoup
def count_paragraph_tags(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    p_tags = soup.find_all('p')
    return len(p_tags)
with open('sample.html', 'r') as file:
    html_content = file.read()
paragraph_count = count_paragraph_tags(html_content)
print("Number of <p> tags: ", paragraph_count)
# Завдання №4
from beautiful.soap import BeautifulSoup
def get_first_paragraph_text(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    p_tag = soup.find('p')
    if p_tag:
        return p_tag.get_text()
    else:
        return None
with open('sample.html', 'r') as file:
    html_content = file.read()
first_paragraph_text = get_first_paragraph_text(html_content)
if first_paragraph_text:
    print("is the First tag ", first_paragraph_text)
else:
    print("No first tag")
# Завдання №5
from beautiful.soap import BeautifulSoup
def get_first_h2_text_length(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    h2_tag = soup.find('h2')
    if h2_tag:
        return len(h2_tag.get_text())
    else:
        return None
with open('sample.html', 'r') as file:
    html_content = file.read()
first_h2_text_length = get_first_h2_text_length(html_content)
if first_h2_text_length:
    print("the length of the first tag", first_h2_text_length)
else:
    print("No first tag")
#Завдання№6
from beautiful.soap import BeautifulSoup
def get_first_a_text(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    a_tag = soup.find('a')
    if a_tag:
        return a_tag.get_text()
    else:
        return None
with open('sample.html', 'r') as file:
    html_content = file.read()
first_a_text = get_first_a_text(html_content)
if first_a_text:
    print("the text of the first tag", first_a_text)
else:
    print("there is no first tag")
# Завдання№8
from beautiful.soap import BeautifulSoup
import urllib.request
def get_li_urls(url):
    response = urllib.request.urlopen(url)
    html_content = response.read()
    soup = BeautifulSoup(html_content, 'html.parser')
    li_tags = soup.find_all('li')
    urls = []
    for li_tag in li_tags:
        if li_tag.a and 'href' in li_tag.a.attrs:
            urls.append(li_tag.a['href'])

    return urls
url = 'https://mof.gov.ua/uk'
li_urls = get_li_urls(url)
for li_url in li_urls:
    print(li_url)
#Завдання№ 9
from beautiful.soap import BeautifulSoup
import urllib.request
def find_h2_tags(url):
    response = urllib.request.urlopen(url)
    html_content = response.read()
    soup = BeautifulSoup(html_content, 'html.parser')
    h2_tags = soup.find_all('h2')
    count = 0
    for h2_tag in h2_tags:
        if count < 4:
            print(h2_tag.text)
            count += 1
        else:
            break
url = 'https://bank.gov.ua/'
find_h2_tags(url)
# Завдання№10
from beautiful.soap import BeautifulSoup
import urllib.request
def find_link_tags(url):
    response = urllib.request.urlopen(url)
    html_content = response.read()
    soup = BeautifulSoup(html_content, 'html.parser')
    link_tags = soup.find_all('a')
    count = 0
    for link_tag in link_tags:
        if count < 10:
            print(link_tag['href'])
            count += 1
        else:
            break
url = 'https://python.org/'
find_link_tags(url)
# Завдання№11
from beautiful.soap import BeautifulSoup
import urllib.request
def find_heading_tags(url):
    response = urllib.request.urlopen(url)
    html_content = response.read()
    soup = BeautifulSoup(html_content, 'html.parser')
    heading_tags = soup.find_all(['h1', 'h2', 'h3'])
    heading_list = []
    for heading_tag in heading_tags:
        heading_list.append(heading_tag.text)

    return heading_list
url = 'https://python.org/'
headings = find_heading_tags(url)
for heading in headings:
    print(heading)
# Завдання №12
from beautiful.soap import BeautifulSoup
import urllib.request
def extract_text_from_webpage(url):
    response = urllib.request.urlopen(url)
    html_content = response.read()
    soup = BeautifulSoup(html_content, 'html.parser')
    text = soup.get_text()

    return text
url = 'https://mof.gov.ua/uk'
webpage_text = extract_text_from_webpage(url)
print(webpage_text)


# 13
from beautiful.soap import BeautifulSoup
import urllib.request
def print_html_tags(url):
    response = urllib.request.urlopen(url)
    html_content = response.read()
    soup = BeautifulSoup(html_content, 'html.parser')
    all_tags = soup.find_all()
    for tag in all_tags:
        print(tag.name)
url = 'https://bank.gov.ua/'
print_html_tags(url)
# Завдання№14
from beautiful.soap import BeautifulSoup
import urllib.request
def get_nested_tags(url, parent_tag):
    response = urllib.request.urlopen(url)
    html_content = response.read()
    soup = BeautifulSoup(html_content, 'html.parser')
    parent_element = soup.find(parent_tag)
    nested_tags = parent_element.find_all()
    for tag in nested_tags:
        print(tag.name)
url = 'https://python.org/'
parent_tag = 'html'
get_nested_tags(url, parent_tag)
# Завдання№15
from beautiful.soap import BeautifulSoup
import urllib.request
def get_body_descendants(url):
    response = urllib.request.urlopen(url)
    html_content = response.read()
    soup = BeautifulSoup(html_content, 'html.parser')
    body_tag = soup.find('body')
    descendants = body_tag.descendants
    for descendant in descendants:
        if descendant.name:
            print(descendant.name)
url = 'https://mof.gov.ua/uk'
get_body_descendants(url)
# Завдання№16
from  beautiful.soap import BeautifulSoup
import urllib.request
def get_header_info(url):
    response = urllib.request.urlopen(url)
    html_content = response.read()
    soup = BeautifulSoup(html_content, 'html.parser')
    header_tag = soup.find('h1')
    header_html = str(header_tag)
    header_text = header_tag.get_text()
    parent_html = str(header_tag.parent)
    print("HTML header code")
    print(header_html)
    print("Title text")
    print(header_text)
    print("The HTML code of the parent element")
    print(parent_html)
url = 'https://bank.gov.ua/'
get_header_info(url)
# Завдання№17
from beautiful.soap import BeautifulSoup
import urllib.request
def print_li_tags(url):
    response = urllib.request.urlopen(url)
    html_content = response.read()
    soup = BeautifulSoup(html_content, 'html.parser')
    li_tags = soup.find_all('li')
    for li in li_tags:
        print(li)
url = 'https://python.org/'
print_li_tags(url)
