import random, string

def randomword(length):
   return ''.join(random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") for i in range(length))

def genUserID():
    User={}
    User["UserID"]=randomword(25)
    User["UserSecret"]=randomword(128)
    User["Nice"]=10
    return User

if __name__ == '__main__':
	print(genUserID())
