f1=open("test.txt",'r')
f2=open("test2.txt",'w')
macro={}
macropar={}
macroarg={}
macrodef={}
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
		ldef=[]
		while (s[i]!="$endmacro"):
			lprog.append(s[i])
			i+=1
		macro[l[1]]=lprog #creating a dictionary for storing macro name with the actual definition
		if len(l)>2: #if there are parameters
			if "," in l[2]: #if there are more than one parameters
				l[2]=l[2].split(",")
				for j in range(len(l[2])):
					l[2][j]=l[2][j].strip("$")
					if "=" in l[2][j]: #if there is any default value for parameters
						l[2][j]=l[2][j].split("=")
						lpar.append(l[2][j][0])
						ldef.append(l[2][j][1])
					else:
						lpar.append(l[2][j])
			else: #if there is only one parameter
				l[2]=l[2].strip("$")
				lpar.append(l[2])
		macropar[l[1]]=lpar
		macrodef[l[1]]=ldef
		macroarg[l[1]]=[]
			
#print (macro)
#print (macropar)

for w in range(len(s)):
	l=s[w].split(" ")
	if l[0] in macro.keys(): #detecting macro calls
		if len(l)>1:#if arguments are given
			a=l[1]
			if "," in a:#if more than one arguments are given
				a=a.split(",")
			'''if len(a)>len(macropar[l[0]]):
				print("error1")
				break'''
			larg=[]
			if len(a)==len(macropar[l[0]]):
				for j in range(len(a)):
					if "=" in a[j]: #for keyword arguments
						v=a[j].split("=")
						v[0]=v[0].strip("$")
						larg.append(v[1])
					else:
						larg.append(a[j])
			
				
			#print (str(w) +":")
			#print (larg)
			macroarg[l[0]]=larg
			#print (macroarg[l[0]])
			for i in range (len(macro[l[0]])): #subsituting arguments
				d=macro[l[0]][i]
				if "$" in d:
					d=d.split("$")	
					res=d[0]
					if len(d)>2:#for more than one parameter subsitution in a line
						for j in range(len(d)):
								g=0
								word=''
								res1=''
								while g<len(d[j]) and d[j][g].isalnum():
									word=word+d[j][g]
									g=g+1
								for k in range(len(macropar[l[0]])):
									if macropar[l[0]][k]==word:
										if macroarg[l[0]][k]=='':
											if macrodef[l[0]][k]:
												word=macrodef[l[0]][k]
											else:
												print ("error2")
												break
										else:
											word=macroarg[l[0]][k]
										res1=res1+word+d[j][g:len(d[j])]
										d[j]=res1
									#print(d[j])
								res=res+d[j]
						
							
					else: #for only one parameter subsitution in one line
						for k in range(len(macropar[l[0]])):
							if macropar[l[0]][k]==d[1]:
								if macroarg[l[0]][k]:
									res=res+macroarg[l[0]][k]
								else:
									res=res+macrodef[l[0]][k]
								#print(macroarg[l[0]][k])
				
				else:
					res=d
				f2.write(res+"\n")
		else: #for no parameter subsitution in an expansion
			for i in range(len(macro[l[0]])):
				f2.write(macro[l[0]][i]+"\n")
			
	else:
		f2.write(s[w]+"\n")
				
		
		
