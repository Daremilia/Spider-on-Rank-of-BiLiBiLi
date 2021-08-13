class Spider:
    def __init__(self, retry: int = 10, gap: int = 3):
        self.retry = retry
        self.gap = gap

    @staticmethod
    def __sleep(second):
        time.sleep(round(random.uniform(second - 0.2, second + 0.2), 2))

    def get(self, url):
        counter = 1
        while counter <= self.retry:
            self.__sleep(self.gap)
            try:
                res = requests.get(url=url)
                res_json = res.json()
                return res_json
            except:
                pass
        return {}

    def execute_task(self):
        pass


class Spider_rank(Spider):
    def __init__(self, task: Task_rank, retry: int = 10, gap: int = 3):
        super().__init__(retry, gap)
        self.task = task
        self.response = None

    def execute_task(self):
        url = self.task.url
        response = super().get(url)
        self.set_response(response)

    def set_response(self, response: dict):
        self.response = response
