"""
Programming for linguists

Implementation of some exceptions
"""

class Existed(Exception):
    """Exception raised for data nodes that are already in a tree.

        Attributes:
            data -- input data node
            message -- explanation of the error
        """

    def __init__(self, data, message="Node cannot be inserted because it's already in a tree."):
        self.data = data
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.data} -> {self.message}'

class NotExisted(Exception):
    """Exception raised for data nodes that are already in a tree.

        Attributes:
            data -- input data node
            message -- explanation of the error
        """

    def __init__(self, data, message="Node cannot be used because their is no such a node"):
        self.data = data
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.data} -> {self.message}'
