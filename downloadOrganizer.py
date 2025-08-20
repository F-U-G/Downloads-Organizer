import os
import re

def main():
    # cd to Downloads directory
    os.chdir(os.environ["HOME"] + "/Downloads/") # need to add error checking here if Downloads in home dir doesnt exist

    # create list of all files in dir
    files = []
    for entry in os.listdir("."):
        if os.path.isfile(entry):
            files.append(entry)


    print(files)
    # loop over files in directory
    for file in files:
        # extract file extension, double backslash due to python string literal syntax
        p = re.compile('\\.[0-9a-z]{1,5}$', re.IGNORECASE)
        extension = p.search(file)
        name = extension.group()[1::]

        # check if file extension can go into a directory
        try:
            # put in directory
            os.rename(file, './' + name + '/' + file)
        except:
            # else mkdir then put in directory
            os.mkdir('./' + name + '/')
            os.rename(file, './' + name + '/' + file)

main()
