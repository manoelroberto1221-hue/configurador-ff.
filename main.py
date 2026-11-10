import json
from pathlib import Path

from kivy.app import App
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup

DEFAULTS = {
    "Geral": 90,
    "Ponto vermelho": 85,
    "Mira 2x": 80,
    "Mira 4x": 75,
    "Mira AWM": 50,
    "Olhadinha": 70,
}

class ConfiguradorApp(App):
    def build(self):
        self.title = "Configurador FF"
        self.config_path = Path(self.user_data_dir) / "sensibilidade.json"
        self.values = self.load_values()
        self.sliders = {}

        scroll = ScrollView()
        page = BoxLayout(orientation="vertical", padding=dp(18),
                         spacing=dp(12), size_hint_y=None)
        page.bind(minimum_height=page.setter("height"))

        title = Label(text="[b]CONFIGURADOR DE SENSIBILIDADE[/b]",
                      markup=True, font_size="21sp",
                      size_hint_y=None, height=dp(48))
        page.add_widget(title)

        note = Label(
            text="Ajuste e salve seus valores. As configurações são sugestões "
                 "e não alteram o Free Fire automaticamente.",
            font_size="14sp", size_hint_y=None, height=dp(64),
            halign="center", valign="middle")
        note.bind(size=lambda obj, size: setattr(obj, "text_size", size))
        page.add_widget(note)

        for name, default in DEFAULTS.items():
            block = BoxLayout(orientation="vertical", spacing=dp(3),
                              size_hint_y=None, height=dp(86))
            value_label = Label(text=f"{name}: {self.values.get(name, default)}",
                                font_size="16sp", size_hint_y=None,
                                height=dp(28), halign="left")
            value_label.bind(size=lambda obj, size: setattr(obj, "text_size", size))
            slider = Slider(min=0, max=200, step=1,
                            value=self.values.get(name, default))
            slider.bind(value=lambda instance, value, n=name, label=value_label:
                        self.update_value(n, value, label))
            self.sliders[name] = slider
            block.add_widget(value_label)
            block.add_widget(slider)
            page.add_widget(block)

        save_btn = Button(text="SALVAR CONFIGURAÇÕES",
                          size_hint_y=None, height=dp(52))
        save_btn.bind(on_release=self.save_values)
        page.add_widget(save_btn)

        reset_btn = Button(text="RESTAURAR VALORES PADRÃO",
                           size_hint_y=None, height=dp(48))
        reset_btn.bind(on_release=self.reset_values)
        page.add_widget(reset_btn)

        scroll.add_widget(page)
        return scroll

    def load_values(self):
        try:
            with self.config_path.open("r", encoding="utf-8") as file:
                data = json.load(file)
            return {key: int(data.get(key, value)) for key, value in DEFAULTS.items()}
        except (OSError, ValueError, TypeError):
            return DEFAULTS.copy()

    def update_value(self, name, value, label):
        self.values[name] = int(value)
        label.text = f"{name}: {int(value)}"

    def save_values(self, *_):
        self.values = {name: int(slider.value) for name, slider in self.sliders.items()}
        self.config_path.parent.mkdir(parents=True, exist_ok=True)
        with self.config_path.open("w", encoding="utf-8") as file:
            json.dump(self.values, file, ensure_ascii=False, indent=2)
        self.show_message("Configurações salvas neste aplicativo.")

    def reset_values(self, *_):
        for name, default in DEFAULTS.items():
            self.sliders[name].value = default
        self.show_message("Valores padrão restaurados. Toque em SALVAR para gravar.")

    def show_message(self, message):
        Popup(title="Pronto", content=Label(text=message, halign="center"),
              size_hint=(0.82, 0.28)).open()

if __name__ == "__main__":
    ConfiguradorApp().run()
