from urllib.request import urlopen
from bs4 import BeautifulSoup
from tqdm import tqdm

MAX_LEVEL = 5
root = "Areas_of_computer_science"

def get_subtree(rets, subUrl, level):
    if level>MAX_LEVEL:
        return 0

    try:
        html = urlopen("https://en.wikipedia.org/wiki/Category:"+subUrl)
    except BaseException:
        return 0

    bsObj = BeautifulSoup(html, 'html.parser')

    bodys = bsObj.findAll("div", {"class":"CategoryTreeItem"})
    for body in bodys:
        kw = body.find("a")
        contents = kw.text
        kw = str(contents)
        print(level,kw)
        rets.append((level,kw))
        get_subtree(rets, kw.replace(' ','_'), level+1)


rets = []
get_subtree(rets,root,1)

with open(f'Wiki_tree-{root}-{MAX_LEVEL}.txt','w') as f:
    for level,kw in rets:
        try:
            print(str(level)+'#'+kw,file=f)
        except BaseException:
            continue

