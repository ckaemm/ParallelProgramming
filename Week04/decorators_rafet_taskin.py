def performance(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        start_time = time.time()
        
        try:
            result = func(*args, **kwargs)
        finally:
            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            end_time = time.time()
            
            wrapper.counter += 1
            wrapper.total_time += (end_time - start_time)
            wrapper.total_mem += peak
            
        return result
        
    wrapper.counter = 0
    wrapper.total_time = 0
    wrapper.total_mem = 0
    return wrapper
