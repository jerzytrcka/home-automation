def verify_initialized(func):
    ''' Decorator to check if the connection has been initialized. If not, it calls the fallback method. '''

    def decorator(self, *args, **kwargs):
        if self.get_initialized():
            return func(self, *args, **kwargs)
        else:
            return self.fallback_method()
        
    return decorator