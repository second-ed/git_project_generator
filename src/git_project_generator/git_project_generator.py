import os
from pathlib import Path


def create_files(root_dir: str, project_name: str, template_dir: str):
    package_name = project_name.replace("_", "-")
    package_dir = f"{root_dir}/{package_name}"
    os.makedirs(package_dir, exist_ok=True)

    config = [
        (f"{package_dir}/src/{project_name}/__init__.py", ""),
        (f"{package_dir}/src/{project_name}/__main__.py", ""),
        (f"{package_dir}/tests/__init__.py", ""),
        (
            f"{package_dir}/tests/test_main.py",
            "\n".join(["import pytest", "", "def test_main():", "    pass"]),
        ),
        (f"{package_dir}/configs/config.yaml", ""),
        (f"{package_dir}/docs/dev_readme.md", ""),
        (f"{package_dir}/logs/general.log", ""),
        (f"{package_dir}/scrap/scratch.ipynb", ""),
        (
            f"{package_dir}/.pre-commit-config.yaml",
            get_template_file_str(f"{template_dir}/.pre-commit-config.yaml"),
        ),
        (
            f"{package_dir}/ruff.toml",
            get_template_file_str(f"{template_dir}/ruff.toml"),
        ),
        (
            f"{package_dir}/.gitignore",
            get_template_file_str(f"{template_dir}/.gitignore"),
        ),
        (
            f"{package_dir}/.github/workflows/ci_tests.yaml",
            get_template_file_str(f"{template_dir}/ci_tests.yaml"),
        ),
    ]

    for file, contents in config:
        create_file(file, contents)

    return f'cd "{package_dir}"'


def get_template_file_str(path: str) -> str:
    try:
        with open(path, "r") as f:
            file_text = f.read()
        return file_text
    except Exception as e:
        print(f"{e}: error reading {path}")
        return ""


def create_file(file_path: str, file_text: str) -> bool:
    try:
        output_file = Path(file_path)
        output_file.parent.mkdir(exist_ok=True, parents=True)
        with open(output_file, "w") as file:
            file.write(file_text)
        return True
    except Exception as e:
        print(f"{e}: exception making {file_path}")
        return False
