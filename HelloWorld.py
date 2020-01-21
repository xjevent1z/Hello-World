from datetime import datetime
"""
```python
    >>> from HelloWorld import HelloWorld
    >>> agent = HelloWorld()
    >>> print(agent)
    Hello World!
```
"""
__author__ = 'David Chou'
__copyright__ = "Copyright {}, David Chou".format(datetime.now().year)
__credits__ = ['David Chou']
__license__ = 'GPL'
__version__ = '1.0.0'
__maintainer__ = "David Chou"
__email__ = "qq3025566@gmail.com"
__status__ = "Production"  #  Prototype, Development, or "Production"


class HelloWorld:
    string = str()

    def __init__(self):
        self.string = 'Hello World!'
    
    def __str__(self):
        return self.string

    def __call__(self):
        self.string = 'Fuck the World!'

if __name__ == "__main__":
    agent = HelloWorld()
    print(agent)