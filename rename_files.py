import os

def rename_files(folder):
    file_list = os.listdir(folder)
    print file_list
    saved_path = os.getcwd()
    os.chdir(folder)

    for e in file_list:
        print 'Old file name: ' + e
        os.rename(e,e.translate(None,'0123456789'))
        print 'New file name ' + e.translate(None,'0123456789')
        print

    os.chdir(saved_path)

rename_files('/Users/Lazbaj/Desktop/version-control/programming_foundations_with_python/prank')
