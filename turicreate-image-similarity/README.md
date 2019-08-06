# TuriCreate Image Similarity Generator

Parago ML Generator for a TuriCreate Image Similarity Model. With this model, given an input
image you can find K similar images from the "reference dataset" used to train the model.

## Installation

Use the [Node package manager](https://www.npmjs.com/package/parago) to install parago.

```bash
npm install -g parago
```

## Usage

### Create Project
Create a project from this generator.
```bash
pgo create <name> -g turicreate-image-similarity
cd <name>
```

### Environment Setup
Use the prepared [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/macos.html) environment to run all commands with this generator:
```
conda env create -f environment.yml
conda activate turicreate-image-similarity
```

### Other Commands
Load the default Zappos Boots dataset to use right out-of-the-box.
```bash
pgo data load --env data_src=zappos
```

Train an image similarity model on boot images in the `data/` folder.
```bash
pgo train --env batch_size=32,gpu=1
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
