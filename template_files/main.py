from src.REPLACE_PROJECT_NAME.config import (
    Config,
    get_dir_path,
    get_logger,
    setup_logger,
)

Config().set_filepath(get_dir_path(__file__, 2, "configs/example_config.yaml"))

setup_logger(__file__, 2)
logger = get_logger(__name__)
