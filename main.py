f = open('python.txt','r')
text = str(f.read())
text=text.replace('.',' ')
text=text.replace('!',' ')
text=text.replace(',',' ')
text=text.replace('?',' ')
text=text.replace('-',' ')
text=text.replace('(',' ')
text=text.replace(')',' ')
text=text.replace(':',' ')
text=text.replace(';',' ')
text=text.replace('"',' ')
text=text.replace("'",' ')
text=text.replace("—",' ')
text=text.replace("«",' ')
text=text.replace("»",' ')
text=text.lower()
text=text.split()
rez={}
for i in range(len(text)):
	if rez.get(text[i])!=None:
		rez[text[i]]+=1
	else:
		rez[text[i]]=1	
b=0
for key in rez:
	if rez[key]>b:
		b=rez[key]
		c=key
print(rez[c],c)		
