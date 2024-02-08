import pytest

class NotInRange(Exception):
    def __init__(self, message="not in range error"):
        self.message =message
        super().__init__(self.message)


def test_generic():
    a=2
    with pytest.raises(NotInRange):
        if a not in range(10,20):
            raise NotInRange
    