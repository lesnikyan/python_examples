
# python_examples/multitask/custom_semafore.py

import logging
import multiprocessing
import time
import sys

LOG_LEVEL = logging.INFO
PROC_COUNT = 20
PROC_POOL_SIZE = 4
PROC_POOL_SIZE = PROC_POOL_SIZE if PROC_POOL_SIZE <= PROC_COUNT else PROC_COUNT
if PROC_POOL_SIZE > PROC_COUNT:
    PROC_POOL_SIZE = PROC_COUNT



def init_worker_logger():
    msg_format = '%(asctime)s [%(levelname)s] [%(module)s:%(name)s] %(message)s'
    logging.basicConfig(format=msg_format)
    rlog = logging.getLogger()
    rlog.setLevel(LOG_LEVEL)


def worker(num, arg):
    init_worker_logger()
    _log = logging.getLogger('subproc-%d' % num)
    _log.info('Subproc started')
    time.sleep(0.1)
    _log.info('Subproc finifshed')
    if num in [3, 7, 13]:
        sys.exit(22)


def get_logger():
    return logging.getLogger('main')


def main():
    init_worker_logger()
    _log = get_logger()

    # Creation proc queue loop
    process_queue = []
    for i in xrange(PROC_COUNT):
        proc_args = [i, (i)*100]
        spname = 'sp_%d' % i
        proc = multiprocessing.Process(target=worker, name=spname, args=proc_args)
        process_queue.append(proc)

    _log.info('Proc list created')

    # Starting loop
    started_list = []
    active_list = []
    finished_list = []

    def start_proc(index):
        process_queue[index].start()
        started_list.append(index)
        active_list.append(index)
        _log.info('Subproc (%d) %s has started' % (index, process_queue[index].name))

    def finish_proc(index):
        if index in active_list:
            active_list.remove(index)
        finished_list.append(index)
        _log.info('Subproc (%d) %s has finished' % (index, process_queue[index].name))
        _log.info('Finished %d processes' % (len(finished_list)))

    for i in xrange(PROC_POOL_SIZE):
        start_proc(i)
    _log.info('Started first part of subprocesses')

    # Control loop
    pqlen = len(process_queue)
    exit_info = list(xrange(pqlen))
    while True:
        if len(active_list) == 0:
            break
        for index in active_list:
            sproc = process_queue[index]

            # if process was finished
            if not sproc.is_alive():
                exit_code = sproc.exitcode
                if exit_code is None:
                    continue
                exit_info[index] = (index, exit_code,)
                finish_proc(index)
                # start next if queue has not started
                if len(started_list) < pqlen:
                    next_index = started_list[-1] + 1
                    start_proc(next_index)
    _log.info('All subprocesses were finished.')
    for info in exit_info:
        _log.info('suproc exit info: %s' % str(info))


if __name__ == '__main__':
    main()
