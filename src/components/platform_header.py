import flet as ft

class PlatformHeader(ft.Container):
    def __init__(self, all_data):
        super().__init__()
        self.all_data = all_data
        
        # --- 样式设置 ---
        # 【修正】使用大写 Colors
        self.bgcolor = ft.Colors.WHITE 
        self.margin = ft.margin.only(top=15, left=20, right=20, bottom=10)
        self.border_radius = 10
        self.padding = ft.padding.symmetric(vertical=20, horizontal=15)
        self.shadow = ft.BoxShadow(
            spread_radius=1,
            blur_radius=3,
            color=ft.Colors.with_opacity(0.05, ft.Colors.BLACK),
            offset=ft.Offset(0, 2)
        )

        self.content = self._build_content()

    def _build_content(self):
        # 1. 数据去重 (修改：使用 platform 字段作为唯一键)
        unique_platforms = {}
        for item in self.all_data:
            # 获取平台名称，使用 .get 防止报错
            p_name = item.get("platform")
            
            # 如果该平台名称还没出现过，且名称不为空，则加入字典
            if p_name and p_name not in unique_platforms:
                unique_platforms[p_name] = item
        platforms_list = list(unique_platforms.values())

        # 2. 构建平台列表
        platform_controls = []
        for p in platforms_list:
            item = ft.Container(
                content=ft.Column(
                    controls=[
                        # 图标
                        ft.Image(
                            src=p.get("icon", ""), 
                            width=45, 
                            height=45, 
                            border_radius=12, 
                            fit=ft.ImageFit.COVER,
                            # 【修正】使用大写 Icons
                            error_content=ft.Icon(ft.Icons.BROKEN_IMAGE) 
                        ),
                        # 名称
                        ft.Text(
                            p.get("platform", "未命名"), 
                            size=12, 
                            color="#333333", 
                            weight=ft.FontWeight.W_500,
                            text_align=ft.TextAlign.CENTER
                        )
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=8
                ),
                padding=10,
                border_radius=8,
                ink=True,
                on_click=lambda e, name=p.get('platform'): print(f"切换到: {name}"),
                on_hover=self._handle_hover
            )
            platform_controls.append(item)

        # 3. 放置所有图标的行
        icons_row = ft.Row(
            controls=platform_controls,
            
            # 【关键修改 1】开启滚动模式 (HIDDEN=隐藏滚动条，AUTO=显示)
            scroll=ft.ScrollMode.HIDDEN, 
            
            spacing=15,
            
            # 【关键修改 2】当开启滚动且内容可能超出时，必须使用 START (左对齐)
            # 如果使用 CENTER，超出屏幕左侧的内容将无法通过滑动看到
            alignment=ft.MainAxisAlignment.START 
        )

        # 4. 底部说明文字
        description = ft.Container(
            content=ft.Text(
                "聚合全网热点，实时追踪当下互联网最热门的话题。",
                size=13,
                # 【修正】使用大写 Colors
                color=ft.Colors.GREY_500,
                text_align=ft.TextAlign.CENTER
            ),
            padding=ft.padding.only(top=10),
            alignment=ft.alignment.center
        )

        # 5. 组合
        return ft.Column(
            controls=[
                icons_row,
                # 【修正】使用大写 Colors
                ft.Divider(height=1, color=ft.Colors.GREY_100),
                description
            ],
            spacing=10,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER 
        )

    def _handle_hover(self, e):
        # 【修正】使用大写 Colors
        e.control.bgcolor = ft.Colors.GREY_50 if e.data == "true" else ft.Colors.TRANSPARENT
        e.control.update()