import json
import time

class DataService:
    @staticmethod
    def get_mock_data():
        """
        模拟 API 返回的数据结构
        结构：List[Dict] -> 每个 Dict 代表一个平台（如知乎、微博）
        """
        # 模拟网络延迟
        # time.sleep(0.5) 
        
        raw_data = [
            {
                "id": "1",
                "title": "微博",
                "icon": "https://file.ipadown.com/tophub/assets/images/media/s.weibo.com.png_50x50.png",
                "items": [
                    {"title": "Flet 2.0 发布，支持更多原生特性", "url": "#", "hot": "500w"},
                    {"title": "Python 成为世界第一编程语言", "url": "#", "hot": "480w"},
                    {"title": "如何看待 AI 取代程序员的言论？", "url": "#", "hot": "420w"},
                    {"title": "如何看待 AI 取代程序员的言论？", "url": "#", "hot": "420w"},
                    {"title": "如何看待 AI 取代程序员的言论？", "url": "#", "hot": "420w"},
                    {"title": "如何看待 AI 取代程序员的言论？", "url": "#", "hot": "420w"},
                    {"title": "如何看待 AI 取代程序员的言论？", "url": "#", "hot": "420w"},
                    {"title": "如何看待 AI 取代程序员的言论？", "url": "#", "hot": "420w"},
                    {"title": "如何看待 AI 取代程序员的言论？", "url": "#", "hot": "420w"},
                    {"title": "如何看待 AI 取代程序员的言论？", "url": "#", "hot": "420w"},
                    {"title": "如何看待 AI 取代程序员的言论？", "url": "#", "hot": "420w"},
                    {"title": "如何看待 AI 取代程序员的言论？", "url": "#", "hot": "420w"},
                    {"title": "如何看待 AI 取代程序员的言论？", "url": "#", "hot": "420w"},
                    {"title": "周末去哪儿玩？", "url": "#", "hot": "300w"},
                    {"title": "新发布的显卡性能测评", "url": "#", "hot": "280w"},
                    {"title": "今日食谱推荐", "url": "#", "hot": "100w"},
                ]
            },
            {
                "id": "2",
                "title": "知乎",
                "icon": "https://file.ipadown.com/tophub/assets/images/media/zhihu.com.png_50x50.png",
                "items": [
                    {"title": "有哪些相见恨晚的 Python 库？", "url": "#", "hot": "2万关注"},
                    {"title": "全栈工程师的未来在哪里？", "url": "#", "hot": "1.5万关注"},
                    {"title": "人类的极限在哪里？", "url": "#", "hot": "9000关注"},
                    {"title": "为什么现在的年轻人不爱看电视了？", "url": "#", "hot": "8000关注"},
                    {"title": "如何评价《黑神话：悟空》？", "url": "#", "hot": "7500关注"},
                ]
            },
            {
                "id": "3",
                "title": "GitHub Trending",
                "icon": "https://file.ipadown.com/tophub/assets/images/media/github.com.png_50x50.png",
                "items": [
                    {"title": "flet-dev/flet", "url": "#", "hot": "Start: 8k"},
                    {"title": "torvalds/linux", "url": "#", "hot": "Start: 150k"},
                    {"title": "python/cpython", "url": "#", "hot": "Start: 60k"},
                    {"title": "microsoft/vscode", "url": "#", "hot": "Start: 160k"},
                    {"title": "facebook/react", "url": "#", "hot": "Start: 220k"},
                ]
            },
             {
                "id": "4",
                "title": "少数派",
                "icon": "https://file.ipadown.com/tophub/assets/images/media/sspai.com.png_50x50.png",
                "items": [
                    {"title": "本周值得关注的 iOS 应用", "url": "#", "hot": ""},
                    {"title": "如何构建你的第二大脑", "url": "#", "hot": ""},
                    {"title": "桌面改造计划 2.0", "url": "#", "hot": ""},
                    {"title": "极简主义生活指南", "url": "#", "hot": ""},
                    {"title": "摄影入门：构图的艺术", "url": "#", "hot": ""},
                ]
            },
             {
                "id": "5",
                "title": "少数派121",
                "icon": "https://file.ipadown.com/tophub/assets/images/media/sspai.com.png_50x50.png",
                "items": [
                    {"title": "本周值得关注的 iOS 应用", "url": "#", "hot": ""},
                    {"title": "如何构建你的第二大脑", "url": "#", "hot": ""},
                    {"title": "桌面改造计划 2.0", "url": "#", "hot": ""},
                    {"title": "极简主义生活指南", "url": "#", "hot": ""},
                    {"title": "摄影入门：构图的艺术", "url": "#", "hot": ""},
                ]
            } 
        ]
        
        # 为了演示效果，复制几份数据填满屏幕
        return raw_data * 3