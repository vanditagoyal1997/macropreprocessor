f1=open("test.txt",'r')
f2=open("test2.txt",'w')
macro={}
macropar={}
macroarg={}
s=f1.readlines()
#print (s)
for i in range(len(s)):
	s[i]=s[i].strip()
for i in range(len(s)):
	l=s[i].split(" ")
	#print (l)
	if l[0]=="$startmacro":
		i=i+1
		lprog=[]
		lpar=[]
		while (s[i]!="$endmacro"):
			lprog.append(s[i])
			i+=1
		macro[l[1]]=lprog
		if len(l)>2:
			if "," in l[2]:
				l[2]=l[2].split(",")
				for j in range(len(l[2])):
					l[2][j]=l[2][j].strip("$")
					lpar.append(l[2][j])
		macropar[l[1]]=lpar
		macroarg[l[1]]=[]
			
print (macro)
print (macropar)

for w in range(len(s)):
	l=s[w].split(" ")
	if l[0] in macro.keys():
		if len(l)>1:
			a=l[1]
			if "," in a:
				a=a.split(",")
			if len(a)!=len(macropar[l[0]]):
				print("error")
				break
			larg=[]
			for j in range(len(a)):
				larg.append(a[j])
			print (str(w) +":")
			#print (larg)
			macroarg[l[0]]=larg
			#print (macroarg[l[0]])
			for i in range (len(macro[l[0]])):
				d=macro[l[0]][i]
				if "$" in d:
					d=d.split("$")	
					res=d[0]
					if len(d)>2:
						for j in range(len(d)):
							g=0
							word=''
							res1=''
							while g<len(d[j]) and d[j][g].isalnum():
								word=word+d[j][g]
								g=g+1
							for k in range(len(macropar[l[0]])):
								if macropar[l[0]][k]==word:
									word=macroarg[l[0]][k]
									res1=res1+word+d[j][g:len(d[j])]
									d[j]=res1
									#print(d[j])
							res=res+d[j]
							
					else:
						for k in range(len(macropar[l[0]])):
							if macropar[l[0]][k]==d[1]:
								res=res+macroarg[l[0]][k]
								#print(macroarg[l[0]][k])
				
				else:
					res=d
				f2.write(res+"\n")
		else:
			for i in range(len(macro[l[0]])):
				f2.write(macro[l[0]][i]+"\n")
			
	else:
		f2.write(s[w]+"\n")
				
		
		
