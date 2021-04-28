from pypika.terms import Function


class RoomType(Function):
    def __init__(self, room_type):
        super(RoomType, self).__init__('MAP_RT', room_type)
