import random, string

def randomword(length):
   return ''.join(random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") for i in range(length))

def genTaskID():
    return randomword(128)

if __name__ == '__main__':
	print(genTaskID())