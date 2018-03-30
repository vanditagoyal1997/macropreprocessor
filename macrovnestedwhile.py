f1=open("test.txt",'r') #file with the original code
f2=open("test2.txt",'w') #file with the processed code
macro={} #dictionary for holding macro name with macro code
macropar={} #dictionary for holding macro name with macro parameters
macroarg={} #dictionary for holding macro name with macro arguments
macrodef={} #dictionary for holding macro name with macro default arguments
s=f1.readlines()
#function for checking while loop
def checkwhile(t,strin,i): 
	strin=strin.split(" ")
	expr=strin[1]
	j=0
	ar1=""
	ar2=""
	ar3=""
	while (expr[j].isdigit()):
		ar1=ar1+expr[j]
		j=j+1
	while (expr[j].isdigit()==False):
		ar2=ar2+expr[j]
		j=j+1
	while (j<len(expr)):
		ar3=ar3+expr[j]
		j=j+1
	ev=eval(expr)
	i=i+1
	if ev: #only if the condition is true from the start
		j=int(ar1)
		if ar2=="<":
			while(j<int(ar3)): #counter loop
				r=i
				while (t[r]!="&endwhile"):
					q=t[r]
					lif=q.split(" ")
					if lif[0] in macro.keys(): #for calling a macro inside a macro
						expandmacro(lif)
						r=r+1
						continue

					elif "$" in q:
						q=q.strip(" ")
						q=q.split("$")	
						resif=''
						if len(q)>2: #for more than one parameter substitution in a line
							for jif in range(len(q)):
								gif=0
								wordif=''
								res1if=''
								while gif<len(q[jif]) and q[jif][gif].isalnum():
									wordif=wordif+q[jif][gif]
									gif=gif+1
								for k in range(len(macropar[l[0]])):
									if macropar[l[0]][k]==wordif:
										if macroarg[l[0]][k]=='': #default arguments to be used 
											if macrodef[l[0]][k]:
												wordif=macrodef[l[0]][k]
											else:
												print ("error2")
												break
										else:
											wordif=macroarg[l[0]][k]
										res1if=res1if+wordif+q[jif][gif:len(q[jif])]
										q[jif]=res1if
							resif=resif+q[jif]	
								
						else: #one parameter substitution in a line
							resif=q[0]
							gif=0
							wordif=''
							res1if=''
							while gif<len(q[1]) and q[1][gif].isalnum():
								wordif=wordif+q[1][gif]
								gif=gif+1
							for k in range(len(macropar[l[0]])):
								if macropar[l[0]][k]==wordif:
									if macroarg[l[0]][k]=='': #default arguments to be used 
										if macrodef[l[0]][k]:
											wordif=macrodef[l[0]][k]
										else:
											print ("error2")
											break
									else:
										wordif=macroarg[l[0]][k]
									res1if=res1if+wordif+q[1][gif:len(q[1])]
									q[1]=res1if
							resif=resif+q[1]		
					
					else: #for no parameter substitution
						resif=q
					finalif=resif
					print(finalif)
					if "&if" in finalif: #for if and else statement
						r=checkif(t,finalif,r)
					elif "&while" in finalif:
						r=checkwhile(t,finalif,r)
					else:
						f2.write(finalif+"\n")
						r=r+1
				
				j=j+1
		elif ar2==">":
			while(j>int(ar3)): #counter loop
				r=i
				while (t[r]!="&endwhile"):
					q=t[r]
					lif=q.split(" ")
					if lif[0] in macro.keys(): #for calling a macro inside a macro
						expandmacro(lif)

					elif "$" in q:
						q=q.strip(" ")
						q=q.split("$")	
						resif=''
						if len(q)>2: #for more than one parameter substitution in a line
							for jif in range(len(q)):
								gif=0
								wordif=''
								res1if=''
								while gif<len(q[jif]) and q[jif][gif].isalnum():
									wordif=wordif+q[jif][gif]
									gif=gif+1
								for k in range(len(macropar[l[0]])):
									if macropar[l[0]][k]==wordif:
										if macroarg[l[0]][k]=='': #default arguments to be used 
											if macrodef[l[0]][k]:
												wordif=macrodef[l[0]][k]
											else:
												print ("error2")
												break
										else:
											wordif=macroarg[l[0]][k]
									res1if=res1if+wordif+q[jif][gif:len(q[jif])]
									q[jif]=res1if
							resif=resif+q[jif]	
								
						else: #one parameter substitution in a line
							resif=q[0]
							gif=0
							wordif=''
							res1if=''
							while gif<len(q[1]) and q[1][gif].isalnum():
								wordif=wordif+q[1][gif]
								gif=gif+1
							for k in range(len(macropar[l[0]])):
								if macropar[l[0]][k]==wordif:
									if macroarg[l[0]][k]=='': #default arguments to be used 
										if macrodef[l[0]][k]:
											wordif=macrodef[l[0]][k]
										else:
											print ("error2")
											break
									else:
										wordif=macroarg[l[0]][k]
									res1if=res1if+wordif+q[1][gif:len(q[1])]
									q[1]=res1if
							resif=resif+q[1]		
					
					else: #for no parameter substitution
						resif=q
					finalif=resif
					#print(finalif)
					if "&if" in finalif: #for if and else statement
						r=checkif(t,finalif,r)
					elif "&while" in finalif:
						r=checkwhile(t,finalif,r)
					else:
						f2.write(finalif+"\n")
						r=r+1
				j=j-1
		elif ar2=="<=":
			while(j<=int(ar3)): #counter loop
				r=i
				while (t[i]!="&endwhile"):
					q=t[r]
					lif=q.split(" ")
					if lif[0] in macro.keys(): #for calling a macro inside a macro
						expandmacro(lif)

					elif "$" in q:
						q=q.strip(" ")
						q=q.split("$")	
						resif=''
						if len(q)>2: #for more than one parameter substitution in a line
							for jif in range(len(q)):
								gif=0
								wordif=''
								res1if=''
								while gif<len(q[jif]) and q[jif][gif].isalnum():
									wordif=wordif+q[jif][gif]
									gif=gif+1
								for k in range(len(macropar[l[0]])):
									if macropar[l[0]][k]==wordif:
										if macroarg[l[0]][k]=='': #default arguments to be used 
											if macrodef[l[0]][k]:
												wordif=macrodef[l[0]][k]
											else:
												print ("error2")
												break
										else:
											wordif=macroarg[l[0]][k]
									res1if=res1if+wordif+q[jif][gif:len(q[jif])]
									q[jif]=res1if
							resif=resif+q[jif]	
								
						else: #one parameter substitution in a line
							resif=q[0]
							gif=0
							wordif=''
							res1if=''
							while gif<len(q[1]) and q[1][gif].isalnum():
								wordif=wordif+q[1][gif]
								gif=gif+1
							for k in range(len(macropar[l[0]])):
								if macropar[l[0]][k]==wordif:
									if macroarg[l[0]][k]=='': #default arguments to be used 
										if macrodef[l[0]][k]:
											wordif=macrodef[l[0]][k]
										else:
											print ("error2")
											break
									else:
										wordif=macroarg[l[0]][k]
									res1if=res1if+wordif+q[1][gif:len(q[1])]
									q[1]=res1if
							resif=resif+q[1]		
					
					else: #for no parameter substitution
						resif=q
					finalif=resif
					#print(finalif)
					if "&if" in finalif:#for if and else statement
						r=checkif(t,finalif,r)
					elif "&while" in finalif:
						r=checkwhile(t,finalif,r)
					else:
						f2.write(finalif+"\n")
						r=r+1
				j=j+1
		elif ar2==">=":
			while(j>=int(ar3)):#counter loop
				r=i
				while (t[r]!="&endwhile"):
					q=t[r]
					lif=q.split(" ")
					if lif[0] in macro.keys(): #for calling a macro inside a macro
						expandmacro(lif)

					elif "$" in q:
						q=q.strip(" ")
						q=q.split("$")	
						resif=''
						if len(q)>2: #for more than one parameter substitution in a line
							for jif in range(len(q)):
								gif=0
								wordif=''
								res1if=''
								while gif<len(q[jif]) and q[jif][gif].isalnum():
									wordif=wordif+q[jif][gif]
									gif=gif+1
								for k in range(len(macropar[l[0]])):
									if macropar[l[0]][k]==wordif:
										if macroarg[l[0]][k]=='': #default arguments to be used 
											if macrodef[l[0]][k]:
												wordif=macrodef[l[0]][k]
											else:
												print ("error2")
												break
										else:
											wordif=macroarg[l[0]][k]
									res1if=res1if+wordif+q[jif][gif:len(q[jif])]
									q[jif]=res1if
							resif=resif+q[jif]	
								
						else: #one parameter substitution in a line
							resif=q[0]
							gif=0
							wordif=''
							res1if=''
							while gif<len(q[1]) and q[1][gif].isalnum():
								wordif=wordif+q[1][gif]
								gif=gif+1
							for k in range(len(macropar[l[0]])):
								if macropar[l[0]][k]==wordif:
									if macroarg[l[0]][k]=='': #default arguments to be used 
										if macrodef[l[0]][k]:
											wordif=macrodef[l[0]][k]
										else:
											print ("error2")
											break
									else:
										wordif=macroarg[l[0]][k]
									res1if=res1if+wordif+q[1][gif:len(q[1])]
									q[1]=res1if
							resif=resif+q[1]		
					
					else: #for no parameter substitution
						resif=q
					finalif=resif
					#print(finalif)
					if "&if" in finalif:#for if and else statement
						r=checkif(t,finalif,r)
					elif "&while" in finalif:
						r=checkwhile(t,finalif,r)
					else:
						f2.write(finalif+"\n")
						r=r+1
				j=j-1
		
	while (t[i]!="&endwhile"):
		i=i+1
	return i+1
#function for evaluating if and else statements
def checkif(t,strin,i):
	strin=strin.split(" ")
	expr=strin[1]
	ev=eval(expr)
	i=i+1
	if ev:
		while(t[i]!="&endif"):
			q=t[i]
			lif=q.split(" ")
			if lif[0] in macro.keys(): #for calling a macro inside a macro
				expandmacro(lif)

			elif "$" in q:
				q=q.strip(" ")
				q=q.split("$")	
				resif=''
				if len(q)>2: #for more than one parameter substitution in a line
					for jif in range(len(q)):
						gif=0
						wordif=''
						res1if=''
						while gif<len(q[jif]) and q[jif][gif].isalnum():
								wordif=wordif+q[jif][gif]
								gif=gif+1
						for k in range(len(macropar[l[0]])):
								if macropar[l[0]][k]==wordif:
									if macroarg[l[0]][k]=='': #default arguments to be used 
										if macrodef[l[0]][k]:
											wordif=macrodef[l[0]][k]
										else:
											print ("error2")
											break
									else:
										wordif=macroarg[l[0]][k]
									res1if=res1if+wordif+q[jif][gif:len(q[jif])]
									q[jif]=res1if
						resif=resif+q[jif]	
								
				else: #one parameter substitution in a line
					resif=q[0]
					gif=0
					wordif=''
					res1if=''
					while gif<len(q[1]) and q[1][gif].isalnum():
							wordif=wordif+q[1][gif]
							gif=gif+1
					for k in range(len(macropar[l[0]])):
							if macropar[l[0]][k]==wordif:
								if macroarg[l[0]][k]=='': #default arguments to be used 
									if macrodef[l[0]][k]:
										wordif=macrodef[l[0]][k]
									else:
										print ("error2")
										break
								else:
									wordif=macroarg[l[0]][k]
								res1if=res1if+wordif+q[1][gif:len(q[1])]
								q[1]=res1if
					resif=resif+q[1]		
					
			else: #for no parameter substitution
				resif=q
			finalif=resif
			#print(finalif)
			if "&if" in finalif:
				i=checkif(t,finalif,i)
			elif "&while" in finalif:
				i=checkwhile(t,finalif,i)
			else:
				f2.write(finalif+"\n")
				i=i+1
		while (t[i]!="&else"):
			i=i+1
		while(t[i]!="&endelse"):
			i=i+1
		return i+1
		
	else:
		while (t[i]!="&else"):
			i=i+1
		
		while(t[i]!="&endelse"):
			q=t[i]
			lif=q.split(" ")
			if lif[0] in macro.keys(): #for calling a macro inside a macro
				expandmacro(lif)
			elif "$" in q:
				q=q.strip(" ")
				q=q.split("$")	
				resif=''
				if len(q)>2: #for more than one parameter substitution in a line
					for jif in range(len(q)):
						gif=0
						wordif=''
						res1if=''
						while gif<len(q[jif]) and q[jif][gif].isalnum():
								wordif=wordif+q[jif][gif]
								gif=gif+1
						for k in range(len(macropar[l[0]])):
								if macropar[l[0]][k]==wordif:
									if macroarg[l[0]][k]=='': #default arguments to be used 
										if macrodef[l[0]][k]:
											wordif=macrodef[l[0]][k]
										else:
											print ("error2")
											break
									else:
										wordif=macroarg[l[0]][k]
									res1if=res1if+wordif+q[jif][gif:len(q[jif])]
									q[jif]=res1if
						resif=resif+q[jif]	
								
				else: #one parameter substitution in a line
					resif=q[0]
					gif=0
					wordif=''
					res1if=''
					while gif<len(q[1]) and q[1][gif].isalnum():
							wordif=wordif+q[1][gif]
							gif=gif+1
					for k in range(len(macropar[l[0]])):
							if macropar[l[0]][k]==wordif:
								if macroarg[l[0]][k]=='': #default arguments to be used 
									if macrodef[l[0]][k]:
										wordif=macrodef[l[0]][k]
									else:
										print ("error2")
										break
								else:
									wordif=macroarg[l[0]][k]
								res1if=res1if+wordif+q[1][gif:len(q[1])]
								q[1]=res1if
					resif=resif+q[1]		
					
			else: #for no parameter substitution
				resif=q
			finalif=resif
			if "&if" in finalif: #checking for if and else statement
				i=checkif(t,finalif,i)
			elif "&while" in finalif:
				i=checkwhile(t,finalif,i)
			else:
				f2.write(finalif+"\n")
				i=i+1
		return i+1
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
					if (l1[2][0]=="$"):
						k=3
					else:
						k=2
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
		
			#parameter substitution
		i=0
		while(i<(len(macro[l[0]]))):
			d=macro[l[0]][i]
			l2=d.split(" ")
			if l2[0] in macro.keys(): #for calling a macro inside a macro
				expandmacro(l2)
				i=i+1
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
					g=0
					word=''
					res1=''
					k=0
					while g<len(d[1]) and d[1][g].isalnum():
						word=word+d[1][g]
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
							res1=res1+word+d[1][g:len(d[1])]
							print(res1)
							d[1]=res1
					res=res+d[1]		
					print(res)
			else: #for no parameter substitution
				res=d
				
			final=res
			if "&if" in final: #checking for if and else statement
				i=checkif(macro[l[0]],final,i)
			elif "&while" in final: #checking for while loop
				i=checkwhile(macro[l[0]],final,i)
				
			else:
				f2.write(final+"\n")
				i=i+1
				
	else: #if no arguments required
		for m in range(len(macro[l[0]])):
			f2.write(macro[l[0]][m]+"\n")
			
	
for i in range(len(s)):
	s[i]=s[i].strip()

					
#for finding the last macro
'''for i in range(len(s)):
	if s[i]=="$endmacro":

		k=i'''
#driving code
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
		
