import flet as ft
from datetime import datetime

def get_app_bar():
    # 获取时间
    week_days = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
    now = datetime.now()
    # 注意：这里去掉了前面的空格，因为换行了不需要空格隔开
    date_str = f"{now.strftime('%m月%d日')} {week_days[now.weekday()]}"

    return ft.AppBar(
        # --- 1. 移除左侧菜单 ---
        leading=None,
        leading_width=0, # 设置为0，消除左侧留白
        
        # --- 2. 标题区域 (改为上下垂直结构) ---
        title=ft.Container(
            content=ft.Column(
                controls=[
                    # 上方：大标题
                    ft.Text(
                        "今日热榜", 
                        weight=ft.FontWeight.BOLD, 
                        color=ft.Colors.BLACK87, # 确保使用大写 Colors
                        size=15, # 稍微改小一点，适应双行布局
                        height=20, # 控制行高，避免间距过大
                    ),
                    # 下方：小时间
                    ft.Text(
                        date_str, 
                        size=10, # 设为小字号
                        color=ft.Colors.GREY_500,
                        weight=ft.FontWeight.NORMAL,
                        height=14, # 控制行高
                    ),
                ],
                spacing=0, # 上下两行紧贴
                alignment=ft.MainAxisAlignment.CENTER, # 垂直居中
                horizontal_alignment=ft.CrossAxisAlignment.START # 文字左对齐
            ),
            # 给整个标题块加一点左边距，不要紧贴屏幕边缘
            padding=ft.padding.only(left=20), 
        ),
        
        title_spacing=0,
        center_title=False,
        
        # 样式设置
        bgcolor=ft.Colors.WHITE,
        elevation=0, 

        # --- 3. 右侧区域 (保持不变) ---
        actions=[
            ft.Container(
                content=ft.TextField(
                    hint_text="搜索...",
                    border_radius=20,
                    height=35,
                    content_padding=ft.padding.only(left=15, bottom=12),
                    text_size=13,
                    border_color="transparent",
                    bgcolor=ft.Colors.GREY_100,
                    prefix_icon=ft.Icons.SEARCH,
                ),
                width=160, 
                padding=ft.padding.only(top=10, bottom=10) 
            ),
            
            ft.Container(width=5),
            
            ft.IconButton(ft.Icons.NOTIFICATIONS_NONE, icon_color=ft.Colors.BLACK54),
            # ft.IconButton(ft.Icons.PERSON_OUTLINE, icon_color=ft.Colors.BLACK54),
            
            ft.Container(width=10) 
        ],
    )