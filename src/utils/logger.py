# utils/logger.py
import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger(log_file="app.log", max_bytes=5*1024*1024, backup_count=3):
    """
    配置全局日志
    :param log_file: 日志文件名
    :param max_bytes: 单个日志文件最大字节数 (默认5MB)
    :param backup_count: 保留的旧日志文件数量
    """
    
    # 1. 创建日志目录 (如果不存在)
    # 建议将日志放在单独的 logs 文件夹下，保持根目录整洁
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
        
    log_path = os.path.join(log_dir, log_file)

    # 2. 获取根日志记录器
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # 3. 如果已经有处理器，说明已经配置过，直接返回避免重复添加
    if logger.handlers:
        return logger

    # 4. 定义日志格式
    formatter = logging.Formatter(
        '%(asctime)s - [%(filename)s:%(lineno)d] - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # 5. 处理器 A: 文件输出 (支持自动回滚/切割)
    # RotatingFileHandler 可以防止日志文件无限增长
    file_handler = RotatingFileHandler(
        log_path, 
        maxBytes=max_bytes, 
        backupCount=backup_count, 
        encoding='utf-8'
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # 6. 处理器 B: 控制台输出 (方便开发调试)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger