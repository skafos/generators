'''
train.py

This is where training of the model occurs.  Please look at the
config.ini file for details on where things are hooked up.
'''
####
# TRAINING CONFIGURATION
####
import os
import argparse
import yaml
import turicreate as tc

# Parse (optional) args
parser = argparse.ArgumentParser(description='Ska ML CLI Tool')
parser.add_argument('--data_path', type=str, default=None)
parser.add_argument('--dataset', type=str, default=None)
parser.add_argument('--save_dataset', type=bool, default=False)
parser.add_argument('--artifacts_path', type=str, default=None)
parser.add_argument('--model_name', type=str, default=None)
parser.add_argument('--training_split', type=float, default=None)
parser.add_argument('--epochs', type=int, default=None)
parser.add_argument('--batch_size', type=int, default=None)
parser.add_argument('--gpu', type=int, default=None)
args = parser.parse_args()

# Parse config
config = ""
with open("config.yaml", 'r') as stream:
    try:
        config=yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)
c_default = dict(config['DEFAULT'].items())
c_train = dict(config['TRAIN'].items())

# Load Config File by Default
dataset = args.dataset
save_dataset = args.save_dataset
data_path = args.data_path or c_default['data_path']
artifacts_path = args.artifacts_path or c_default['artifacts_path']
model_name = args.model_name or c_default['model_name']
training_split = args.training_split or float(c_train['training_split'])
epochs = args.epochs or int(c_train['epochs'])
batch_size = args.batch_size or int(c_train['batch_size'])
gpu = args.gpu or int(c_train['gpu'])

####
# MODEL TRAINING CODE
####
if __name__ == "__main__":
    print("##### Training Image Classifier Model #####")
    if gpu > 0:
        print("\n...Setting up GPU")
        tc.config.set_num_gpus(gpu)

    # Load the data
    if dataset:
        if not os.path.exists(artifacts_path + dataset):
            sys.exit("The provided dataset doesn't exist.")
        print("...Loading previously processed training dataset")
        data =  tc.SFrame(artifacts_path + dataset)
    else:
        if not os.listdir(data_path):
            sys.exit("data/ folder is empty... make sure to put folders of images here before training.")
        print("...Loading images into an sframe")
        data = tc.image_analysis.load_images(data_path, with_path=True)
        data['label'] = data['path'].apply(lambda path: os.path.basename(os.path.dirname(path)))
        if save_dataset:
            # for no save it to a default name... later allow users to configure?
            data.save(artifacts_path + "training_data.sframe")

    # Make a train-test split for evaluation purposes
    if training_split:
        print("...Using {} of the provided data for training".format(training_split))
        train_data, test_data = data.random_split(training_split)
    else:
        train_data = data
        test_data = None

    # Train the model
    print("...Training the image classifier for {} epochs with in batches of {}\n".format(epochs, batch_size))
    model = tc.image_classifier.create(
        dataset=train_data,
        target='label',
        max_iterations=epochs,
        batch_size=batch_size
    )

    # Evaluate the trained model and print the results
    print("\n\nFinished Training")
    if test_data:
        metrics = model.evaluate(test_data)
        print("Model accuracy on test data: {}".format(metrics['accuracy']))

    # Save the model for later use
    print("Saving model")
    model.save(artifacts_path + model_name)
    print("Done")
    print("Generated with Love by Skafos")