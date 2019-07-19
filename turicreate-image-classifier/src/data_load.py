"""
data-load

Pre-load some sample data for running this generator out-of-the-box.
"""
####
# DATA LOAD CONFIGURATION
####
import os
import sys
import shutil
import urllib.request
import tarfile

# Load Data Load Attributes
data_path = os.environ["data_path"]
data_src = os.environ["data_src"]

data_sources = {
    "cats_dogs": "https://s3.amazonaws.com/skafos.example.data/ImageClassifier/PetImages.tar.gz",
    "more_pets": "https://s3.amazonaws.com/skafos.example.data/ImageClassifier/MorePets.tar.gz",
    "poison_plants": "https://s3.amazonaws.com/skafos.example.data/ImageClassifier/poisonPlants.tar.gz"
}


####
# DATA LOAD CODE
####
if __name__ == "__main__":
    print("\n##### Loading Image Classifier Sample Data #####", flush=True)

    existing_files = os.listdir(data_path)

    if existing_files:
        if (len(existing_files) == 1) and existing_files[0] == ".gitkeep":
            pass
        elif (len(existing_files) == 1) and existing_files[0] != ".gitkeep":
            sys.exit("Your data/ directory is not empty. Run data-clean first!")
        elif len(existing_files) > 1:
            sys.exit("Your data/ directory is not empty. Run data-clean first!")


    # Specify the data set download url and path
    data_url = data_sources.get(data_src)
    if not data_url:
        sys.exit("Non-supported data source - {} - passed in.".format(data_src))

    images_tar_path = data_url.split("/")[-1]
    images_path = images_tar_path.split('.')[0] + "/"

    # Pull the compressed data and extract
    print("Pulling images from {}".format(data_url), flush=True)
    retrieve = urllib.request.urlretrieve(data_url, data_path + images_tar_path)
    tar = tarfile.open(data_path + images_tar_path)
    tar.extractall(data_path)
    tar.close()
    # Remove the tar file
    os.remove(data_path + images_tar_path)
    # Move all image class folders up a level
    for cls in os.listdir(data_path + images_path):
        f = data_path + images_path + cls
        shutil.move(f, data_path)
    # Remove old artifact
    shutil.rmtree(data_path + images_path)


    print("Done retrieving and unpacking data.", flush=True)
