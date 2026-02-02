from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

from game import GameWidget

# App background color
Window.clearcolor = (0.4, 0.47, 0.55, 1)


class HomeScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation='vertical',
            spacing=20,
            padding=30
        )

        layout.add_widget(Image(
            source='iplogo.jpg',
            size_hint=(1, 0.3)
        ))

        layout.add_widget(Label(
            text="Catch an Alien 👽",
            font_size=34
        ))

        start_btn = Button(
            text="Start Game",
            size_hint=(1, 0.2),
            background_color=(0, 0.45, 0.85, 1)
        )

        start_btn.bind(on_press=self.go_to_game)

        layout.add_widget(start_btn)
        self.add_widget(layout)

    def go_to_game(self, instance):
        self.manager.current = "game"


class GameScreen(Screen):

    def on_enter(self):
        self.start_game()

    def start_game(self):
        self.clear_widgets()
        game = GameWidget(on_restart=self.start_game)
        self.add_widget(game)


class CatchAlienApp(App):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(GameScreen(name="game"))
        return sm


if __name__ == "__main__":
    CatchAlienApp().run()

