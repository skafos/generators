# TuriCreate Image Classifier Generator

Parago ML Generator for a TuriCreate Image Classifier.

## Installation

Use the package manager [Homebrew](https://brew.sh/) to install parago.

```bash
brew install parago
```

## Usage

Create a project from this generator.
```bash
pgo create <name> --generator=turicreate-image-classifier
```

Load the default Cats & Dogs dataset to play right out-of-the-box.
```bash
pgo data load
```

Train an image classification model on images in the `data/` folder.
```bash
pgo train --env epochs=20,batch_size=32,gpu=1
```

Export your trained model to coreML format
```bash
pgo export --env output=coreml
```

Clear out the `data/` directory so you can add your own images and retrain.
```bash
pgo data clean
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[APACHE 2](https://choosealicense.com/licenses/apache-2.0/)
