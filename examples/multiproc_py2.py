
import logging
import logging.handlers
import sys
import traceback
import time
import multiprocessing
from multiprocessing import Process, Queue


class CustomQueueHandler(logging.Handler):

    def __init__(self, queue):
        logging.Handler.__init__(self)
        self._qu = queue
        
    def emit(self, record):
        self._qu.put(record)


# def logRecord(name, lvl, msg, exc=None):
#     log = logging.getLogger()
#     (file_name, line_num, func) = log.findCaller()
#     print 'Log caller: ', (file_name, line_num, func)
#     """ makeRecord(self, name, level, fn, lno, msg, args, exc_info, func=None, extra=None) """

#     return log.makeRecord(name, lvl, file_name, line_num, msg, None, exc, func)

import os
def log_conf():
    logger = logging.getLogger()
    # print(dir(logging), '\n\n')
    # print(dir(logging.handlers), '\n\n')
    log_file = 'log_demos/log/multiproc_queue2.log'
    if os.path.isfile(log_file):
        os.remove(log_file)
    handler = logging.FileHandler(log_file)
    formatter = logging.Formatter('%(asctime)s %(processName)-10s %(name)s %(levelname)-8s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    # (file_name, line_number, func_name) = logger.findCaller()
    # logger.makeRecord()


def worker_conf(queue):
    # handler = logging.handlers.QueueHandler(queue)
    handler = CustomQueueHandler(queue)
    logger = logging.getLogger()
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)


def log_process(queue, configurer):
    ''' '''
    configurer()
    # queue = Queue()
    # _log = logging.getLogger('simple-logger')
    while True:
        try:
            record = queue.get()
            if record is None:
                break
            logger = logging.getLogger(record.name)
            logger.handle(record)
        except Exception as ex:
            ex_info = sys.exc_info()
            print(traceback.format_exception(*ex_info))


def worker_process(queue, configurer, data=[], pid=0):
    # create logger by queue
    configurer(queue)
    name = multiprocessing.current_process().name
    logger = logging.getLogger('worker_%s' % name)
    print('Worker %s started' % name)
    # logger = logging.getLogger()
    for i in range(10):
        msg = 'Worker %s puts %s iter' % (name, i)
        logger.log(logging.INFO, msg)
        time.sleep(0.01)
    print('Worker %s finished' % name)


def main():
    ''' '''

    log_queue = Queue()

    # create logger process
    log_proc = Process(target=log_process, name='Log_subproc', 
                       args=(log_queue, log_conf))
    log_proc.start()

    # create workers
    workers = []
    for i in range(5):
        data = []
        pid = 100 + i
        proc_args = (log_queue, worker_conf)
        proc_kwargs = {
            'data': data,
            'pid': pid
        }
        proc = Process(target=worker_process, name='worker%s' % pid, args=proc_args,
                       kwargs=proc_kwargs)
        proc.start()
        workers.append(proc)
    # waiting
    for worker in workers:
        worker.join()
    log_queue.put_nowait(None)
    log_proc.join()
    print('End of main')


# python_examples/log_demos/multi_proc.py
if __name__ == '__main__':
    main()