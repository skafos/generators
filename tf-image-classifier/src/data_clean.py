"""
data-clean

Remove all data from the data/ dir.
"""
####
# DATA CLEAN CONFIGURATION
####
import os
import shutil

# Load Data Clean Attributes
data_path = os.environ["data_path"]
assert os.path.exists(data_path), "Data directory path doesn't exist."

####
# DATA CLEAN CODE
####
if __name__ == "__main__":
    print("\n##### Cleaning Image Classifier Data #####", flush=True)

    v = input("Sure you want to remove data in the {} directory (y/n): ".format(data_path))
    if v.lower().strip() in ("y", "yes"):
        # ignore dot files
        files = [file for file in os.listdir(data_path) if not file.startswith(".")]
        for f in files:
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
        print("Ok. Leaving data directory as is.", flush=True)
