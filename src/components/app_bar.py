import flet as ft
from datetime import datetime

def get_app_bar(on_nav_change=None):
    # 获取时间
    week_days = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
    now = datetime.now()
    date_str = f"{now.strftime('%m月%d日')} {week_days[now.weekday()]}"

    # --- 辅助函数：创建紧凑型导航按钮 ---
    def nav_btn(text, index):
        return ft.TextButton(
            content=ft.Text(text, size=14, weight=ft.FontWeight.W_500),
            style=ft.ButtonStyle(
                color={
                    ft.ControlState.HOVERED: ft.Colors.BLUE,
                    ft.ControlState.DEFAULT: ft.Colors.BLACK54
                },
                overlay_color=ft.Colors.TRANSPARENT,
                # 【关键修改 1】设置较小的内边距
                # 左右各 8px，比默认的 16px 紧凑很多，适合手机屏幕
                padding=ft.padding.symmetric(horizontal=8), 
                # 设置圆角，点击时的高亮背景更好看
                shape=ft.RoundedRectangleBorder(radius=6),
            ),
            on_click=lambda e: on_nav_change(index) if on_nav_change else print(f"点击了Tab: {text}")
        )

    return ft.AppBar(
        leading=None,
        leading_width=0, 
        
        title=ft.Row(
            controls=[
                # 1. 标题块
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text("今日热榜", weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK87, size=15, height=20),
                            ft.Text(date_str, size=10, color=ft.Colors.GREY_500, weight=ft.FontWeight.NORMAL, height=14),
                        ],
                        spacing=0,
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.START
                    ),
                    padding=ft.padding.only(left=20), 
                ),

                # 2. 分割线
                ft.Container(
                    height=20, # 稍微改短一点
                    width=1, 
                    bgcolor=ft.Colors.GREY_300,
                    # 【关键修改 2】减小左右边距，从 15 减为 8，节省空间
                    margin=ft.margin.symmetric(horizontal=8) 
                ),

                # 3. Tab 导航区域
                # 使用 Container 包裹并开启 expand，确保它能占据剩余空间
                ft.Container(
                    content=ft.Row(
                        controls=[
                            nav_btn("综合", 0),
                            nav_btn("科技", 1),
                            nav_btn("娱乐", 2),
                            nav_btn("开发", 3),
                            nav_btn("设计", 4),
                        ],
                        # 【关键修改 3】
                        # spacing=0：完全靠按钮自身的 padding 控制间距，最紧凑
                        # scroll=HIDDEN：开启横向滚动！如果手机屏幕太小放不下，用户可以滑动查看，不会报错或挤压。
                        spacing=0,
                        scroll=ft.ScrollMode.HIDDEN, 
                    ),
                    expand=True, # 占据 Title 区域剩余的所有宽度
                    height=40,   # 限制高度，防止撑开 AppBar
                )
            ],
            spacing=0,
            vertical_alignment=ft.CrossAxisAlignment.CENTER
        ),
        
        title_spacing=0,
        center_title=False,
        bgcolor=ft.Colors.WHITE,
        elevation=0, 
        surface_tint_color=ft.Colors.TRANSPARENT,

        # --- 右侧区域 ---
        actions=[
            # ft.Container(
            #     content=ft.TextField(
            #         hint_text="搜索...",
            #         border_radius=20,
            #         height=35,
            #         content_padding=ft.padding.only(left=15, bottom=12),
            #         text_size=13,
            #         border_color="transparent",
            #         bgcolor=ft.Colors.GREY_100,
            #         prefix_icon=ft.Icons.SEARCH,
            #     ),
            #     width=160, # 保持较小的搜索框宽度
            #     padding=ft.padding.only(top=10, bottom=10) 
            # ),
            ft.Container(width=5),
            ft.IconButton(ft.Icons.NOTIFICATIONS_NONE, icon_color=ft.Colors.BLACK54),
            # ft.IconButton(ft.Icons.PERSON_OUTLINE, icon_color=ft.Colors.BLACK54),
            ft.Container(width=10) 
        ],
    )