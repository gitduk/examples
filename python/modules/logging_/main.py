import logging
import logging.config
import yaml


def base_use():
    logging.debug("debug")
    logging.info("info")
    logging.warning("warning")
    logging.error("error")
    logging.critical("critical")


def add_some_config():
    """
    格式化消息字段列表: https://docs.python.org/zh-cn/3/library/logging.html#logrecord-attributes
    write log to file
    :return:
    """
    logging.basicConfig(
        datefmt="%Y-%m-%d %H:%M:%S",
        format="%(asctime)s %(msecs)d %(filename)s %(funcName)s %(lineno)d %(levelname)s: %(message)s",
        filename="logging.log",
        filemode="w",
        level=logging.INFO,
    )

    base_use()


def get_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler_formatter = logging.Formatter(
        datefmt="%Y-%m-%d %H:%M:%S",
        fmt="%(asctime)s %(msecs)d %(filename)s %(funcName)s %(lineno)d %(levelname)s: %(message)s")
    console_handler.setFormatter(console_handler_formatter)

    file_handler = logging.FileHandler(filename="main.log")
    file_handler.setLevel(logging.INFO)
    file_handler_formatter = logging.Formatter(
        datefmt="%Y-%m-%d %H:%M:%S",
        fmt="%(asctime)s %(msecs)d %(filename)s %(funcName)s %(lineno)d %(levelname)s: %(message)s")
    file_handler.setFormatter(file_handler_formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger


if __name__ == '__main__':
    # 基础使用方法
    # base_use()  # 默认级别为warning

    # 基础配置
    # add_some_config()

    # 手动添加 handler
    # logger = get_logger()
    # logger.info("run init logger")

    # 使用yaml配置文件
    with open("logging.yaml", "r") as config:
        logging.config.dictConfig(yaml.load(config, Loader=yaml.SafeLoader))

    logger = logging.getLogger("my_module")
    logger.info("hi")
    logger.warning("hi")
    logger.error("kill")
