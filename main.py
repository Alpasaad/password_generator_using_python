import tkinter as tk 
import string 
import random 

char_num=input("please enter the number of charcter you want: ")  

while True:
        
        try:
            char_num=int(char_num)
            if char_num <6:
                print("[-]the length must be more than 6 number:  ")
                char_num=input("please enter the number of charcter you want again: ")
            else:
                break
        except:
            print("[-]please our program axcept numbers only ")
            char_num=input("please enter the number of charcter you want again: ")
mypass=[]
s1=list(string.ascii_letters)
s1=random.sample(s1,len(s1))
s2=list(string.ascii_lowercase)
s2=random.sample(s2,len(s2))
s3=list(string.ascii_uppercase)
s3=random.sample(s3,len(s3))
s4=list(string.punctuation)
s4=random.sample(s4,len(s4))
cp=round((char_num*0.3))
lp=round((char_num*0.2))
for i in range(cp):
    mypass.append(s1[i])
    mypass.append(s2[i])
for i in range(lp):
    mypass.append(s3[i])
    mypass.append(s4[i])
    mypass=random.sample(mypass,len(mypass))
    spass="".join(mypass)
print(spass)




 
         
       


        
        














# #craete the window 
# window = tk.Tk()
# window.title("password generator")
# labal=tk.Label(text="My program will help you to generate password!")
# window.geometry("500x100")
# labal.pack()
# window.configure(background="gray")
# pass_length=tk.Label(window,text="length of password: ").place(x=30,y=50)
# e1=tk.Entry(window).place(x=200,y=50)
# submit_button=tk.Button(window,text="Submit").place(x=350,y=50)
# pass_result=tk.Label(window,text="Your password: ").place(x=30,y=75)

# window.mainloop()




