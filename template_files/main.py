import logging

from src.REPLACE_PROJECT_NAME._logger import (
    get_dir_path,
    setup_logger,
)
from src.REPLACE_PROJECT_NAME.config import Config

Config().set_filepath(get_dir_path(__file__, 2, "configs/example_config.yaml"))

setup_logger(__file__, 2)
logger = logging.getLogger()
