import pytest

@pytest.mark.parametrize("testPoints, testX ,expected", [
    [((0,0),(1,1)),2,2],
    [((1,1),(0,0)),5,5]
])
def test_line_calc(testPoints, testX, expected):
    from line import line_calc
    answer = line_calc(testPoints, testX)
    assert answer == expected

@pytest.mark.parametrize("x1,x2,y1,y2,expected", [
    [1,2,1,2,1],
    [4,5,4,5,1]
])
def test_slope_calc(x1,x2,y1,y2,expected):
    from line import slope_calc
    answer = slope_calc(x1,x2,y1,y2)
    assert answer == expected