import flet as ft

# 修改点：继承自 ft.Container
class Sidebar(ft.Container):
    def __init__(self):
        super().__init__()
        
        # 设置 Container 自身样式
        self.width = 200
        self.bgcolor = ft.Colors.WHITE
        self.padding = 10
        
        # 设置内容
        self.content = ft.Column(
            controls=[
                self.nav_item("全部", ft.Icons.HOME, True),
                self.nav_item("科技", ft.Icons.COMPUTER),
                self.nav_item("娱乐", ft.Icons.MOVIE),
                self.nav_item("创意", ft.Icons.LIGHTBULB),
                self.nav_item("游戏", ft.Icons.GAMES),
                self.nav_item("购物", ft.Icons.SHOPPING_BAG),
                ft.Divider(),
                ft.Text("我的订阅", size=12, color=ft.Colors.GREY),
                self.nav_item("微博", ft.Icons.BOOKMARK_BORDER),
                self.nav_item("知乎", ft.Icons.BOOKMARK_BORDER),
            ],
            spacing=5
        )

    def nav_item(self, text, icon, is_active=False):
        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.Icon(icon, size=18, color=ft.Colors.RED if is_active else ft.Colors.GREY_600),
                    ft.Text(text, size=14, color=ft.Colors.RED if is_active else ft.Colors.GREY_800, weight=ft.FontWeight.W_500)
                ],
            ),
            bgcolor=ft.Colors.RED_50 if is_active else ft.Colors.TRANSPARENT,
            padding=10,
            border_radius=8,
            on_hover=lambda e: self._handle_hover(e),
            ink=True,
            on_click=lambda e: print(f"Navigate to {text}")
        )

    def _handle_hover(self, e):
        # 鼠标悬停效果
        e.control.bgcolor = ft.Colors.GREY_100 if e.data == "true" else ft.Colors.TRANSPARENT
        e.control.update()