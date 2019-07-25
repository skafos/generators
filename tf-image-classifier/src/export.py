'''
export

Convert a trained image classifier (saved_model.pb) to another format (CoreML, TF-Lite, etc)
'''
####
# EXPORT CONFIGURATION
####
import os
import tfcoreml as tf_converter

# Load Export Attributes
artifacts_path = "artifacts/"#os.environ["artifacts_path"]
output = "coreml"#os.environ["output"]
model_name = "ImageClassifier"#os.environ["model_name"]
final_tensor_name = "final_result"#os.environ["final_tensor_name"]

assert output == 'coreml', "Sorry! Other output formats are not yet supported!"

####
# MODEL EXPORT CODE
####
if __name__ == "__main__":
    print("\n##### Exporting Image Classifier Model #####", flush=True)
    print("Loading model and converting", flush=True)
    coreml_model_name = artifacts_path + model_name.strip(".pb") + ".mlmodel"
    tf_converter.convert(
        tf_model_path=artifacts_path + model_name + ".pb",
        mlmodel_path=coreml_model_name,
        output_feature_names=[final_tensor_name + ":0"]
    )

    print("Done.", flush=True)
