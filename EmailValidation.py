email=input("Enter your email-id:")# a@a.in
flag,f1,k=0,0,0
if len(email)>=8:
    if email[0].isalpha():#checks if alphabet or not
        if "@" in email and email.count("@")==1:
            if (email[-3]==".") ^ (email[-4]=="."):#xor operation same 0 diff 1
                for i in email:#to check for spaces
                    if i==" ":
                        k=1
                    elif i.isalpha():#checks for Uppercases
                        if i==i.upper():
                            f1=1
                    elif i.isdigit():#checks for 0-9
                        continue
                    elif i=="_" or i=="." or i=="@": #no problem
                        continue
                    else:#if other than these any other special char(s)
                        k=1


                if flag==1 or f1==1 or k==1:
                    print("spaces,uppercase,special char(s) other than [@,_,.]  not allowed")
                else:
                    print(" Email-id is valid ")

            else:
                print(". must be in its correct position")

        else:
            print("@ must be present in an email-id and it's count should be one!")

    else:
        print("The first char of the email-id should be an alphabet")


else:
    print("email-id should be atleast 8 char(s) long!")