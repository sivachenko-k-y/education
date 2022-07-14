from kivy.app import App            # класс "окно\приложение"
from kivy.uix.button import Button  # класс "кнопка"


class MyApp(App):# имя класса - имя загаловка окна пр., должно заканчиваться на App

    def build(self):
        btn1 = Button(text='Hello world', font_size=14)

        def callback(instance):
            print('The button <%s> is being pressed' % instance.text)

        btn1.bind(on_press=callback)

        return btn1





if __name__ == "__main__":          # если текущий модуль это  __main__,то
    MyApp().run()                   # создаем экземпляр и вызываем метод
