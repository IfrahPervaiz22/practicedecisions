#Practice Question for decision
#ch=1=EVEN/ODD
#EVEN/ODD
ch=input("Enter your choice:(1-5)")
ans=0
if ch=="1":
    no=eval(input("Enter a Number:"))
    if no%2==0:
        print("The number is even.")
    else:
        print("The number is odd.")
#ch=2=MARKSHEET
#MARKSHEET
elif ch=="2":
    sub1,sub2,sub3,sub4,sub5=eval(input("Enter Marks of 5 subjects:"))
    add=sub1+sub2+sub3+sub4+sub5
    tot=500
    per=add*100/tot
    print("Your percentage=",per)
    if per>=50 and per<=59:
        print("D grade")
    elif per>=60 and per<=69:
        print("C grade")
    elif per>=70 and per<=79:
        print("B grade")
    elif per>=80 and per<=89:
        print("A grade")
    elif per>=90 and per<=100:
        print("A1 grade")
    else:
        print("FAIL!")
#ch=3=AREA OF CIRCLE
#AREA OF CIRCLE
elif ch=="3":
    rad=eval(input("Enter the Radius:"))
    PI=3.142
    Area=PI*(pow(rad,2))
    print("The Area of Circle=",Area,"sq cm")
#ch=4=VOWEL/CONSONANT
#VOWEL/CONSONANT
elif ch=="4":
    alp=input("Enter a Character:").lower()
    if alp=="a" or alp=="e" or alp=="i" or alp=="o" or alp=="u":
        print(alp," is Vowel.")
    else:
        print(alp," is Consonant")
#ch=5=CALCULATOR
#CALCULATOR
elif ch=="5":
    no1,no2=eval(input("Enter two numbers:"))
    ope=(input("Write the operation you want to perform:(add,sub,mul,div,flo,exp,rem)"))
    Ans=0
    if ope=="add":
        Ans=no1+no2
        print(no1,"+",no2,"=",Ans)
    elif ope=="sub":
        Ans=no1-no2
        print(no1,"-",no2,"=",Ans)
    elif ope=="mul":
        Ans=no1*no2
        print(no1,"*",no2,"=",Ans)
    elif ope=="div":
        Ans=no1/no2
        print(no1,"/",no2,"=",Ans)
    elif ope=="rem":
        Ans=no1%no2
        print(no1,"%",no2,"=",Ans)
    elif ope=="exp":
        Ans=no1**no2
        print(no1,"**",no2,"=",Ans)
    elif ope=="flo":
        Ans=no1//no2
        print(no1,"//",no2,"=",Ans)
    else:
        print("Invalid Input")
else:
    print("ERROR!!")
        
        
        
        
        
    


    
    
    
    
        
    
    
    
    