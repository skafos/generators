'''
compile.py

This is where we convert a trained model to a different format.
'''
####
# COMPILE CONFIGURATION
####
import os
import sys
import argparse
import configparser
import turicreate as tc

# Parse args
parser = argparse.ArgumentParser(description='Ska ML CLI Tool')
parser.add_argument('model_name', type=str, default=None)
parser.add_argument('--artifacts_path', type=str, default=None)
parser.add_argument('--output', type=str, default='coreml')
args = parser.parse_args()

# Parse config
config = ""
with open("config.yaml", 'r') as stream:
    try:
        config=yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

# Load Config and Args
artifacts_path = args.artifacts_path or config['DEFAULT']['artifacts_path']
output = args.output
model_name = args.model_name
if not model_name or not os.path.exists(artifacts_path + model_name):
    sys.exit('Must provide a model to compile.')

####
# MODEL COMPILE CODE
####
if __name__ == "__main__":
    print("##### Compling Image Classifier Model #####")
    print("...Loading model")
    model = tc.load_model(artifacts_path + model_name)

    if output == 'coreml':
        print("...Exporting to CoreML format!")
        model.export_coreml(artifacts_path + model_name + '.mlmodel')
    else:
        sys.exit("Sorry we don't support other types of output formats yet!")

print("Done")
