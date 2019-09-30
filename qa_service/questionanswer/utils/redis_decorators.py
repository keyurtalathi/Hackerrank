from flask import current_app as app


def get_custom_memoizer(function_name):
    def get_memoized_results(candidate_function):
        def wrapper(*args, **kwargs):
            cache_handler = app.global_cache_handler
            key = function_name + str(kwargs)
            # print "\n\n\nkey -----------",key
            value = cache_handler.get(key)
            # print "\n\n\nvalue ------------",value
            if not value:
                # print 'not found in cache**********'
                value = candidate_function(*args, **kwargs)
                app.logger.info("Value from API request for : %s" % str(value))
                cache_handler.set(key, value)
            else:
                app.logger.info("Value from cache for : %s" % str(value))
            return value

        return wrapper

    return get_memoized_results
