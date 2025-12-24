import flet as ft
import time
from collections import defaultdict
import logging
from utils.logger import setup_logger

# 导入您现有的组件
from data_service import DataService
from components.app_bar import get_app_bar
from components.platform_header import PlatformHeader
from components.topic_card import TopicCard
from components.footer import Footer

setup_logger()

# --- 1. 定义限流器类 ---
class RateLimiter:
    def __init__(self, max_requests: int, window_seconds: int):
        """
        :param max_requests: 时间窗口内允许的最大请求次数
        :param window_seconds: 时间窗口大小（秒）
        """
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        # 存储格式: { '192.168.1.1': [timestamp1, timestamp2, ...] }
        self.access_history = defaultdict(list)

    def is_allowed(self, ip_address: str) -> bool:
        # 如果获取不到IP（本地运行通常是None），视情况处理，这里默认允许或者设为本地回环
        if not ip_address:
            ip_address = "127.0.0.1" 
            
        current_time = time.time()
        timestamps = self.access_history[ip_address]
        
        # 清理过期记录（保留窗口期内的时间戳）
        valid_timestamps = [t for t in timestamps if current_time - t < self.window_seconds]
        self.access_history[ip_address] = valid_timestamps
        
        # 判断是否超限
        if len(valid_timestamps) >= self.max_requests:
            return False  # 禁止访问
        
        # 记录本次访问
        self.access_history[ip_address].append(current_time)
        return True

# --- 配置限流规则 ---
# 例如：60秒内最多允许 10 次访问 (刷新页面算一次访问)
# 您可以根据实际需求调整这个数字
global_limiter = RateLimiter(max_requests=10, window_seconds=60)


def main(page: ft.Page):
    # 1. 页面基础设置
    page.title = "今日热榜 - Clone"
    page.bgcolor = "#f5f7f9"
    page.padding = 0
    page.theme_mode = ft.ThemeMode.LIGHT

    # --- 2. IP 限流检查 (拦截逻辑) ---
    # 获取客户端 IP
    client_ip = page.client_ip or "127.0.0.1"

    logging.info(f"用户接入 IP: {client_ip}")

    if not global_limiter.is_allowed(client_ip):
        # === 如果被限流，显示禁止访问页面 ===
        page.bgcolor = ft.Colors.RED_50 # 背景变红
        page.add(
            ft.Center(
                content=ft.Column(
                    controls=[
                        ft.Icon(ft.Icons.GPP_BAD, size=80, color=ft.Colors.RED),
                        ft.Text("访问过于频繁", size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.RED),
                        ft.Container(height=10),
                        ft.Text(f"您的 IP ({client_ip}) 已触发安全限制。", color=ft.Colors.GREY_700),
                        ft.Text("请稍后再次尝试访问。", color=ft.Colors.GREY_700),
                        ft.Container(height=20),
                        ft.OutlinedButton("尝试刷新", on_click=lambda e: page.window_reload())
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=5
                )
            )
        )
        return # 【关键】直接结束函数，不加载后续正常的 App 内容

    # =========================================================
    # === 如果 IP 正常，执行原本的 App 逻辑 ===
    # =========================================================

    # 3. 获取数据
    all_data = DataService.get_mock_data()

    # 4. 定义主内容容器
    body_container = ft.ListView(
        expand=True, 
        spacing=0,
        padding=0
    )

    # --- 页面构建函数：构建首页 ---
    def build_home_view():
        header_section = PlatformHeader(all_data)
        
        grid_items = []
        for item in all_data:
            grid_items.append(
                ft.Column(
                    controls=[TopicCard(item)],
                    col={"sm": 12, "md": 6, "lg": 4, "xl": 3} 
                )
            )

        content_grid = ft.ResponsiveRow(
            controls=grid_items,
            run_spacing=20,
            spacing=20
        )

        return [
            header_section,
            ft.Container(
                content=content_grid,
                padding=ft.padding.symmetric(horizontal=20, vertical=10)
            ),
            Footer()
        ]

    # --- 页面构建函数：构建分类页 ---
    def build_category_view(category_name):
        # 简单筛选逻辑
        filtered_data = [item for item in all_data if category_name in item['platform'] or len(item['items']) > 0]
        
        grid_items = []
        for item in filtered_data:
            grid_items.append(
                ft.Column(
                    controls=[TopicCard(item)],
                    col={"sm": 12, "md": 6, "lg": 4, "xl": 3} 
                )
            )
            
        content_grid = ft.ResponsiveRow(
            controls=grid_items,
            run_spacing=20,
            spacing=20
        )

        return [
            # 分类页标题
            ft.Container(
                content=ft.Text(f"{category_name} 热榜", size=24, weight=ft.FontWeight.BOLD),
                padding=ft.padding.only(left=20, top=20, bottom=10),
                bgcolor=ft.Colors.WHITE, # 保持背景一致
                width=float("inf") 
            ),
            ft.Container(
                content=content_grid,
                padding=ft.padding.symmetric(horizontal=20, vertical=10)
            ),
            Footer()
        ]

    # 5. 定义路由切换处理函数
    def handle_nav_change(index):
        logging.info(f"切换页面至 Tab 索引: {index}")
        
        # 清空当前内容
        body_container.controls.clear()
        
        # 根据索引加载不同内容
        if index == 0:
            body_container.controls = build_home_view()
        elif index == 1:
            body_container.controls = build_category_view("科技")
        elif index == 2:
            body_container.controls = build_category_view("娱乐")
        elif index == 3:
            body_container.controls = build_category_view("开发")
        elif index == 4:
            body_container.controls = build_category_view("设计")
            
        # 刷新页面
        # 注意：这里需要 try-catch，防止极快切换时的极端情况，虽然逻辑上已经修正了add顺序
        try:
            body_container.scroll_to(offset=0, duration=100)
        except Exception:
            pass 
        page.update()

    # 6. 初始化 Appbar 并绑定回调
    page.appbar = get_app_bar(on_nav_change=handle_nav_change)
    
    # --- 关键顺序修正 ---
    # 7. 先将容器添加到页面
    page.add(body_container)

    # 8. 再加载首页数据 (触发 update)
    handle_nav_change(0)

if __name__ == "__main__":
    # 建议使用 Web 模式测试 IP，方便刷新
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)