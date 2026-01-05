class Extra:
    @staticmethod
    def to_bbox_coords(pos1, pos2):
        sX = min(pos1.x, pos2.x)
        sY = min(pos1.y, pos2.y)
        eX = max(pos1.x, pos2.x)
        eY = max(pos1.y, pos2.y)
        return (sX, sY, eX, eY)