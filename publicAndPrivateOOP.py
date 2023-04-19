"""

Python has the concept of public, protected, and private classes, although the distinction is not
enforced by the language itself, unlike some other languages such as Java.

In Python, class attributes and methods can be accessed from outside the class using the dot notation,
regardless of their visibility level. However, there are naming conventions that are commonly used to
indicate the visibility level of an attribute or method.


Naming Conventions:
_____________________
   -> no underscored for public.

_ -> one underscore for protected.

__ -> two underscored for private.
"""

class _ProtectedClass:

    def __init__(self,name,age,color):
        self.name = name
        self.age = age
        self.color = color

    def publicMethod(self):
        return self.name

    def _protectedMethod(self):
        return self.age

    def __privateMethod(self):
        return self.color


class __PrivateClass:

    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def publicMethod(self):
        return self.name

    def _protectedMethod(self):
        return self.age

    def __privateMethod(self):
        return self.color


class PublicClass:

    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
        self.privy = __PrivateClass(name,age,color)

    def publicMethod(self):
        return self.name

    def _protectedMethod(self):
        return self.age

    def __privateMethod(self):
        return self.color