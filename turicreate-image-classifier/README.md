# TuriCreate Image Classifier

This is a Skafos Generator package for a TuriCreate Image Classifier.

## Installation

Use the package manager [Homebrew](https://brew.sh/) to install skafos.

```bash
brew install ska
```

## Usage

```bash
ska <your-model-name> --generator=turicreate-image-classifier
```

Train your model from raw data in the `data/` folder
```bash
ska train --epochs 20 --batch_size 32
```

Train your model from a previously processed dataset
```bash
ska train --epochs 20 --batch_size 32 --dataset mydata.sframe
```

```bash
ska compile ImageClassifier --output coreml
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[APACHE 2](https://choosealicense.com/licenses/apache-2.0/)
