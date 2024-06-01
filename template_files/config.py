import yaml


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
