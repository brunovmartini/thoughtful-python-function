import pytest
from thoughtful.thoughtful_sort import sort

def test_standard_package():
    assert sort(10, 10, 10, 5) == "STANDARD"

def test_bulky_package():
    assert sort(200, 100, 100, 10) == "SPECIAL"

def test_bulky_package_with_large_dimension():
    assert sort(100, 100, 200, 10) == "SPECIAL"

def test_heavy_package():
    assert sort(50, 50, 50, 25) == "SPECIAL"

def test_rejected_package():
    assert sort(200, 200, 200, 25) == "REJECTED"

def test_zero_dimensions():
    with pytest.raises(ValueError, match="Dimensions and mass must be greater than zero."):
        sort(0, 100, 100, 10)

def test_zero_mass():
    with pytest.raises(ValueError, match="Dimensions and mass must be greater than zero."):
        sort(10, 10, 10, 0)

def test_negative_width():
    with pytest.raises(ValueError, match="Dimensions and mass must be greater than zero."):
        sort(-10, 100, 100, 10)

def test_negative_height():
    with pytest.raises(ValueError, match="Dimensions and mass must be greater than zero."):
        sort(100, -10, 100, 10)

def test_negative_length():
    with pytest.raises(ValueError, match="Dimensions and mass must be greater than zero."):
        sort(100, 100, -10, 10)

def test_negative_mass():
    with pytest.raises(ValueError, match="Dimensions and mass must be greater than zero."):
        sort(100, 100, 100, -10)

def test_non_numeric_width():
    with pytest.raises(ValueError, match="All inputs must be numeric."):
        sort("a", 100, 100, 10)

def test_non_numeric_height():
    with pytest.raises(ValueError, match="All inputs must be numeric."):
        sort(100, "b", 100, 10)

def test_non_numeric_length():
    with pytest.raises(ValueError, match="All inputs must be numeric."):
        sort(100, 100, "c", 10)

def test_non_numeric_mass():
    with pytest.raises(ValueError, match="All inputs must be numeric."):
        sort(100, 100, 100, "d")
