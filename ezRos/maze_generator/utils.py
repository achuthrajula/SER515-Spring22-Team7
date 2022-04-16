import random


def random_number_generator_with_minimum_distance(distance, maze_spread, itr):
    try:
        return [distance*i + x for i, x in enumerate(random.sample(range(-maze_spread*(2), 0), itr))]
    except Exception:
        return 'error'


def random_number_generator(itr):
    l = []
    for _ in range(itr):
        l.append(random.randint(0, 1))

    return(l)
