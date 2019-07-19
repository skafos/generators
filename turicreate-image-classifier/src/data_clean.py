"""
data-clean

Remove all data from the data/ dir.
"""
####
# DATA CLEAN CONFIGURATION
####
import os
import sys
import shutil

# Load Data Clean Attributes
data_path = os.environ["data_path"]


####
# DATA CLEAN CODE
####
if __name__ == "__main__":
    print("\n##### Cleaning Image Classifier Data #####", flush=True)

    if os.path.exists(data_path):
        v = input("Are you sure you want to clean all data in the {} directory (y/n):".format(data_path))
        if v.lower().strip() in ("y", "yes"):
            for f in os.listdir(data_path):
                if f == ".gitkeep":
                    continue
                f_path = os.path.join(data_path, f)
                try:
                    if os.path.isfile(f_path):
                        os.remove(f_path)
                    elif os.path.isdir(f_path):
                        shutil.rmtree(f_path)
                except Exception as e:
                    print(e)
            print("Done.", flush=True)
        else:
            sys.exit("Ok. Leaving data directory as is.")
    else:
        sys.exit("Data directory path doesn't exist.")
