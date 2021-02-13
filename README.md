## URL dhe structure crawling

Ky skripte ose aplikacion synon qe te nxjerr te gjitha linqet dhe disa informata rreth website te cilin e zgjedhim.
Ne rastin tone jemi fokusuar ne website-in lokal [Merrjep](https://www.merrjep.com "Website Merrjep")

Ne gui se pari zgjedhim se sa faqe deshirojme te bejme crawl pra faqen maksimale japim si input ne GUI

Kemi perdorur keto librari per zhvillimin e kodit

```python
import requests
from bs4 import BeautifulSoup
from tkinter import *
```
Per te instaluar librarine BeautifulSoup
```
pip install BeautifulSoup4
```
