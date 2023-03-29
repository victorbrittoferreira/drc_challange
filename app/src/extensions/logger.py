import logging


def log_exceptions(msg: str, extra: dict):
    """
    A decorator function that logs exceptions that occur in a wrapped function.

    Args:
        msg (str): A message string to include in the log message.
        extra (dict, optional): Additional information to include in the log message.
            Defaults to None.

    Returns:
        function: A decorator function that can be applied to another function.

    Example:
        import logging

        logging.basicConfig(level=logging.INFO)

        @log_exceptions(msg="An error occurred", extra={"reason": "unknown"})
        def my_function():
            raise ValueError("Something went wrong")

        my_function()
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            logger = logging.getLogger(func.__name__)
            # fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            try:
                return func(*args, **kwargs)
            except Exception as error:
                logger.exception(msg, extra=extra, exc_info=True)
                raise error

        return wrapper

    return decorator
