from pypika.terms import Function


class MapRT(Function):
    """
    Custom PyPika function for roomType mapping
    """
    def __init__(self, col):
        super(MapRT, self).__init__('MAP_RT', col)
