def test_check_HDL1():
    from interface import check_HDL
    answer = check_HDL(70)
    assert answer == "Normal"

def test_check_HDL2():
    from interface import check_HDL
    answer = check_HDL(30)
    assert answer == "Low"

def test_check_HDL3():
    from interface import check_HDL
    answer = check_HDL(50)
    assert answer == "Borderline Low"