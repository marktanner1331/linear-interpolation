import numpy as np

class LinearInterpolator:
    # an array of x values, in order
    _sortedDomain = []

    # a dictionary of x, y values
    _dataPointsDict = {}

    def __init__(self, dataPoints):
        for dataPoint in dataPoints:
            self._dataPointsDict[dataPoint[0]] = dataPoint[1]

        self._sortedDomain = [dataPoint[0] for dataPoint in dataPoints]
        self._sortedDomain = np.sort(self._sortedDomain)

    def interpolate(self, x):
        # find the index of the smallest element larger than x
        closest = np.searchsorted(self._sortedDomain, x)

        # find the two x values (before and after x
        x1 = self._sortedDomain[closest - 1]
        x2 = self._sortedDomain[closest]

        # and their corresponding y values
        y1 = self._dataPointsDict[x1]
        y2 = self._dataPointsDict[x2]

        # find the deltaX and deltaY
        deltaX = x2 - x1
        deltaY = y2 - y1

        # calculate the gradient
        gradient = deltaY / deltaX

        # and finally interpolate
        xPart = x - x1
        yPart = xPart * gradient

        return y1 + yPart

dataPoints = [
    [1, 28],
    [2, 21],
    [3, 96],
    [4, 96],
    [5, 120],
    [6, 87],
    [7, 50]
]

interpolator = LinearInterpolator(dataPoints)

print(interpolator.interpolate(2.4)) # 50.99999999999999
print(interpolator.interpolate(2.6)) # 66.0
