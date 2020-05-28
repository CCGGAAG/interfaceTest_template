# coding=utf-8
from tools.sample_tools import get_project_config
from tools.log import Logger


class BaseClass(object):
    """
    初始化配置信息
    """
    logger = None
    user_info = None
    db_info = None
    mail_info = None
    host_info = None

    def __new__(cls, *args, **kwargs):
        """
        单例模式确保配置信息唯一
        """
        if not hasattr(cls, '_instance'):
            orig = super(BaseClass, cls)
            cls._instance = orig.__new__(cls, *args, **kwargs)
            cls._instance.__initconf()
        return cls._instance

    def __initconf(self):
        self.db_info = get_project_config('database.yaml')
        self.user_info = get_project_config('user.yaml')
        self.mail_info = get_project_config('email.yaml')
        self.logger = Logger()
        self.host_info = get_project_config('hosts.yaml')