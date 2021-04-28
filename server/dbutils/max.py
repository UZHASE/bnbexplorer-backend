from pypika.terms import Function


class Max(Function):
    """
    Custom PyPika function for SQL MAX operation
    """
    def __init__(self, col):
        super(Max, self).__init__('MAX', col)
