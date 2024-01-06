def perform_task():
    pass


def generator_func(max_iterations):
    count = 0
    while count < max_iterations:
        yield perform_task
        count += 1


for task in generator_func(100):
    task()
