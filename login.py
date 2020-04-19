import os
import random
code='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890`~!@#$%^&*()-_=+/* '
#key=random.randint(1,9)
key=9

def main(code,key):
    usr=open("usr.txt",'a')
    pas=open("pas.txt",'a')
    def encrypt_data(message,key):
        global encrypt
        encrypt=''
        global k
        message=message+str(key)
        for i in message:
            position=code.find(i)
            newposition=(position+key)%80
            encrypt+=code[newposition]
       # print('Encryted data is: ',encrypt)
        k = encrypt[-1]

    usr=os.path.getsize("usr.txt")
    pas=os.path.getsize("pas.txt")
    if (usr and pas) == 0:                  #Checking the contents of the file, if noy present then enter the credention details for login or  login for futher use
        print("------------------------Login System----------------------")
        print("Enter the credentials for login syatem")
        u=input("Enter the username: ")
        p=input("Enter the password: ")
        encrypt_data(u,key)
        usr=open("usr.txt",'a')
        usr.write(encrypt)
        encrypt_data(p,key)
        pas=open("pas.txt",'a')
        pas.write(encrypt)
        os.access("usr.txt",os.R_OK)
        os.access("pas.txt",os.R_OK)
        usr.close()
        pas.close()
    else:
        u=input("Enter the username: ")
        p=input("Enter the password: ")
        encrypt_data(u,key)
        user = encrypt
        encrypt_data(p,key)
        passwrd = encrypt
        usr=open("usr.txt",'r')
        pas=open("pas.txt",'r')
        if(user == usr.read() and passwrd == pas.read()):
            print("Correct credential")
            #futher add the additional controls over hear
        else:
            print("incoreect credentials")
            main(code,key)
        os.system("exit")

#calling the main function
if __name__ == "__main__": 
    main(code,key)




