class Student(object):
    def __init__(self):
        self._score = 0;

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


a = Student()
print(a.score)
a.score = 101
print(a.score)
