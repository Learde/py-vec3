from main import Vec3


def test_addition():
    v1 = Vec3(1, 2, 3)
    v2 = Vec3(4, 5, 6)
    result = v1 + v2
    assert result == Vec3(5, 7, 9), "Addition failed"


def test_subtraction():
    v1 = Vec3(1, 2, 3)
    v2 = Vec3(4, 5, 6)
    result = v1 - v2
    assert result == Vec3(-3, -3, -3), "Subtraction failed"


def test_scalar_multiplication():
    v1 = Vec3(1, 2, 3)
    scalar = 2
    result = v1 * scalar
    assert result == Vec3(2, 4, 6), "Scalar multiplication failed"


def test_scalar_division():
    v1 = Vec3(2, 4, 6)
    scalar = 2
    result = v1 / scalar
    assert result == Vec3(1, 2, 3), "Scalar division failed"


def test_dot_product():
    v1 = Vec3(1, 2, 3)
    v2 = Vec3(4, 5, 6)
    result = v1.dot(v2)
    assert result == 32, "Dot product calculation failed"


def test_cross_product():
    v1 = Vec3(1, 2, 3)
    v2 = Vec3(4, 5, 6)
    result = v1.cross(v2)
    assert result == Vec3(-3, 6, -3), "Cross product calculation failed"


def test_length():
    v = Vec3(3, 4, 0)
    result = v.length()
    assert result == 5, "Length calculation failed"


def test_normalize():
    v = Vec3(3, 4, 0)
    result = v.normalize()
    assert result == Vec3(0.6, 0.8, 0), "Normalization failed"
