class Task:
    def __init__(self):
        self.create_date = time.strftime('%Y_%m_%d %H:%M:%S', time.localtime())
        self.finish_date = time.strftime('%Y_%m_%d', time.localtime())
        
        
class Task_rank(Task):
    __cat_dict = {'rid=0&type=all': '全站', 'day=3&season_type=1': '番剧', 'day=3&season_type=4': '国产动画',
                  'rid=168&type=all': '国创相关', 'day=3&season_type=3': '纪录片', 'rid=1&type=all': '动画',
                  'rid=3&type=all': '音乐', 'rid=129&type=all': '舞蹈', 'rid=4&type=all': '游戏',
                  'rid=36&type=all': '知识','rid=188&type=all': '科技', 'rid=234&type=all': '运动',
                  'rid=223&type=all': '汽车', 'rid=160&type=all': '生活', 'rid=211&type=all': '美食',
                  'rid=217&type=all': '动物圈', 'rid=119&type=all': '鬼畜', 'rid=155&type=all': '时尚',
                  'rid=5&type=all': '娱乐', 'rid=181&type=all': '影视', 'day=3&season_type=2': '电影',
                  'day=3&season_type=5': '电视剧','rid=0&type=origin': '原创', 'rid=0&type=rookie': '新人'}

    def __init__(self, url: str):
        super().__init__()
        self.url = url
        self.cat = self.get_cat(url)

    def get_cat(self, url):
        pattern = '\?(.*)'
        keyword = re.findall(pattern, url)[0]
        return self.__cat_dict[keyword]
