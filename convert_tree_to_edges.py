MIN_CNT = 500

def filter(kw):
	return kw_pvis[kw]>MIN_CNT and len(kw.split(' '))<=3 and ''.join(kw.split(' ')).isalpha()


kw_pvis = {}
with open("Wiki_pvi.txt") as f:
	for line in f.readlines():
		kw,pvi = line.strip().split('\t')
		kw = kw.lower()
		pvi = int(pvi)
		kw_pvis[kw] = pvi

pairs = set()
with open(f'Wiki_tree-Areas_of_computer_science-5.txt') as f:
	stk = []
	stk.append((0,None))

	for line in f.readlines():
		h, kw = line.split('#')
		h = int(h)
		kw = kw.strip().lower()

		while len(stk)>0:
			pre_h, pre_kw = stk[-1]
			if h-pre_h==1:
				print("add:", (pre_kw,kw))
				if pre_h!=0:
					pairs.add((pre_kw,kw))
				stk.append((h,kw))
				break
			else:
				stk.pop()
				print("pop:", (pre_h,pre_kw))


with open(f'Wiki_pair-Areas_of_computer_science-{MIN_CNT}.txt','w') as f:
	for pair in pairs:
		# if True:
		if filter(pair[0]) and filter(pair[1]):
			print(pair[0]+'\t'+pair[1],file=f)
