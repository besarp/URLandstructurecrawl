import requests
from bs4 import BeautifulSoup
from tkinter import *

root = Tk()

def trade_spider():
    faqe = 1
    faqe_max = faqemaxinput.get()
    while faqe <= int(faqe_max):
        url = 'https://www.merrjep.com/shpalljet/?Page=' + str(faqe)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('a',{'class': 'Link_vis'}):
            href = 'https://www.merrjep.com' + link.get('href')
            title = link.string
            Label(root, text="Emri: \n" + title).grid(row=1,column=1)
         #   print(title.encode('utf-8', 'replace').decode())
        #    print(href)
            merr_te_dhena(href)
        faqe += 1


def merr_te_dhena(item_url):
    j=3
    i=1
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for cmimi in soup.findAll('strong',{'class' : 'text-success'}):
        Label(root, text="cmimi: \n" + cmimi.string).grid(row=i,column=0)
        i+=1
    for link in soup.findAll('a'):
        href = "https://www.merrjep.com" + link.get('href')
        if isinstance(href, str):
            Label(root , text=href).grid(row=j,column=1)
            j+=1

faqemaxinput = Entry(root, width=50)
faqemaxinput.grid(row=0,column=1)
faqemaxlabel = Label(root , text="Zgjedh Faqet maksimale per crawl :").grid(row=0,column=0)

button = Button(root, text="Vazhdo", padx=10, pady=10, command=trade_spider).grid(row=1,column=2)


root.mainloop()


#faqe_max_input = input("Zgjedh sa faqe maksimale ")


