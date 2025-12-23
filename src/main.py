import flet as ft
from data_service import DataService
from components.app_bar import get_app_bar
from components.platform_header import PlatformHeader
from components.topic_card import TopicCard
from components.footer import Footer  # 【新增】导入 Footer

def main(page: ft.Page):
    # 1. 页面基础设置
    page.title = "今日热榜 - Clone"
    # 设置浅灰色背景，这样白色的 Header 和 Card 才会显眼
    page.bgcolor = "#f5f7f9" 
    page.padding = 0
    page.theme_mode = ft.ThemeMode.LIGHT
    
    # 2. 获取数据
    data_list = DataService.get_mock_data()

    # 3. 初始化头部区域
    # 这是一个独立的 Container，会被放置在列表的最上方
    header_section = PlatformHeader(data_list)

    # 4. 初始化卡片网格
    grid_items = []
    for item in data_list:
        grid_items.append(
            ft.Column(
                controls=[TopicCard(item)],
                # 响应式列宽：大屏一行4个，中屏3个，平板2个，手机1个
                col={"sm": 12, "md": 6, "lg": 4, "xl": 3} 
            )
        )

    content_grid = ft.ResponsiveRow(
        controls=grid_items,
        run_spacing=20, # 卡片上下间距
        spacing=20      # 卡片左右间距
    )

    # 5. 主布局结构
    # 使用 ListView 实现页面级滚动
    main_layout = ft.ListView(
        controls=[
            # --- 区域 1：头部平台信息 ---
            header_section,
            
            # --- 区域 2：卡片网格 ---
            ft.Container(
                content=content_grid,
                # 给网格区域增加内边距，使其不紧贴屏幕边缘
                padding=ft.padding.symmetric(horizontal=20, vertical=10) 
            ),
            
            # --- 区域 3：页脚 (替换了原来的空白 Container) ---
            Footer()  # 【修改点】在这里添加 Footer
        ],
        expand=True, # 占满整个 Body 区域
        spacing=0    # 控件之间的默认间距设为0，由各控件自身的 margin 控制
    )

    # 6. 组装页面
    # Appbar 是固定在顶部的，不随 ListView 滚动
    page.appbar = get_app_bar()
    
    # main_layout 是页面的主体内容
    page.add(main_layout)

if __name__ == "__main__":
    ft.app(target=main)