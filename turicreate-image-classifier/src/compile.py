'''
compile

Convert a trained image classifier to another format (CoreML, TF-Lite, etc)
'''
####
# COMPILE CONFIGURATION
####
import os
import sys
import turicreate as tc


# Load Config and Args
artifacts_path = os.environ['artifacts_path']
output = os.environ['output']
model_name = os.environ['model_name']
if not model_name or not os.path.exists(artifacts_path + model_name):
    sys.exit('Must provide the name of the model to compile.')

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
