'''
export

Convert a trained image classifier to another format (CoreML, TF-Lite, etc)
'''
####
# EXPORT CONFIGURATION
####
import os
import turicreate as tc


# Load Export Attributes
artifacts_path = os.environ["artifacts_path"]
output = os.environ["output"]
model_name = os.environ["model_name"]

assert output == 'coreml', "Sorry! Other output formats are not yet supported!"
assert os.path.exists(artifacts_path + model_name), "Must provide the name of the model to compile."

####
# MODEL EXPORT CODE
####
if __name__ == "__main__":
    print("\n##### Exporting Image Classifier Model #####", flush=True)
    print("Loading model", flush=True)

    model = tc.load_model(artifacts_path + model_name)

    print("Exporting to CoreML format!", flush=True)
    model.export_coreml(artifacts_path + model_name + ".mlmodel")

    print("Done.", flush=True)
