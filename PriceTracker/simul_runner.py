import manage, continuous_runner
import multiprocessing

for process in ('manage'):
    p = multiprocessing.Process(target=lambda: __import__(process))
    p.start()

