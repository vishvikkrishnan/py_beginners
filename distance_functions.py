from math import sqrt

class DistanceFunctions:
    """
    Distance functions measure the difference between two points.
    For instance in machine learning, we often want to compute the similarity between two points that we can do by calculating the distance between them.
    """
    @staticmethod
    def euclidean_distance(X: list, Y: list) -> float:
        return sqrt(sum((x - y)**2 for x, y in zip(X, Y)))

    @staticmethod
    def hamming_distance(X: list, Y: list) -> float:
	    return sum(abs(x - y) for x, y in zip(X, Y)) / len(X)

    @staticmethod
    def manhattan_distance(X: list, Y: list) -> float:
	    return sum(abs(x - y) for x, y in zip(X, Y))

    @staticmethod
    def minkowski_distance(X: list, Y: list, order: int) -> float:
	    return sum(abs(x - y)**order for x, y in zip(X, Y))**(1 / order)


if __name__ == "__main__":
    A = [0.5, 0.5, 0.5]
    B = [1, 1, 1]
    euclidean_AB = DistanceFunctions.euclidean_distance(A, B)
    hamming_AB = DistanceFunctions.hamming_distance(A, B)
    manhattan_AB = DistanceFunctions.manhattan_distance(A, B)
    mink3_AB = DistanceFunctions.minkowski_distance(A, B, 3)
    print(f'Points {A} and {B} have distances: Euclidean {euclidean_AB}, Hamming {hamming_AB}, Manhattan {manhattan_AB} and Minkowski (3rd oder) {mink3_AB}')
