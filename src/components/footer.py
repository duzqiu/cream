import flet as ft

class Footer(ft.Container):
    def __init__(self):
        super().__init__()
        
        # 设置页脚容器的样式
        self.padding = ft.padding.symmetric(vertical=30, horizontal=20)
        self.bgcolor = ft.Colors.TRANSPARENT # 背景透明，融入页面背景
        self.alignment = ft.alignment.center
        
        self.content = self._build_content()

    def _build_content(self):
        # 辅助链接样式
        def link_text(text):
            return ft.Text(
                text, 
                size=12, 
                color=ft.Colors.GREY_500,
                weight=ft.FontWeight.W_500,
                # 鼠标移上去变色效果（可选高级功能，这里简化处理）
            )

        return ft.Column(
            controls=[
                # 第一行：友情链接
                ft.Row(
                    controls=[
                        link_text("关于我们"),
                        self._dot(),
                        link_text("免责声明"),
                        self._dot(),
                        link_text("帮助中心"),
                        self._dot(),
                        link_text("联系合作"),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=5
                ),
                
                # 第二行：版权信息
                ft.Text(
                    "© 2024 TopHub Clone. Powered by Flet & Python.", 
                    size=12, 
                    color=ft.Colors.GREY_400
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10
        )

    def _dot(self):
        """链接之间的分隔点"""
        return ft.Container(
            width=3, 
            height=3, 
            border_radius=3, 
            bgcolor=ft.Colors.GREY_400,
            margin=ft.margin.symmetric(horizontal=5)
        )