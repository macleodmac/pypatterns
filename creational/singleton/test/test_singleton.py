from creational.singleton.singleton import Config


def test_multiple_config_objects_are_the_same_object():
    # act
    config = Config().instance()
    another_config = Config().instance()

    # assert
    assert config is another_config
