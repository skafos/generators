# TensorFlow Image Classifier Generator

Parago ML Generator for a TensorFlow Image Classifier.

## Installation

Use the [Node package manager](https://www.npmjs.com/package/parago) to install parago.

```bash
npm install -g parago
```

## Usage

### Create Project
Create a project from this generator.
```bash
pgo create <name> -g tf-image-classifier
cd <name>
```

### Environment Setup
Use the prepared [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/macos.html) environment to run all commands with this generator:
```
conda env create -f environment.yml
conda activate tf-image-classifier
```

### Other Commands
Load the default Pets dataset to use right out-of-the-box.
```bash
pgo data load
```

Train an image classification model on images in the `data/` folder.
```bash
pgo train --env epochs=30,train_batch_size=128
```

Export your trained model to Core ML format:
```bash
pgo export --env output=coreml
```

Deploy your Core ML artifact with Skafos:
```bash
pgo deploy
```

Clear out the `data/` directory so you can add your own images and retrain.
```bash
pgo data clean
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[APACHE 2](https://choosealicense.com/licenses/apache-2.0/)
