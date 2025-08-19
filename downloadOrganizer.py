import os

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

        # check if file extension can go into a directory
            # put in directory

            # else mkdir then put in directory

main()
