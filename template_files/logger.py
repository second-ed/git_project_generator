import logging
import os
from logging.handlers import RotatingFileHandler

import attr
from attr.validators import instance_of


@attr.define
class GeneralLogger:
    log_folder_path: str = attr.ib(validator=[instance_of(str)])
    log_file_name: str = attr.ib(validator=[instance_of(str)])
    name: str = attr.ib(validator=[instance_of(str)], init=False)
    formatter: logging.Formatter = attr.ib(
        default=logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        ),
        validator=[instance_of(logging.Formatter)],
    )
    max_bytes: int = attr.ib(default=1024 * 1024, validator=[instance_of(int)])

    def __attrs_post_init__(self):
        os.makedirs(self.log_folder_path, exist_ok=True)

    def get(self, name: str) -> logging.Logger:
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)

        handlers = [
            ("general", logging.INFO),
            ("debug", logging.DEBUG),
            ("warning", logging.WARNING),
        ]

        for level_name, level in handlers:
            logger.addHandler(self.get_handler(level_name, level))

        return logger

    def get_handler(self, name: str, level: int) -> RotatingFileHandler:
        handler = RotatingFileHandler(
            f"{self.log_folder_path}/{name}_{self.log_file_name}.log",
            maxBytes=self.max_bytes,
            backupCount=1,
        )
        handler.setLevel(level)
        handler.setFormatter(self.formatter)
        return handler
