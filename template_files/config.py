import logging
import logging.config
from pathlib import Path

import yaml


def setup_logger(file, idx) -> bool:
    logging.config.fileConfig(
        get_dir_path(file, idx, "logging.ini"),
        defaults={"root": get_dir_path(file, idx, "logs")},
    )
    return True


def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)


def get_dir_path(src: str, idx: int, dst: str) -> str:
    curr_dir = Path(src).parents[idx]
    return str(curr_dir.joinpath(dst)).replace("\\", "/")


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Config(metaclass=SingletonMeta):
    @classmethod
    def set_filepath(cls, filepath: str) -> None:
        cls._filepath: str = filepath
        cls.read_config()

    @classmethod
    def read_config(cls) -> None:
        cls._config_data = {}
        if cls._filepath is None:
            raise ValueError("No config file specified")
        with open(cls._filepath, "r") as file:
            try:
                cls._config_data = yaml.safe_load(file)
            except yaml.YAMLError as e:
                print(f"Error loading YAML file: {e}")
        if cls._config_data:
            for k, v in cls._config_data.items():
                setattr(cls, k, property(lambda cls, val=v: val))
