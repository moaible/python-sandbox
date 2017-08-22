class HelloWorld(object):

    """A hello world simple class"""

    class_name = 'Class Method'

    def __init__(self, name ='World'):
        self.name = name

    def text(self) -> str:
        return f'Hello, {self.name}'

    @classmethod
    def class_text(cls) -> str:
        return f'Hello {cls.class_name}'
