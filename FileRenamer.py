import os
from shutil import copyfile

def main():
    j = 0
    for filename in os.listdir('./Input/'):
        src = "./Input/" + filename
        dst = "./Output/" + filename
        copyfile(src, dst)
        oldStr = "./Output/" + filename
        newStr = "./Output/" + str(j).zfill(4) + ".jpg"
        os.rename(oldStr, newStr)
        j += 1

if __name__ == '__main__':
    main()
