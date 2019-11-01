from urllib.request import urlopen
from bs4 import BeautifulSoup
from tqdm import tqdm

def get_pvi_month(kw):
	# https://en.wikipedia.org/w/index.php?title=virtual_pets&action=info
    kw = kw.replace(' ','_')
    try:
        html = urlopen(f"https://en.wikipedia.org/w/index.php?title={kw}&action=info")
    except BaseException:
        return 0
    bsObj = BeautifulSoup(html, 'html.parser')
    pvi = bsObj.find("div", {"class","mw-pvi-month"}).text
    return int(pvi.replace(',',''))


filename = "Wiki_tree-Areas_of_computer_science-5.txt"
kws = set()

with open(filename) as f:
    for line in f.readlines():
        h,kw = line.strip().split('#')
        kws.add(kw)

kw_pvis = {}
for kw in tqdm(kws,ascii=True):
   	pvi = get_pvi_month(kw)
   	kw_pvis[kw] = pvi

with open("Wiki_pvi.txt","w") as f:
    for kw,pvi in kw_pvis.items():
        print(kw+"\t"+str(pvi),file=f)
