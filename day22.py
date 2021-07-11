#1q
from PIL import Image
img = Image.open("study.png")
print(img.format)
import matplotlib.pyplot as plt
plt.imshow(img)
#2q
import pyPDF2
pdf1File =open('100 python interview Questions.pdf', 'rb')
pdf2File = open('python cheatsheet.pdf','rb')
pdf1Reader = pyPDF2.pdfFileReader(pdf1File)
pdf2Reader = pyPDF2.pdfFileReader(pdf1File)
pdfWriter = pyPDF2.pdfFileWriter()
for pageNum in range(pdf1Reader.numPages):
    pageObj = pdf1Reader.getPage(pageNum)
    pdfWriter.addpage(pageObj)
for pageNum in range(pdf2reader.numPages):
    pageObj = pdf2Reader.getPage(pageNum)
    pdfWriter.addpage(pageObj)

pdfOutputFile = open('MergedFiles.pdf','wb')
pdfWriter.write(pdfOutputFile)

pdfOutputFile.close()
pdf1File.close()
pdf2File.close()
pdf3=open('MergedFiles.pdf','rb')
pdf3Reader = PyPDF2.pdfFileReader(pdf3)
print(pdf3Reader)
pdf3.close()
#3q
import requests
import mysqldb
from bs4 import Beautifulsoup
import mysql.connector
mydb = mysql.connector.connect(host="local host",username="root",password="Dharani@379")
mydb = mysql.connector.connect(host="local host",username="root",password="Dharani@379",databas = "doctors1")
dbse = mydb.cursor()

url_to_scrape = 'https://news.ycombinator.com/news'
plain_html_text = requests.get(url_to_scrape)
soup = BeautifulSoup(plain_html_text.text, "html.parser")
print(soup.prettify())



#4q
import mysql.connector
mydb = mysql.connector.connect(host="local host",username="root",password="Dharani@379")
dbse=mydb.cursor()
dbse.execute("SHOW DATABASES")
for entry in dbse:
    print(entry)


import mysql.connector
mydb = mysql.connector.connect(host="local host",username="root",password="Dharani@379",database="doctors1")
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM Doctors where patients_visited=0")
myresult=mycursor.fetchall()
for x in myresult:
    print(x)


    

    
