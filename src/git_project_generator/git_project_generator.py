import os
from pathlib import Path

import attr
from attr.validators import instance_of, min_len

from ._logger import get_logger, setup_logger

setup_logger(__file__, 2)
logger = get_logger(__name__)

@attr.define
class GitProjectGenerator:
    root_dir: str = attr.ib(validator=[instance_of(str), min_len(2)])
    template_dir: str = attr.ib(validator=[instance_of(str), min_len(2)])
    project_name: str = attr.ib(validator=[instance_of(str), min_len(2)])
    project_author: str = attr.ib(validator=[instance_of(str), min_len(2)])

    def get_template_file_str(self, file_name: str) -> str:
        for k, v in locals().items():
            logger.debug(f"{k} = {v}")
        try:
            with open(f"{self.template_dir}{file_name}", "r") as f:
                file_text = f.read()
            return file_text
        except Exception as e:
            print(f"{e}: error reading {file_name}")
            return ""

    def create_file(self, file_path: str, file_text: str) -> bool:
        for k, v in locals().items():
            logger.debug(f"{k} = {v}")
        try:
            output_file = Path(file_path)
            output_file.parent.mkdir(exist_ok=True, parents=True)
            with open(output_file, "w") as file:
                file.write(file_text)
            return True
        except Exception as e:
            print(f"{e}: exception making {file_path}")
            return False

    def create_folder(self, folder_path: str) -> bool:
        for k, v in locals().items():
            logger.debug(f"{k} = {v}")
        try:
            os.makedirs(folder_path, exist_ok=True)
            return True
        except Exception as e:
            print(f"{e}: exception making {folder_path}")
            return False

    def create_git_dir(self) -> bool:
        for k, v in locals().items():
            logger.debug(f"{k} = {v}")
        project_root: str = self.root_dir + self.project_name
        folders: list[str] = [
            ".github/workflows",
            "src",
            "docs",
            "configs",
            "envs",
            "tests",
            "scrap",
        ]

        essential_files: dict[str, str] = {
            f"{project_root}/.github/workflows/run_tests.yaml": self.get_template_file_str(
                "run_tests.yaml"
            ).replace(
                "REPLACE_PROJECT_NAME", self.project_name
            ),
            f"{project_root}/configs/example_config.yaml": "# add config details here\nlogs_folder: ./logs/",
            f"{project_root}/docs/README.md": "",
            f"{project_root}/envs/.env": "# add secrets here",
            f"{project_root}/logs/general.log": "",
            f"{project_root}/scrap/scratch.ipynb": "",
            f"{project_root}/.gitignore": self.get_template_file_str(
                ".gitignore"
            ),
            f"{project_root}/pyproject.toml": self.get_template_file_str(
                "pyproject.toml"
            )
            .replace("REPLACE_PROJECT_NAME", self.project_name)
            .replace("REPLACE_PROJECT_AUTHOR", self.project_author),
            f"{project_root}/src/{self.project_name}/config.py": self.get_template_file_str(
                "config.py"
            ),
            # f"{project_root}/src/__init__.py": "",
            f"{project_root}/src/{self.project_name}/__init__.py": "",
            f"{project_root}/src/{self.project_name}/_logger.py": self.get_template_file_str(
                "_logger.py"
            ),
            f"{project_root}/src/{self.project_name}/main.py": self.get_template_file_str(
                "main.py"
            ).replace(
                "REPLACE_PROJECT_NAME", self.project_name
            ),
            f"{project_root}/tests/__init__.py": "",
            f"{project_root}/.pre-commit-config.yaml": self.get_template_file_str(
                ".pre-commit-config.yaml"
            ).replace(
                "REPLACE_PROJECT_NAME", self.project_name
            ),
            f"{project_root}/logging.ini": self.get_template_file_str(
                "logging.ini"
            ),
            f"{project_root}/ruff.toml": self.get_template_file_str(
                "ruff.toml"
            ),
        }

        try:
            for folder in folders:
                self.create_folder(f"{project_root}/{folder}")

            for k, v in essential_files.items():
                self.create_file(k, v)

            return True
        except Exception as e:
            print(f"{e}: failed to create git directory")
            return False
