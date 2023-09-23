from kivy.app import App
from kivy.core.window import Window
from kivy.uix.image import AsyncImage
from kivy.uix.pagelayout import PageLayout
Window.size = (415,914)
class test(App):
    def build(self):
        layout = PageLayout()
        layout.add_widget(AsyncImage(source = "https://www.code33.ir/wp-content/uploads/2023/09/Untitled.png"))
        layout.add_widget(AsyncImage(source = "https://www.code33.ir/wp-content/uploads/2023/09/Untitled.png"))
        layout.add_widget(AsyncImage(source = "https://www.code33.ir/wp-content/uploads/2023/09/Untitled.png"))
        layout.add_widget(AsyncImage(source = "https://www.code33.ir/wp-content/uploads/2023/09/Untitled.png"))
        return layout
test().run()