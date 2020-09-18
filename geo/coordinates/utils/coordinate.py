from scipy.spatial import distance


class CoordinateObj:
    @staticmethod
    def get_nearest(dataset, coordinate):
        return CoordinateObj._find(dataset, coordinate).argmin()

    @staticmethod
    def get_furthest(dataset, coordinate):
        return CoordinateObj._find(dataset, coordinate).argmax()

    @staticmethod
    def _find(dataset, coordinate):
        print(distance.cdist([coordinate], dataset))
        return distance.cdist([coordinate], dataset)
