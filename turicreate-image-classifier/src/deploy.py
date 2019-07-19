'''
deploy

Upload a trained image classifier to the Skafos platform to deploy to iOS
'''
####
# DEPLOY CONFIGURATION
####
import os
import sys
from skafos import models

# Load Export Attributes
artifacts_path = os.environ["artifacts_path"]

# Get other variables from user
file = str(input("Enter the model filename in the artifacts/ folder to upload: "))
api_token = str(input("Enter your Skafos API TOKEN: "))
org_name = str(input("Enter your Skafos Org Name: "))
app_name = str(input("Enter your Skafos App Name: "))
model_name = str(input("Enter your Skafos Model Name: "))
description = input("Enter a description: ")

if not file or not os.path.exists(artifacts_path + file):
    sys.exit("Must provide a valid name of a model to upload.")

####
# MODEL DEPLOY CODE
####
if __name__ == "__main__":
    print("\n##### Deploying Image Classifier Model to Skafos #####", flush=True)

    # Upload with skafossdk
    res = models.upload_version(
        files=artifacts_path + file,
        description=description,
        skafos_api_token=api_token,
        org_name=org_name,
        app_name=app_name,
        model_name=model_name
    )

print("Done.", flush=True)
