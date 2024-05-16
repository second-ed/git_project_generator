import logging
import logging.config

from src.{REPLACE_PROJECT_NAME}.config import Config

Config().set_filepath("./configs/example_config.yaml")
logging.config.fileConfig('./logging.ini', defaults={"root": Config().logs_folder})
logger = logging.getLogger(__name__)

