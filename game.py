import random
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.animation import Animation
from kivy.core.audio import SoundLoader

# Game configuration
GAME_DURATION = 60        # seconds
ALIEN_COUNT = 4           # aliens on screen
MOVE_INTERVAL = 2         # seconds


class GameWidget(FloatLayout):

    def __init__(self, on_restart=None, **kwargs):
        super().__init__(**kwargs)

        # --- Background Image ---
        self.bg = Image(
            source="galaxy3.png",
            allow_stretch=True,
            keep_ratio=False,
            size_hint=(1, 1),
            pos_hint={"x": 0, "y": 0}
        )
        self.add_widget(self.bg)

        self.on_restart = on_restart
        self.score = 0
        self.time_left = GAME_DURATION
        self.aliens = []

        # Background music
        self.bg_music = SoundLoader.load(
            "catchalienmusic.mp3"
        )
        if self.bg_music:
            self.bg_music.loop = True
            self.bg_music.play()

        # Score (top-left)
        self.score_label = Label(
            text="Score: 0",
            pos_hint={"x": 0.02, "top": 0.98},
            font_size=20
        )

        # Timer (top-right)
        self.timer_label = Label(
            text=f"Time: {GAME_DURATION}",
            pos_hint={"right": 0.98, "top": 0.98},
            font_size=20
        )

        self.add_widget(self.score_label)
        self.add_widget(self.timer_label)

        # Create aliens
        for _ in range(ALIEN_COUNT):
            alien = Image(
                source="alien.png",
                size_hint=(0.18, 0.18)
            )
            alien.bind(on_touch_down=self.catch_alien)
            self.aliens.append(alien)
            self.add_widget(alien)

        # Schedule events
        self.move_event = Clock.schedule_interval(self.move_aliens, MOVE_INTERVAL)
        self.timer_event = Clock.schedule_interval(self.update_timer, 1)

        self.move_aliens(0)

    # Move aliens
    def move_aliens(self, dt):
        for alien in self.aliens:
            Animation(
                pos_hint={
                    "x": random.uniform(0.05, 0.8),
                    "y": random.uniform(0.05, 0.7)
                },
                duration=0.3
            ).start(alien)

    # Catch alien
    def catch_alien(self, alien, touch):
        if alien.collide_point(*touch.pos):
            self.score += 1
            self.score_label.text = f"Score: {self.score}"

            alien.pos_hint = {
                "x": random.uniform(0.05, 0.8),
                "y": random.uniform(0.05, 0.7)
            }

    # Update timer
    def update_timer(self, dt):
        self.time_left -= 1
        self.timer_label.text = f"Time: {self.time_left}"

        if self.time_left <= 0:
            self.end_game()

    # End game
    def end_game(self):
        Clock.unschedule(self.move_event)
        Clock.unschedule(self.timer_event)

        if self.bg_music:
            self.bg_music.stop()

        self.clear_widgets()

        container = BoxLayout(
            orientation="vertical",
            size_hint=(1, 1),
            padding=30,
            spacing=20
        )

        final_label = Label(
            text=f"⏱ Time Up!\n\nFinal Score: {self.score}",
            font_size=36,
            halign="center",
            valign="middle"
        )

        final_label.bind(
            size=lambda instance, value: setattr(instance, "text_size", value)
        )

        restart_btn = Button(
            text="Play Again",
            size_hint=(0.6, 0.15),
            pos_hint={"center_x": 0.5}
        )

        restart_btn.bind(on_press=lambda x: self.on_restart())

        container.add_widget(final_label)
        container.add_widget(restart_btn)
        self.add_widget(container)

