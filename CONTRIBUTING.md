# Contributing
Thanks for helping out! Making Parago Generators will eventually be a more automated process. We want to make sure the default file structure and command templates work well. Please send us feedback/ideas so we can get that ironed out soon! In the meantime, please follow these guidelines and steps to create a generator.

## Making a Generator
### Requirements
- Only **Python 3+** is officially supported at the moment.
- Must include the following files:
    - a conda environment file: `environment.yml` at the root level
    - a parago config file: `parago.yml` at the root level
    - empty `data/` and `artifacts/` subfolders with a `.gitkeep` file inside each
    - a `LICENSE` file (we like APACHE 2) at the root level
    - a `README.md` file showing usage of your generator
    - a `src/` subfolder that contains the code

**Example**
```
my-generator/
    artifacts/
        .gitkeep
    data/
        .gitkeep
    src/
        train.py
        export.py
        deploy.py
        data_clean.py
        data_load.py
    environment.yml
    parago.yml
    LICENSE
    README.md
```
See the two examples in this repository for how these files should look.

### Parago Commands
**Commands** are pre-defined wrappers around code & logic that YOU write. There are 5 high level commands that Parago supports out of the box. Each command is defined in the `parago.yml` file under `commands:`.

1. `pgo data load`: Each generator should include a way to get some sample training data into the `data/` folder. Otherwise your user will not be able to do anything. Often this involves making a network call to S3 or some other hosting service to download same pre-processed data. This command refers to `src/data_load.py`.

2. `pgo train`: This is the most universal step for all ML generators. Take training data in the `data/` folder, load it up, and train a model. This command often makes use of several different params outlined in the config. Store the resulting model in the `artifacts/` folder. This command refers to `src/train.py`.

3. `pgo export`: Takes a trained model artifact and converts it to another format. CoreML and TFLite are the two most common examples as these are formats required for mobile apps. This command refers to `src/export.py`.

4. `pgo deploy`: Delivers the trained model to some external service. The initial examples deploy the model to the Skafos platform. This command refers to `src/deploy.py`.

5. `pgo data clean`: This step cleans out (removes) all data in the `data/` folder so the user can start again with a different dataset. Eventually this command will be brought in-house and handled by Parago directly. This command refers to `src/data_clean.py`.


### Parago Tasks
**Tasks** are just like commands except they are 100% defined by YOU. Include any additional steps in the `tasks:` section of the `parago.yml` file. Users can run your tasks with: `pgo run <task-name>`. That way if there are any custom steps of your workflow that aren't covered by the 5 commands above, you can still include them.


### Parago Env
As a way to parametrize the way Parago executes your defined commands, define default params/args in the `parago.yml` file under `env:`. These values can be overridden at runtime if the user passes the `--env` flag followed by key-value pairs:
```bash
$ pgo train --env epochs=5,batch_size=20
```

These values will then be included in the Python runtime environment when the code is run. We might figure out a way to make this better in the future.


## Submissions
Check out a branch and make a PR against master. We will review and test your generator before merging. We recognize we don't have the best way to test these generators against `pgo` yet. That will be addressed this sprint.


## Final Note
Parago is the wrapper around the commands that YOU write. Think with the end user in mind. The 5 high level commands are: `data load`, `data clean`, `train`, `export`,
and `deploy`. Outside of that, feel free to add other tasks that make sense for your workflow: data preprocessing steps, post-training steps, etc. Enjoy!
