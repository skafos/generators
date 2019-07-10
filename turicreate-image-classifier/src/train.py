"""
train

Train a turicreate image classifier on data in the data/ directory.
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
training_split = float(os.environ["training_split"])
epochs = int(os.environ["epochs"])
batch_size = int(os.environ["batch_size"])
gpu = int(os.environ["gpu"])


####
# MODEL TRAINING CODE
####
if __name__ == "__main__":
    print("\n##### Training Image Classifier Model #####", flush=True)
    if gpu > 0:
        print("\n...Setting up GPU")
        tc.config.set_num_gpus(gpu)

    # Load the data
    if not os.listdir(data_path):
        sys.exit("data/ folder is empty... Try running data-load or add your own image folders")
    print("...Loading images into an sframe", flush=True)
    data = tc.image_analysis.load_images(data_path, with_path=True)
    data["label"] = data["path"].apply(lambda path: os.path.basename(os.path.dirname(path)))

    # Make a train-test split for evaluation purposes
    if training_split:
        print("...Using {} of the provided data for training".format(training_split), flush=True)
        train_data, test_data = data.random_split(training_split)
    else:
        train_data = data
        test_data = None

    # Train the model
    print("...Training the image classifier for {} epochs with in batches of {}\n".format(epochs, batch_size), flush=True)
    model = tc.image_classifier.create(
        dataset=train_data,
        target="label",
        max_iterations=epochs,
        batch_size=batch_size
    )

    # Evaluate the trained model and print the results
    print("\n\nFinished Training", flush=True)
    if test_data:
        metrics = model.evaluate(test_data)
        print("Model accuracy on test data: {}".format(metrics["accuracy"]), flush=True)

    # Save the model for later use
    print("Saving model", flush=True)
    model.save(artifacts_path + model_name)
    print("Done. Generated with Love by Skafos", flush=True)
