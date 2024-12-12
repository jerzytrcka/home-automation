def verify_initialized(func):
    ''' Decorator to check if the connection has been initialized. If not, it attempts an initialization.
    If initialization fails, it calls the fallback method. '''

    def decorator(self, *args, **kwargs):
        if not self.initialized:
            self.initialize()

        if self.initialized:
            return func(*args, **kwargs)
        else:
            return self.fallback_method()
        
    return decorator