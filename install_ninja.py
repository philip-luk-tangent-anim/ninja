import os
import shutil
import errno


def CreateDir(dirpath):
    """
    Create a directory if it doesn't exist.  
    """
    try:
        os.makedirs(dirpath)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(dirpath):
            pass
        else:
            raise

"""
Copy the ninja executable files to the REZ package 'bin' directory.
"""
if __name__ == "__main__":
    target_install_dir = os.path.join(os.environ.get('REZ_BUILD_INSTALL_PATH'), 'bin')
    print("target_install_dir: {}".format(target_install_dir))
    CreateDir(target_install_dir)

    files = [f for f in os.listdir(os.environ.get('REZ_BUILD_PATH')) if os.path.isfile(f) and os.access(f, os.X_OK)] 
    for file in files:
        print("Copying {} to {}".format(file, target_install_dir))
        shutil.copy2(file, target_install_dir)
