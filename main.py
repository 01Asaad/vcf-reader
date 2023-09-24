import quopri
from traceback import format_exc
from re import sub
with open("pp.vcf", "r", encoding="utf-8") as f :
	t=f.read()
ppp=[]
errprs=0
t=t.splitlines()
for i in range(len(t)) :
	if "BEGIN" in t[i] :
		si=i

		for j in range(len(t[si:])) :
			if "END" in t[si+j] :
				ei=j+si
				print(si, ei)
				break
		for k in t[si:ei] :
			#print(k)
			if k.startswith("TEL") :
				if k.startswith("TEL:") :
					tel=k[2:]
				elif k.startswith("TEL;") :
					for p in range(len(k)) :
						if k[p]==":" :
							tel=k[p+1:]
			if k.startswith("N") :
				if k.startswith("N:") :
					name=k[2:]
				elif k.startswith("N;") :
					for p in range(len(k)) :
						if k[p]==":" :
							try :
								name=sub(";"," ",str(quopri.decodestring(k[p+1:]), encoding="UTF-8")).strip()
							except :
								rty=len(k)
								while rty>=0 :
									try :
										name=sub(";"," ",str(quopri.decodestring(k[p+1:rty+1]), encoding="UTF-8")).strip()
										break
									except :
										rty-=1
										if rty<0 : raise Exception("FFFF")
		try :
			name=name.split(" ")
			print(name)
			namee=name[1:]
			namee.append(name[0])
			print(name[1:], name[0])
			name=" ".join(namee)
			ppp.append((name, tel))
			del name, tel
		except :
			#print(format_exc())
			errprs+=1
			#break
			continue
ppp="\n".join([f"{d[1]} : {d[0]}" for d in ppp])
#print(ppp)
with open("er.txt", "w", encoding="utf-8") as f :
	f.write(ppp)
print(errprs)