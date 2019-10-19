import json
import time
import logging

from fluent import handler


# - Set logging
def set_logging(logger, log_name, host="127.0.0.1", port=24224, level='INFO'):

    custom_format = {
        'host': '%(hostname)s',
        'where': '%(module)s.%(funcName)s',
        'type': '%(levelname)s',
        'stack_trace': '%(exc_text)s',
        'created': '%(created)s',
        #'stack_info': '%(stack_info)s',
    }

    if level == 'INFO':
        level = logging.INFO

    if level == 'DEBUG':
        level = logging.DEBUG

    logging.basicConfig(level=level,
                        format='%(asctime)s %(name)-8s %(levelname)-8s %(message)s',
                        datefmt='%m-%d %H:%M',
                        filemode='a'
                        )

    # Console settings
    console = logging.StreamHandler()
    console.setLevel(level)

    formatter = logging.Formatter('%(name)-8s: %(levelname)-8s %(message)s')

    # tell the handler to use this format
    console.setFormatter(formatter)

    h = handler.FluentHandler(log_name, host=host, port=port)

    formatter = handler.FluentRecordFormatter(custom_format)
    h.setFormatter(formatter)

    log = logging.getLogger(logger)
    log.addHandler(h)

    return log


# Main
if __name__ == '__main__':

    log = set_logging(
        'fluentd',
        'application.python.test',
        'localhost',
        24224,
        'INFO'
    )

    log.debug('Message debug')
    log.info('Message info')
    log.error('Message error')
    log.critical('Message critical')

    try:
        a = 2 / 0
    except Exception as e:
        log.exception('Error during divide')
