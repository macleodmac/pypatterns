from creational.singleton.singleton import Config


config = Config().instance()
print(config)

another_config = Config().instance()
print(config is another_config)
