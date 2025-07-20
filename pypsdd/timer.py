import sys
import time

class Timer:
    """Utility for timing code via Python's "with" statement.

    Examples
    --------

    >>> import time
    >>> with Timer():
    ...   time.sleep(2)
    ...
    = timing ... 2.002s
    >>> with Timer("hello",prefix="# "):
    ...   time.sleep(2)
    ...
    # hello ... 2.002s
    >>> my_timer = Timer(verbose=False)
    >>> with my_timer:
    ...   time.sleep(2)
    ...
    >>> print("%.3fs (%d)" % (my_timer.total_time, my_timer.total_calls))
    2.000s (1)
    """

    def __init__(self,msg="timing",prefix="= ",verbose=True):
        self.msg = msg
        self.prefix = prefix
        self.verbose = verbose
        self.total_time = 0.0
        self.total_calls = 0

    def __enter__(self):
        if self.verbose:
            print( self.prefix + self.msg + " ... ", end="")
            sys.stdout.flush()
        self.start = time.time()
        return self

    def __exit__(self,type,value,traceback):
        elapsed = time.time()-self.start
        self.total_time += elapsed
        self.total_calls += 1
        if self.verbose:
            print( "%.3fs" % elapsed)
            sys.stdout.flush()
