# Git project generator
### Creates a directory structure:
```
root_project_directory
|- .github/
    |- workflows/
        |- run_tests.yaml
|- configs/
    |- example_config.yaml
|- docs/
    |- README.md
|- envs/
    |- .env
|- scrap/
    |- scratch.ipynb
|- src/
    |- __init__.py
    |- config.py
|- tests/
    |- __init__.py
|- .gitignore
|- pyproject.toml
```

### Config
specify config in config folder:
```
# where the repo will be located
root_dir: 

# where the template files are located
template_dir: 

# name of the project
project_name: 

# your name
project_author: 
```