print("Enter Source File's Name: ", end="")
sfile = input()

try:
    filehandle = open(sfile, "r")

    print("Enter Target File's Name: ", end="")
    tfile = input()
    texts = filehandle.readlines()
    filehandle.close()

    try:
        filehandle = open(tfile, "w")

        for s in texts:
            filehandle.write(s)
        filehandle.close()

        print("\nContent of \"" +sfile+ "\" gets Copied to \"" +tfile+ "\" Successfully!")
        print("\nWant to Display the Content of \"" +tfile+ "\" (y/n) ? ", end="")
        chk = input()
        if chk.lower()=='y':
            try:
                filehandle = open(tfile, "r")
                contents = filehandle.readlines()
                for s in contents:
                    print(s, end="")
                filehandle.close()
                print()
            except IOError:
                print("\nError occurred while opening the file!")

    except IOError:
        print("\nError occurred while opening/creating the file!")

except IOError:
    print("\nThe file doesn't exist!")
