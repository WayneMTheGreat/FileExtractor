# Input: Directory to place files into
# Output: Files removed from sub-folders of the chosen directory.
# Processing: This program recursively removes files from all sub-folders of the current directory.
#            Once they are removed from the sub-folders they are put in the main directory.
#            Finally, all the sub-folders are deleted.

import os
import shutil
import stat

path = input('Copy and paste the directory to which you would like to copy the files: ')
realPath = os.path.abspath(path)  # this should be immutable. The main path where the files go.


def removeFromSubFolder(directory):
    print("Moving files...")
    traverseDirectories(directory)
    print("Done.")


def traverseDirectories(folder):
    # we start at the root folder that we want to move files around in.
    # we need to look at all sub folders in this root folder.
    # once we have that list we need to begin traversing them.
    # we want to go depth first and remove all files from the deepest folder.
    # we would move all of these files to the root directory.
    # we would then remove all sub-folders in this first folder we traversed.
    # we would pop back to the root directory and repeat the procedure.

    subs = os.listdir(folder)


    for sd in subs:
        subDirectory = os.path.join(folder, sd)
        if os.path.isfile(subDirectory):
            if not subDirectory == realPath:
                (head, tail) = os.path.split(subDirectory)
                try:
                    shutil.copyfile(os.path.abspath(subDirectory), os.path.join(realPath, tail))
                    os.chmod(os.path.abspath(subDirectory), stat.S_IWRITE)
                    os.remove(subDirectory)
                except shutil.SameFileError:
                    pass
            else:
                return

        elif os.path.isdir(subDirectory):  # enter it
            traverseDirectories(subDirectory)

        else:
            print('we shouldn\'t be here.')
            # handle the miscellaneous errors later.
            return




def removeFolders(path):
    subs = os.listdir(path)
    print("Cleaning up sub-folders...")
    for sd in subs:
        subPath = os.path.join(path, sd)
        if os.path.isdir(subPath):
            shutil.rmtree(subPath)
        else:
            continue

    print("Done.")


removeFromSubFolder(realPath)
removeFolders(realPath)
