amt=int(input("enter no"))
if amt%100==0: #if amt are devisable by 100 then it goes to inside if otherwise it will show else statement
    if amt>=2000:
        notes=amt/2000;  #amt mese 2000 minus karna
        print("2000 notes are",int(notes))
        amt=amt%2000  #yaha pe amount update hua
    if amt>=500:
        notes=amt/500;
        print("500 notes are",int(notes))
        amt=amt%500;
    if amt>=200:
        notes=amt/200;
        print("200 notes are", int(notes))
        amt=amt%200;
    if amt>=100:
        notes=amt/100;
        print("100 notes are",int(notes))
        amt=amt%100;
else:
    print("invalid ammount")
