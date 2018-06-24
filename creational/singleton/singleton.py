

class __Config(object):

    @property
    def foo(self):
        return 'foo'

    @property
    def bar(self):
        return 'bar'


_config = __Config()


class Config(object):

    @staticmethod
    def instance():
        return _config

