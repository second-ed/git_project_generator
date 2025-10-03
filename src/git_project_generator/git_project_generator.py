from pathlib import Path

import attrs


@attrs.define
class TemplateFile:
    dst_path: Path = attrs.field(converter=Path)
    contents: str = attrs.field(default="")

    def create(self):
        self.dst_path.parent.mkdir(exist_ok=True, parents=True)
        self.dst_path.write_text(self.contents)


def create_files(root_dir: str, project_name: str, template_dir: str):
    package_name = project_name.replace("_", "-")
    package_dir = f"{root_dir.rstrip('/')}/{package_name}"

    config = [
        TemplateFile(f"{package_dir}/src/{project_name}/__init__.py"),
        TemplateFile(f"{package_dir}/tests/{project_name}/__init__.py"),
        TemplateFile(f"{package_dir}/src/{project_name}/__main__.py"),
        TemplateFile(
            f"{package_dir}/tests/{project_name}/test_main.py",
            "\n".join(["import pytest", "", "def test_main():", "    pass"]),
        ),
        TemplateFile(f"{package_dir}/src/{project_name}/adapters/__init__.py"),
        TemplateFile(f"{package_dir}/tests/{project_name}/adapters/__init__.py"),
        TemplateFile(f"{package_dir}/src/{project_name}/core/__init__.py"),
        TemplateFile(f"{package_dir}/tests/{project_name}/core/__init__.py"),
        TemplateFile(f"{package_dir}/src/{project_name}/services/__init__.py"),
        TemplateFile(f"{package_dir}/tests/{project_name}/services/__init__.py"),
        TemplateFile(f"{package_dir}/scrap/scratch.ipynb"),
        TemplateFile(f"{package_dir}/README.md"),
        TemplateFile(f"{package_dir}/envs/.env", "LOGGING_ENABLED = true"),
        TemplateFile(
            f"{package_dir}/src/{project_name}/core/logger.py",
            Path(f"{template_dir}/logger.py").read_text(),
        ),
        TemplateFile(
            f"{package_dir}/ruff.toml", Path(f"{template_dir}/ruff.toml").read_text()
        ),
        TemplateFile(
            f"{package_dir}/.pre-commit-config.yaml",
            Path(f"{template_dir}/.pre-commit-config.yaml").read_text(),
        ),
        TemplateFile(
            f"{package_dir}/.github/workflows/ci_tests.yaml",
            Path(f"{template_dir}/ci_tests.yaml").read_text(),
        ),
    ]

    for template in config:
        template.create()

    return f'cd "{package_dir}"'
