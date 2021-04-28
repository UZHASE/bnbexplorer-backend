from pypika.terms import Function


class Normalize(Function):
    """
    Custom PyPika function to perform normalization
    """
    def __init__(self, val, min, max):
        super(Normalize, self).__init__('NORM', val, min, max)
