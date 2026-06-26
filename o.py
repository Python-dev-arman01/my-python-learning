with open("My_info.txt","w") as f:
	f.write("My name is : Mohammad-Arman\nMy carunt age is:16 \n My carunt class is: 11 by pcm\n I am from india")
	
	
with open("My_info.txt","a") as f:
	f.write(" I wans i make  a profetional python devlaper")
	
with open("My_info.txt","r") as f:
	data= f.read()
print(data.split())
print("="*55)	
data.replace("carunt","curunt")
data.replace("wants","want to")
data.replace("profetional","profesional")
data.replace("devlaper","devloper")
with open ("My_info.txt","r") as f:
	data= f.read()	
	
print(data.split())