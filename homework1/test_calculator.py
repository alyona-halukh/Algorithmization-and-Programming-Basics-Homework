def test_volume():
    a = 5
    b = 4
    c = 3

    volume = a * b * c

    assert volume == 60


def test_area():
    a = 5
    b = 4
    c = 3

    area = 2 * (a * b + b * c + a * c)

    assert area == 94