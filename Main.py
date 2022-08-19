from bs4 import BeautifulSoup
import requests

#can only be from flipkart.com and needed when clicked on the said product
url = input('Input the url: ')
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')                       #soup the content of the page

selection = input("Input your selected choice(input 'all' if you want all info): ")
results = soup.find('div', class_='dyC4hf')                             #locations of the variables
price = soup.find('div', class_= '_30jeq3 _16Jk6d')
title = soup.find('h1', class_= 'yhB1nd')
rating = soup.find('div', class_='_3LWZlK')
supplier = soup.find('div', class_='_1RLviY')
supplierterms = soup.find('ul', class_='_2-RJLI')
warranty = soup.find('div', class_='_352bdz')

#converts string price to integer
strprice = price.text
numfilter = filter(str.isdigit, strprice)               #Filters(filter func) out unnecessary characters(ie ₹) isdigits to numerical digits
numprice = "".join(numfilter)                           #creates string by join ""

usdprice = float(numprice) * 0.013                      #makes usd price by rupees to usd conversion

strsuppterm = supplierterms.text.replace('?', '\n')     #removes ? from supplier terms

strwarranty = warranty.text.replace('Know More', '')

if selection.lower() == 'price':
    print('\n'+'Price: '+ price.text)                           #prints price, title, rating, and usd price of the given product
if selection.lower() == 'title':
    print('Title: '+ title.text)
if selection.lower() == 'rating':
    print('Rating: '+ rating.text + '/5 stars')
if selection.lower() == 'price(usd)' or selection.lower() == 'us price':
    print('Price(USD): $', usdprice, '\n')
if selection.lower() == 'supplier':
    print('Supplier: '+ supplier.text)
if selection.lower() == 'supplier terms' or selection.lower() == 'terms' or selection.lower() == 'terms and conditions':
    print('Supplier terms:\n' + strsuppterm)
if selection.lower() == 'warranty':
    print('Warranty Information:', strwarranty, '\n')
if selection.lower() == "all":
    print('\n'+'Price: '+ price.text) 
    print('Title: '+ title.text)
    print('Rating: '+ rating.text + '/5 stars')
    print('Price(USD): $', usdprice, '\n')
    print('Supplier: '+ supplier.text)
    print('Supplier terms:\n' + strsuppterm)
    print('Warranty Information:', strwarranty, '\n')