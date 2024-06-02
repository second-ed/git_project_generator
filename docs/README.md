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
|- logs/
    |- general.log
|- scrap/
    |- scratch.ipynb
|- src/
    |- project_name/
        |- __init__.py
        |- _logger.py
        |- config.py
        |- main.py
|- tests/
    |- __init__.py
|- .gitignore
|- logging.ini
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
