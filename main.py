from multiprocessing import Queue, Process
import time
import random
from Task import Task_rank
from Spider import Spider_rank
from Processor import Processor_rank
import redis


def consumer3(r, q2):
    while 1:
        q2.get()
        print(time.time())
        time.sleep(1)


def consumer2(q2: Queue):
    pool = redis.ConnectionPool(host='localhost', port=6379, db=1, decode_responses=True)
    r = redis.Redis(connection_pool=pool)
    while True:
        spider: Spider_rank = q2.get()
        if spider is None:
            break
        processor = Processor_rank(spider=spider, r=r)
        processor.process()
        print(processor.__str__())


def consumer(q1: Queue, q2: Queue):
    while True:
        task: Task_rank = q1.get()
        if task is None:
            break
        spider = Spider_rank(task=task, retry=5)
        spider.execute_task()
        q2.put(spider)
        print(spider.__str__())
        time.sleep(3)


def producer(url_li: list, q: Queue):
    for url in url_li:
        task = Task_rank(url=url)
        q.put(task)
        print(task.__str__())


if __name__ == '__main__':
    pool = redis.ConnectionPool(host='localhost', port=6379, db=1, decode_responses=True)
    r = redis.Redis(connection_pool=pool)
    li1 = r.get("B站排行榜_视频_url").splitlines()
    li2 = r.get("B站排行榜_连载动画_url").splitlines()
    li3 = r.get("B站排行榜_其他_url").splitlines()
    url_li = [*li1, *li2, *li3]

    queue1 = Queue()
    queue2 = Queue()

    p1 = Process(target=producer, args=(url_li, queue1))
    c1 = Process(target=consumer, args=(queue1, queue2))
    c2 = Process(target=consumer2, args=(queue2, ))

    p1.start()
    c1.start()
    c2.start()

    p1.join()
    queue1.put(None)
    c1.join()
    queue2.put(None)

