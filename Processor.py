class Processor:
    pass
    
    
class Processor_rank(Processor):
    def __init__(self, spider: Spider_rank, r: redis.Redis):
        self.spider = spider
        self.r = r

    def process(self):
        response = self.spider.response
        if response.get('data'):
            self.store(response.get('data')['list'])
        elif response.get('result'):
            self.store(response.get('result')['list'])

    def store(self, response_p: list):
        name = "_".join(["B站排行版", self.spider.task.cat, self.spider.task.finish_date])
        self.r.lpush(name, *[str(i) for i in response_p])
