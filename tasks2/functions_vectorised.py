import numpy as np


def sum_non_neg_diag(X: np.ndarray) -> int:
    """
    Вернуть  сумму неотрицательных элементов на диагонали прямоугольной матрицы X.
    Если неотрицательных элементов на диагонали нет, то вернуть -1
    """
    d = np.diagonal(X)
    if np.all(d < 0):
        return -1
    return np.sum(d[d >= 0])


def are_multisets_equal(x: np.ndarray, y: np.ndarray) -> bool:
    """
    Проверить, задают ли два вектора одно и то же мультимножество.
    """
    return np.array_equal(np.sort(x), np.sort(y))


def max_prod_mod_3(x: np.ndarray):
    """
    Вернуть максимальное прозведение соседних элементов в массиве x,
    таких что хотя бы один множитель в произведении делится на 3.
    Если таких произведений нет, то вернуть -1.
    """
    p = x[1:] * x[:-1]
    p = p[p % 3 == 0]
    if len(p) == 0:
        return -1
    return p.max()


def convert_image(image: np.ndarray, weights: np.ndarray) -> np.ndarray:
    """
    Сложить каналы изображения с указанными весами.
    """
    return np.dot(image, weights)


def rle_scalar(x: np.ndarray, y: np.ndarray) -> int:
    """
    Найти скалярное произведение между векторами x и y, заданными в формате RLE.
    В случае несовпадения длин векторов вернуть -1.
    """
    x_dec = np.repeat(x.T[0], x.T[1])
    y_dec = np.repeat(y.T[0], y.T[1])
    if len(x_dec) != len(y_dec):
        return -1
    return np.dot(x_dec, y_dec)


def cosine_distance(X: np.ndarray, Y: np.ndarray) -> np.ndarray:
    """
    Вычислить матрицу косинусных расстояний между объектами X и Y.
    В случае равенства хотя бы одно из двух векторов 0, косинусное расстояние считать равным 1.
    """
    norm = np.outer(np.linalg.norm(X, axis=1), np.linalg.norm(Y, axis=1))
    flag = norm != 0
    cos_dist = np.ones((len(X), len(Y)))
    cos_dist[flag] = np.dot(X, Y.T)[flag] / norm[flag]
    return cos_dist
