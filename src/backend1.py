import globalvar
from globalvar import Nilai, Operan, string, Operator, Solusi, Bracket, Hasil

""" -----Algoritma greedy untuk '24 solver'----- """

def SortNilai (Operan):
#I.S. list berisi operan terdefinisi
#F.S. list berisi operan terurut dari besar ke kecil
	loop = len(Operan)
	swap = True
	i=0
	while(i<loop-1) and swap:
		swap=False
		for j in range (loop-1):
			if (int(Operan[j]) < int(Operan[j+1])):
				Operan[j],Operan[j+1] = Operan[j+1],Operan[j]
				swap = True

def CountOperator (a,Op,b):
#I.S. char a, b, Op terdefinisi
#F.S. Hasil kalkulasi integer a dan b sesuai Op	
	if (Op == '+'):
		return (int(a) + int(b))
	elif (Op == '-'):
		return int(a) - int(b)
	elif (Op == '*'):
		return int(a) * int(b)
	else:
		return int(a) / int(b)

def CountSolusi (Solusi,Op,a,Bracket):
#I.S. list Solusi terdefinisi (tidak boleh kosong),char Op, int a, dan int Bracket terdefinisi
#F.S. Hasil kalkulasi list Solusi bila digabungkan dengan calon solusi
	i=1
	hasil = Solusi[i-1]
	if(Bracket==3):
		hasil=CountOperator(Solusi[2],Solusi[3],Solusi[4])
		hasil=CountOperator(Solusi[0],Solusi[1],hasil)
		hasil=CountOperator(hasil,Op,a)
	else:
		while (i<(len(Solusi)-1)):
			hasil = CountOperator(hasil,Solusi[i],Solusi[i+1])
			i+=2
		hasil = CountOperator(hasil,Op,a)
	return hasil

def CountPoin (Solusi,Op,Bracket):
#I.S. list Solusi terdefinisi (tidak boleh kosong), char Op dan int Bracket terdefinisi
#F.S. Output poin tiap operator dan tanda kurung yang digunakan, yaitu
# '+'=5, '-'=4, '*'=3, '/'=2, '()'=-1
	Minus = False #True jika Op yang sebelumnya dipakai '+' atau '-'
	i=1
	Poin=0
	while(i<(len(Solusi)-1)):
		if(Solusi[i] == '+'):
			Poin+=5
			Minus = True
		elif(Solusi[i] == '-'):
			Poin+=4
			Minus = True
		elif(Solusi[i] == '*'):
			if(Minus):
				Poin+=2
			else:
				Poin+=3
			Minus=False
		elif(Solusi[i] == '/'):
			if(Minus):
				Poin+=1
			else:
				Poin+=2
		i+=2
	if(Op == '+'):
		Poin+=5
	elif(Op == '-'):
		Poin+=4
	elif(Op == '*'):
		if(Minus):
			Poin +=2
		else:
			Poin +=3
	else:
		if(Minus):
			Poin +=1
		else:
			Poin+=2
	if(Bracket==3):
		Poin-=1
	return Poin

def Seleksi (Operan,Operator,Solusi):
#I.S. list Operan dan Solusi terdefinisi, tidak kosong. list Operator terdefinisi
#F.S. menyeleksi kandidat (Operan dan Operator) untuk masuk Solusi
	global Bracket
	global Hasil
	idxmaks = 0 	#untuk menandakan kandidat yang akan masuk solusi
	maks = -9999	#untuk menandakan nilai kandidat yang terbaik
	if(Bracket==0):
		if(Operan[0]==1 and len(Operan)!=1):
				if(Hasil>=3 and Hasil<=8):
					if(len(Operan)==3):
						Bracket=6
						idxmaks=2
					else:
						for i in range (len(Operator)):
							temp=CountSolusi(Solusi,Operator[i],Operan[0],Bracket)
							if(temp>=24):
								selisih24 = temp - 24
							else:
								selisih24 = 24 - temp
							if (CountPoin(Solusi,Operator[i],Bracket)-selisih24 > maks):
								Hasil=temp
								maks = CountPoin(Solusi,Operator[i],Bracket)-selisih24
								idxmaks=i
				elif(Hasil>=9 and Hasil<=13):
					if(len(Operan)==3):
						Bracket=3
						idxmaks=2
					else:
						Bracket=4
						idxmaks=2
				else:
					for i in range (len(Operator)):
						temp=CountSolusi(Solusi,Operator[i],Operan[0],Bracket)
						if(temp>=24):
							selisih24 = temp - 24
						else:
							selisih24 = 24 - temp
						if (CountPoin(Solusi,Operator[i],Bracket)-selisih24 > maks):
							Hasil=temp
							maks = CountPoin(Solusi,Operator[i],Bracket)-selisih24
							idxmaks=i
		elif(Operan[0]==1 and Hasil==24):
			idxmaks=2
		else:
			for i in range (len(Operator)):
				temp=CountSolusi(Solusi,Operator[i],Operan[0],Bracket)
				if(temp>=24):
					selisih24 = temp - 24
				else:
					selisih24 = 24 - temp
				if (CountPoin(Solusi,Operator[i],Bracket)-selisih24 > maks):
					Hasil=temp
					maks = CountPoin(Solusi,Operator[i],Bracket)-selisih24
					idxmaks=i
	elif(Bracket==3):
		if(len(Operan)==2):
			Hasil=CountOperator(Solusi[2],Operator[0],Operan[0])
			Hasil=CountOperator(Solusi[0],Solusi[1],Hasil)
			idxmaks=0
		elif (Hasil==24):
			idxmaks=2
		else:
			for i in range (len(Operator)):
				temp=CountSolusi(Solusi,Operator[i],Operan[0],Bracket)
				if(temp>=24):
					selisih24 = temp - 24
				else:
					selisih24 = 24 - temp
				if (CountPoin(Solusi,Operator[i],Bracket)-selisih24 > maks):
					Hasil=temp
					maks = CountPoin(Solusi,Operator[i],Bracket)-selisih24
					idxmaks=i
	elif(Bracket==4 or Bracket==6):
		idxmaks=0	
	Solusi.append(Operator[idxmaks])


def Greedy (Operan,Operator,Solusi):
#I.S. list Operan terisi terurut mengecil, list Operator terdefinisi, list Solusi kosong
#F.S. list Operan kosong, list Solusi terisi solusi
	global Bracket
	global Hasil
	Hasil+=Operan[0]
	Solusi.append(str(Operan[0]))
	Operan.remove(Operan[0])
	while(len(Operan)!=0):
		Seleksi(Operan,Operator,Solusi)
		Solusi.append(str(Operan[0]))
		Operan.remove(Operan[0])

def PrintSolusi (Solusi):
#I.S. list Solusi terdefinisi dan panjangnya 7 (full), int Bracket terdefinisi
#F.S. Output solusi ke layar
	global Bracket
	global string
	if(Bracket==0):
		if (Solusi[3]=='+' or Solusi[3]=='-') and (Solusi[5]=='*' or Solusi[5]=='/'):
			Bracket = 2
		elif(Solusi[1]=='+' or Solusi[1]=='-') and (Solusi[3]=='*' or Solusi[3]=='/'):
			Bracket = 1
	elif(Bracket==4):
		if(Solusi[1]=='+' or Solusi[1]=='-'):
			Bracket=5
	if(Bracket ==0):
		for x in Solusi:
			string.append(x)
	elif(Bracket ==1):
		string.append("(")
		for i in range(3):
			string.append(Solusi[i])
		string.append(")")
		for i in range(3,7):
			string.append(Solusi[i])
	elif(Bracket==2):
		string.append("(")
		for i in range(5):
			string.append(Solusi[i])
		string.append(")")
		for i in range(5,7):
			string.append(Solusi[i] )
	elif(Bracket==3):
		for i in range(2):
			string.append(Solusi[i] )
		string.append("(" )
		for i in range(2,5):
			string.append(Solusi[i] )
		string.append(")" )
		for i in range(5,7):
			string.append(Solusi[i] )
	elif(Bracket==4):
		for i in range(4):
			string.append(Solusi[i] )
		string.append("(" )
		for i in range (4,7):
			string.append(Solusi[i] )
		string.append(")" )
	elif(Bracket==5):
		string.append("(" )
		for i in range(3):
			string.append(Solusi[i] )
		string.append(")"+Solusi[3]+"(" )
		for i in range(4,7):
			string.append(Solusi[i] )
		string.append(")" )
	else:
		for i in range(2):
			string.append(Solusi[i] )
		string.append("(" )
		for i in range(2,7):
			string.append(Solusi[i] )
		string.append(")" )
	string.append("")
