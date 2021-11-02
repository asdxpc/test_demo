import logging, os, time



class Get_log:

    def __init__(self):
        # 创建一个记录
        self.log = logging.getLogger()
        # 设置记录器记录BUG等级
        self.log.setLevel(level=logging.INFO)
        # 定义一个格式输出的格式
        self.formater = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
        # log保存的路径及格式，每次运行一次即根据时间创建一个log文件
        self.log_path = os.path.join('../log', '%s.log' % time.strftime('%Y-%m-%d %H_%M_%S'))
        # 写死log文件名，直接在原来的基础上添加新的log数据
       # self.log_path = os.path.join(log_path, 'log_result.log')

    def __get_log(self, level, message):
        # 创建一个hander,处理器，有FileHander和StremaHandler,分别输出log到文件或者控制台
        fh = logging.FileHandler(self.log_path, encoding='utf-8')
        # 设置handler的输出等级
        fh.setLevel(logging.INFO)
        # 设置handler的输出格式
        fh.setFormatter(self.formater)
        # 把handler添加到记录器
        self.log.addHandler(fh)

        sh = logging.StreamHandler()
        sh.setLevel(logging.INFO)
        sh.setFormatter(self.formater)
        # 把这个处理器也添加到记录器中，一个记录器可以存在多个处理器，这样log文件记录的同时屏幕也会输出log信息
        self.log.addHandler(sh)
        # 判断并输出对应的log信息
        if level == 'debug':
            # self.log.debug(message)
            self.log.debug(message)
        if level == 'info':
            self.log.info(message)
        if level == 'warning':
            self.log.warning(message)
        if level == 'error':
            self.log.error(message)
        if level == 'critail':
            self.log.critical()
        # 调用后需要移除处理器，否则会导致执行多个用例后输出重复的问题
        self.log.removeHandler(sh)
        self.log.removeHandler(fh)
        fh.close()

    # 创建对应的log输出函数
    def log_debug(self,message):
        self.__get_log('debug',message)

    def log_info(self,message):
        self.__get_log('info',message)

    def log_warning(self,message):
        self.__get_log('warning',message)

    def log_error(self,message):
        self.__get_log('error',message)

    def log_critical(self,message):
        self.__get_log('warning',message)

if __name__ == "__main__":
    Get_log().log_error("测试info")
