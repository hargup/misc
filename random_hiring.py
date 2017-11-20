import numpy as np

class person(object):
    def __init__(self, grade):
        self.grade = grade

    def get_real_val(self):
        if self.grade is "Good":
            return np.random.normal(10, 5)
        if self.grade is "Average":
            # Average graders have lower average but higher variance than high
            # graders
            return np.random.normal(5, 25)

good_graders = [person('Good') for i in range(1000)]
average_graders = [person('Average') for i in range(1000)]

def get_selection_value(N, M):
    # The simulates the interview process, we have a fixed size pool of
    # candidaes who are interviewed to get their real value
    # N: The total size of the pool
    # M: The number of high graders in the pool

    selects = list(np.random.choice(good_graders, M))
    selects.extend(np.random.choice(average_graders, N-M))
    vals = [x.get_real_val() for x in selects]
    good_enough = filter(lambda x: x>8, vals)
    return sum(good_enough)

runs = 100
N = 20
for i in range(21):
    print("good graders: %s, average graders: %s, average utitlity: %s" %
            (i, N-i, sum([get_selection_value(N, i) for x in range(runs)])/runs))

# This is monotonic it is better to take just one group and leave the rest than
# taking a combination
