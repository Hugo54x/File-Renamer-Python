import os
from shutil import copyfile

def main():
    j = 0
    for filename in os.listdir('./Input/'):

        src = "./Input/" + filename
        dst = "./Output/" + filename
        copyfile(src, dst)
        src = "./Output/" + filename
        dst = src + "_" + str(j) + ".jpg"
        os.rename(src, dst)
        j += 1

if __name__ == '__main__':
    main()
