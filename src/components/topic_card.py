import flet as ft
import random

class TopicCard(ft.Container):
    def __init__(self, platform_data):
        super().__init__()
        self.data = platform_data
        
        # 1. 设置卡片样式
        self.height = 400
        self.bgcolor = ft.Colors.WHITE
        self.border_radius = 8
        self.padding = 15
        self.shadow = ft.BoxShadow(
            spread_radius=1,
            blur_radius=5,
            color=ft.Colors.with_opacity(0.1, ft.Colors.BLACK),
        )

        self.content = self._build_content()

    def _build_content(self):
        # --- A. 头部区域 (保持不变) ---
        header = ft.Row(
            controls=[
                ft.Image(
                    src=self.data.get("icon", ""), 
                    width=24, height=24, border_radius=4, fit=ft.ImageFit.COVER,
                    error_content=ft.Icon(ft.Icons.IMAGE_NOT_SUPPORTED)
                ),
                # 主标题
                ft.Text(self.data.get("title", "未命名"), weight=ft.FontWeight.BOLD, size=16, color="#333333"),
                ft.Container(expand=True),
                # 副标题
                ft.Text(self.data.get("subtitle", "未命名"), size=12, color=ft.Colors.BLUE_GREY_400),
            ],
            vertical_alignment=ft.CrossAxisAlignment.CENTER
        )

        # --- B. 中间列表区域 (核心修改点) ---
        list_items = []
        items_to_show = self.data["items"]

        for idx, item in enumerate(items_to_show):
            rank_num = idx + 1
            
            # 【关键】根据排名决定背景色
            if rank_num == 1:
                bg_color = ft.Colors.RED
                text_color = ft.Colors.WHITE # 前三名数字是白色
            elif rank_num == 2:
                bg_color = ft.Colors.ORANGE
                text_color = ft.Colors.WHITE
            elif rank_num == 3:
                bg_color = ft.Colors.AMBER
                text_color = ft.Colors.WHITE
            else:
                # 4名以后：灰色背景，深灰色数字
                bg_color = ft.Colors.GREY_400 
                text_color = ft.Colors.WHITE

            # 【关键】创建数字序号的容器
            rank_badge = ft.Container(
                content=ft.Text(
                    f"{rank_num}", 
                    color=text_color, 
                    weight=ft.FontWeight.BOLD, 
                    size=12
                ),
                bgcolor=bg_color,          # 设置背景色
                border_radius=4,           # 设置圆角
                width=20,                  # 固定宽度和高度使其成为正方形
                height=20,
                alignment=ft.alignment.center, # 数字居中
                margin=ft.margin.only(right=5) # 右侧留点间距
            )

            # 单行条目
            item_row = ft.Container(
                content=ft.Row(
                    controls=[
                        # 这里放入新的序号徽章
                        rank_badge, 
                        
                        ft.Text(
                            item.get("title", ""), 
                            size=14, 
                            color="#333333", 
                            overflow=ft.TextOverflow.ELLIPSIS,
                            no_wrap=True,
                            expand=True
                        ),
                        ft.Text(item.get("hot", ""), size=12, color=ft.Colors.GREY_400),
                    ],
                    # spacing 改小一点，因为 rank_badge 已经自带了 margin
                    spacing=2, 
                    vertical_alignment=ft.CrossAxisAlignment.CENTER
                ),
                padding=ft.padding.symmetric(vertical=8, horizontal=2),
                on_click=lambda e, title=item.get("title"): print(f"点击了: {title}"),
                ink=True,
                border_radius=4
            )
            list_items.append(item_row)

        scrollable_content = ft.ListView(
            controls=list_items,
            expand=True,
            spacing=0,
            padding=ft.padding.only(top=5, bottom=5)
        )

        # --- C. 底部区域 (保持不变) ---
        mock_time = f"{random.randint(1, 59)}分钟前更新"
        footer = ft.Column(
            controls=[
                ft.Divider(height=1, color=ft.Colors.GREY_100),
                ft.Row(
                    controls=[
                        ft.Icon(ft.Icons.ACCESS_TIME, size=12, color=ft.Colors.GREY_400),
                        ft.Text(mock_time, size=11, color=ft.Colors.GREY_400),
                        ft.Container(expand=True),
                        ft.Icon(ft.Icons.REFRESH, size=14, color=ft.Colors.GREY_400),
                    ],
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                )
            ],
            spacing=5
        )

        # --- D. 整体布局 ---
        return ft.Column(
            controls=[header, ft.Divider(height=1, color=ft.Colors.GREY_100), scrollable_content, footer],
            spacing=2,
            expand=True
        )