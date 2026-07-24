import logging
import sys


class Logger:
    """Application logger."""

    @staticmethod
    def get_logger(name: str) -> logging.Logger:
        logger = logging.getLogger(name)

        if logger.hasHandlers():
            return logger

        logger.setLevel(logging.INFO)

        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        handler.setFormatter(formatter)
        logger.addHandler(handler)

        return logger