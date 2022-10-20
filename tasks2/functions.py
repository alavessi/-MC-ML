from os import scandir
from re import X
from typing import List


def sum_non_neg_diag(X: List[List[int]]) -> int:
    """
    Вернуть  сумму неотрицательных элементов на диагонали прямоугольной матрицы X. 
    Если неотрицательных элементов на диагонали нет, то вернуть -1
    """
    sum, diag_only_neg = 0, True
    for i in range(min(len(X), len(X[0]))):
        if X[i][i] >= 0:
            diag_only_neg = False
            sum += X[i][i]
    if diag_only_neg:
        return -1
    return sum


def are_multisets_equal(x: List[int], y: List[int]) -> bool:
    """
    Проверить, задают ли два вектора одно и то же мультимножество.
    """
    return sorted(x) == sorted(y)


def max_prod_mod_3(x: List[int]) -> int:
    """
    Вернуть максимальное прозведение соседних элементов в массиве x, 
    таких что хотя бы один множитель в произведении делится на 3.
    Если таких произведений нет, то вернуть -1.
    """
    max_prod = -1
    for i in range(len(x) - 1):
        if x[i] % 3 == 0 or x[i + 1] % 3 == 0:
            max_prod = max(max_prod, x[i] * x[i + 1])
    return max_prod


def convert_image(image: List[List[List[float]]], weights: List[float]) -> List[List[float]]:
    """
    Сложить каналы изображения с указанными весами.
    """
    wsum = [[0.0] * len(image[0]) for _ in range(len(image))]
    for i in range(len(image)):
        for j in range(len(image[0])):
            for k in range(len(weights)):
                wsum[i][j] += weights[k] * image[i][j][k]
    return wsum
    

def rle_scalar(x: List[List[int]], y:  List[List[int]]) -> int:
    """
    Найти скалярное произведение между векторами x и y, заданными в формате RLE.
    В случае несовпадения длин векторов вернуть -1.
    """
    x_dec = sum([[pair[0]] * pair[1] for pair in x], [])
    y_dec = sum([[pair[0]] * pair[1] for pair in y], [])
    if len(x_dec) != len(y_dec):
        return -1
    return sum([x_dec[i] * y_dec[i] for i in range(len(x_dec))])


def cosine_distance(X: List[List[float]], Y: List[List[float]]) -> List[List[float]]:
    """
    Вычислить матрицу косинусных расстояний между объектами X и Y. 
    В случае равенства хотя бы одно из двух векторов 0, косинусное расстояние считать равным 1.
    """
    distances = [[0.0] * len(Y) for i in range(len(X))]
    for i in range(len(X)):
        norm_x = sum(map(lambda x: x ** 2, X[i])) ** 0.5
        for j in range(len(Y)):
            norm_y = sum(map(lambda y: y ** 2, Y[j])) ** 0.5
            if norm_x == 0 or norm_y == 0:
                distances[i][j] = 1
            else:
                d = 0.0
                for k in range(len(X[i])):
                    d += X[i][k] * Y[j][k]
                distances[i][j] = d / (norm_x * norm_y)
    return distances
