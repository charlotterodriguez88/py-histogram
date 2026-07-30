from percentile import Samples


def test_p():
    s = Samples()
    for i in range(1, 101):
        s.add(i)
    assert s.percentile(50) in (50, 51)
    assert s.percentile(99) in (99, 100)
