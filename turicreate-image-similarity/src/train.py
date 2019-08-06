"""
train

Train a turicreate image similarity model on reference data in the data/ folder.
"""
####
# TRAINING CONFIGURATION
####
import os
import turicreate as tc

# Load Training Attributes
data_path = os.environ["data_path"]
artifacts_path = os.environ["artifacts_path"]
model_name = os.environ["model_name"]
batch_size = int(os.environ["batch_size"])
gpu = int(os.environ["gpu"])

assert os.listdir(data_path), "Data directory is empty. Nothing to train with."

####
# MODEL TRAINING CODE
####
if __name__ == "__main__":
    print("\n##### Training Image Similarity Model #####", flush=True)
    if gpu > 0:
        print("\n...Setting up GPU")
        tc.config.set_num_gpus(gpu)

    # Load the data
    print("Loading images into an sframe", flush=True)
    reference_data = tc.image_analysis.load_images(data_path)
    reference_data = reference_data.add_row_number()

    # Train the model
    print("Training the image similarity model in batches of {}\n".format(batch_size), flush=True)
    model = tc.image_similarity.create(
        dataset=reference_data,
        batch_size=batch_size
    )
    print(model.summary(), flush=True)

    # Save the model for later use
    print("Saving model", flush=True)
    model.save(artifacts_path + model_name)
    print("Done", flush=True)
