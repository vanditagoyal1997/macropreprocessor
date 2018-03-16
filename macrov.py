f1=open("test.txt",'r')
f2=open("test2.txt",'w')
macro={}
macropar={}
macroarg={}
macrodef={}
s=f1.readlines()

#function for populating macro and macropar dictionary with the program and parameters associated with the macro
def definemacro(s,l,i): 
	lprog=[]
	lpar=[]
	ldef=[]
	if "$endmacro" in s[i-1]: #for a single line macro
		j=3
		singleline=''
		while (l[j]!="$endmacro"):
			if "#" in l[j]: #for removal of a comment
				x=l[j].index("#")
				l[j]=l[j][0:x-1]
				singleline=singleline+l[j]+" "
				j=j+1
			else:
				singleline=singleline+l[j]+" "
				j+=1
		lprog.append(singleline)
	if "$endmacro" not in s[i-1]:
		while (s[i]!="$endmacro"):
			l1=s[i].split(" ")
			if l1[0]=="$startmacro": #for nested macros
				if "$endmacro" in l1: #if a single line macro is defined within another macro
					k=3
					singleline1=''
					while (l1[k]!="$endmacro"):
						if "#" in l1[k]: #for removal of a comment
							x=l1[k].index("#")
							l1[k]=l[k][0:x-1]
							singleline1=singleline1+l1[k]+" "
							k=k+1
						else:
							singleline1=singleline1+l1[k]+" "
							k+=1
					lprog.append(singleline1)
					
				
				definemacro(s,l1,i+1)
				i=i+1
			elif "#" in s[i]: #for removal of a comment
				x=s[i].index("#")
				s[i]=s[i][0:x-1]
				lprog.append(s[i])
				i=i+1
			else:
				lprog.append(s[i])
				i+=1
	macro[l[1]]=lprog
	print(macro)
	if len(l)>2: #for more than one parameter
		if "," in l[2]:
			l[2]=l[2].split(",")
			for j in range(len(l[2])):
				l[2][j]=l[2][j].strip("$")
				if "=" in l[2][j]:
					l[2][j]=l[2][j].split("=")
					lpar.append(l[2][j][0])
					ldef.append(l[2][j][1])
				else:
					lpar.append(l[2][j])
		else: #for only one parameter
			l[2]=l[2].strip("$")
			lpar.append(l[2])
	macropar[l[1]]=lpar
	macrodef[l[1]]=ldef
	macroarg[l[1]]=[]
	#print(macropar)

#function for populating macroarg (argument dictionary) and expanding the macro whenever a macro call is encountered
def expandmacro(l):
	larg=[]
	if len(l)>1:
		a=l[1]
		if "," in a:
			a=a.split(",")
			for j in range(len(a)):
				if "=" in a[j]: #keyword arguments
					v=a[j].split("=")
					v[0]=v[0].strip("$")
					larg.append(v[1])
				else:
					larg.append(a[j])
		else: #one argument
			if "=" in a: #keyword arguments
				v=a.split("=")
				v[0]=v[0].strip("$")
				larg.append(v[1])
			else:
				larg.append(a)
				
			
		macroarg[l[0]]=larg
		print (macroarg)
			#parameter substitution
		for i in range (len(macro[l[0]])):
			d=macro[l[0]][i]
			l2=d.split(" ")
			if l2[0] in macro.keys(): #for calling a macro inside a macro
				expandmacro(l2)
				continue
			elif "$" in d:
				d=d.strip(" ")
				d=d.split("$")	
				res=''
				if len(d)>2: #for more than one parameter substitution in a line
					for j in range(len(d)):
						g=0
						word=''
						res1=''
						while g<len(d[j]) and d[j][g].isalnum():
								word=word+d[j][g]
								g=g+1
						for k in range(len(macropar[l[0]])):
								if macropar[l[0]][k]==word:
									if macroarg[l[0]][k]=='': #default arguments to be used 
										if macrodef[l[0]][k]:
											word=macrodef[l[0]][k]
										else:
											print ("error2")
											break
									else:
										word=macroarg[l[0]][k]
									res1=res1+word+d[j][g:len(d[j])]
									print(res1)
									d[j]=res1
						res=res+d[j]	
							
								
				else: #one parameter substitution in a line
					res=d[0]
					for k in range(len(macropar[l[0]])):
						if macropar[l[0]][k]==d[1]:
							if macroarg[l[0]][k]:
								res=res+macroarg[l[0]][k]
										
							else:
								res=res+macrodef[l[0]][k]
									
					
			else: #for no parameter substitution
				res=d
			f2.write(res+"\n")
	else: #if no arguments required
		for i in range(len(macro[l[0]])):
			f2.write(macro[l[0]][i]+"\n")
			
	
for i in range(len(s)):
	s[i]=s[i].strip()

					
#for finding the last macro
'''for i in range(len(s)):
	if s[i]=="$endmacro":
		k=i'''
w=0
while (w<len(s)):
	l=s[w].split(" ")
	if l[0]=="$startmacro":
		definemacro(s,l,w+1)
		if "$endmacro" in l:
			w=w+1 #for single line macro
		else:
			w=w+len(macro[l[1]])+2 #for multiline macro
	
	else:
	#for storing arguments in macroarg dictionary
		larg=[]
		if l[0] in macro.keys(): #if a macro call is encountered
			expandmacro(l)
			w=w+1
	
		else: #writing rest of the code
			f2.write(s[w]+"\n")
			w=w+1
		
				
f1.close()
f2.close()	
		
