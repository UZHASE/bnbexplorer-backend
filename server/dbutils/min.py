from pypika.terms import Function


class Min(Function):
    """
    Custom PyPika function for SQL MIN operation
    """
    def __init__(self, col):
        super(Min, self).__init__('MIN', col)
