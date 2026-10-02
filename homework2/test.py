def test_sum_of_squares():
    number = 245

    a = number // 100
    b = number // 10 % 10
    c = number % 10

    result = a ** 2 + b ** 2 + c ** 2

    assert result == 45