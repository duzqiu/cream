import json
import time
import requests

class DataService:
    @staticmethod
    def get_mock_data():
        """
        模拟 API 返回的数据结构
        结构：List[Dict] -> 每个 Dict 代表一个平台（如知乎、微博）
        """
        # 模拟网络延迟
        # time.sleep(0.5) 
        raw_data = requests.get("http://127.0.0.1:8000/api/hot_search/list").json()["data"]
        return raw_data
        
        # raw_data = [
        #     {
        #         "id": "1",
        #         "platform": "头条",
        #         "subtitle": "Toutiao",
        #         "icon": "https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/5c/1f/92/5c1f9236-d2a2-c247-c546-50fc5cb02e85/AppIcon-News-0-0-1x_U007emarketing-0-8-0-sRGB-85-220.png/400x400ia-75.webp",
        #         "items": [
        #             {"title": "Flet 2.0 发布，支持更多原生特性", "url": "#", "hot": "500w"},
        #             {"title": "Python 成为世界第一编程语言", "url": "#", "hot": "480w"},
        #             {"title": "如何看待 AI 取代程序员的言论？", "url": "#", "hot": "420w"},
        #             {"title": "如何看待 AI 取代程序员的言论？", "url": "#", "hot": "420w"},
        #             {"title": "如何看待 AI 取代程序员的言论？", "url": "#", "hot": "420w"},
        #             {"title": "如何看待 AI 取代程序员的言论？", "url": "#", "hot": "420w"},
        #             {"title": "如何看待 AI 取代程序员的言论？", "url": "#", "hot": "420w"},
        #             {"title": "如何看待 AI 取代程序员的言论？", "url": "#", "hot": "420w"},
        #             {"title": "如何看待 AI 取代程序员的言论？", "url": "#", "hot": "420w"},
        #             {"title": "如何看待 AI 取代程序员的言论？", "url": "#", "hot": "420w"},
        #             {"title": "如何看待 AI 取代程序员的言论？", "url": "#", "hot": "420w"},
        #             {"title": "如何看待 AI 取代程序员的言论？", "url": "#", "hot": "420w"},
        #             {"title": "如何看待 AI 取代程序员的言论？", "url": "#", "hot": "420w"},
        #             {"title": "周末去哪儿玩？", "url": "#", "hot": "300w"},
        #             {"title": "新发布的显卡性能测评", "url": "#", "hot": "280w"},
        #             {"title": "今日食谱推荐", "url": "#", "hot": "100w"},
        #         ]
        #     },
        #     {
        #         "id": "2",
        #         "platform": "微博",
        #         "subtitle": "Weibo",
        #         "icon": "https://ts3.tc.mm.bing.net/th/id/OIP-C.uVXZhv-4LI6iYq4o1AV3AwAAAA?w=108&h=108&c=1&bgcl=7de8ac&r=0&o=7&cb=ucfimg1&dpr=2&pid=ImgRC&rm=3&ucfimg=1",
        #         "items": [
        #             {"title": "有哪些相见恨晚的 Python 库？", "url": "#", "hot": "2万关注"},
        #             {"title": "全栈工程师的未来在哪里？", "url": "#", "hot": "1.5万关注"},
        #             {"title": "人类的极限在哪里？", "url": "#", "hot": "9000关注"},
        #             {"title": "为什么现在的年轻人不爱看电视了？", "url": "#", "hot": "8000关注"},
        #             {"title": "如何评价《黑神话：悟空》？", "url": "#", "hot": "7500关注"},
        #         ]
        #     },
        #     {
        #         "id": "3",
        #         "platform": "百度",
        #         "subtitle": "Baidu",
        #         "icon": "https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/eb/c8/11/ebc81175-b935-4ce3-7ea9-44f6c979449a/AppIcon-0-0-1x_U007epad-0-1-0-0-sRGB-85-220.png/350x350.png?",
        #         "items": [
        #             {"title": "flet-dev/flet", "url": "#", "hot": "Start: 8k"},
        #             {"title": "torvalds/linux", "url": "#", "hot": "Start: 150k"},
        #             {"title": "python/cpython", "url": "#", "hot": "Start: 60k"},
        #             {"title": "microsoft/vscode", "url": "#", "hot": "Start: 160k"},
        #             {"title": "facebook/react", "url": "#", "hot": "Start: 220k"},
        #         ]
        #     },
        #      {
        #         "id": "4",
        #         "platform": "新浪",
        #         "subtitle": "Sina",
        #         "icon": "https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/08/06/0f/08060fea-34cb-2e42-fbb0-88d445d665b9/AppIcon-0-0-1x_U007emarketing-0-8-0-85-220.png/350x350.png?",
        #         "items": [
        #             {"title": "本周值得关注的 iOS 应用", "url": "#", "hot": ""},
        #             {"title": "如何构建你的第二大脑", "url": "#", "hot": ""},
        #             {"title": "桌面改造计划 2.0", "url": "#", "hot": ""},
        #             {"title": "极简主义生活指南", "url": "#", "hot": ""},
        #             {"title": "摄影入门：构图的艺术", "url": "#", "hot": ""},
        #         ]
        #     },
        #      {
        #         "id": "5",
        #         "platform": "哔哩哔哩",
        #         "subtitle": "Bilibili",
        #         "icon": "https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/74/c2/f5/74c2f550-18c1-4594-9f2a-1a7478416178/AppIcon-0-0-1x_U007epad-0-1-0-85-220.png/350x350.png?",
        #         "items": [
        #             {"title": "本周值得关注的 iOS 应用", "url": "#", "hot": ""},
        #             {"title": "如何构建你的第二大脑", "url": "#", "hot": ""},
        #             {"title": "桌面改造计划 2.0", "url": "#", "hot": ""},
        #             {"title": "极简主义生活指南", "url": "#", "hot": ""},
        #             {"title": "摄影入门：构图的艺术", "url": "#", "hot": ""},
        #         ]
        #     },
        #      {
        #         "id": "6",
        #         "platform": "抖音",
        #         "subtitle": "TikTok",
        #         "icon": "https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/66/2c/e7/662ce7f5-ae55-0929-64e2-94e249ed8dbc/AppIcon_TikTok-0-0-1x_U007epad-0-1-0-0-85-220.png/350x350.png?",
        #         "items": [
        #             {"title": "本周值得关注的 iOS 应用", "url": "#", "hot": ""},
        #             {"title": "如何构建你的第二大脑", "url": "#", "hot": ""},
        #             {"title": "桌面改造计划 2.0", "url": "#", "hot": ""},
        #             {"title": "极简主义生活指南", "url": "#", "hot": ""},
        #             {"title": "摄影入门：构图的艺术", "url": "#", "hot": ""},
        #         ]
        #     } 
        # ]
        
        # # 为了演示效果，复制几份数据填满屏幕
        # return raw_data * 2