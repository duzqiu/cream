import flet as ft

def get_app_bar():
    return ft.AppBar(
        # --- 1. 左侧区域优化 ---
        # # 减小左侧容器的 padding，从 20 减为 10
        # leading=ft.Container(
        #     content=ft.Icon(ft.Icons.DASHBOARD, color=ft.Colors.BLACK87),
        #     padding=ft.padding.only(left=15), 
        #     on_click=lambda e: print("点击了菜单"),
        # ),
        # # 【关键修改】大幅减小 leading_width，给标题腾出空间
        # # 原来是 80，现在改为 50，足够容纳图标和边距
        # leading_width=50, 
        
        # --- 2. 标题区域优化 ---
        title=ft.Container(
            content=ft.Text(
                "今日热榜", 
                weight=ft.FontWeight.BOLD, 
                color=ft.Colors.BLACK87,
                # 【关键修改】减小字号，使其在手机上更精致
                size=16, 
                # 【关键修改】增加溢出处理，万一屏幕极小，显示省略号而不是换行错位
                overflow=ft.TextOverflow.ELLIPSIS,
                no_wrap=True
            ),
            # 减小左侧间距，使其紧凑
            padding=ft.padding.only(left=20), 
        ),
        
        # 减小标题与 leading 的默认间距
        title_spacing=0,
        center_title=False,
        
        # 样式设置
        bgcolor=ft.Colors.WHITE,
        elevation=0, 

        # --- 3. 右侧区域优化 ---
        actions=[
            ft.Container(
                content=ft.TextField(
                    hint_text="搜索...",
                    border_radius=20,
                    height=35,
                    content_padding=ft.padding.only(left=15, bottom=12),
                    text_size=13, # 搜索框文字也稍微改小
                    border_color="transparent",
                    bgcolor=ft.Colors.GREY_100,
                    prefix_icon=ft.Icons.SEARCH,
                ),
                # 【关键修改】大幅减小搜索框宽度
                # 原来 260，现在 160。在手机上 260 会直接把标题挤没。
                width=160, 
                padding=ft.padding.only(top=10, bottom=10) 
            ),
            
            ft.Container(width=5), # 减小间距
            
            # 使用 IconButton 默认大小，不额外增加 padding
            ft.IconButton(ft.Icons.NOTIFICATIONS_NONE, icon_color=ft.Colors.BLACK54, tooltip="通知"),
            
            # 用户头像
            # ft.IconButton(ft.Icons.PERSON_OUTLINE, icon_color=ft.Colors.BLACK54, tooltip="我的"),
            
            # 右侧对齐占位符（稍微减小以节省空间）
            ft.Container(width=10) 
        ],
    )