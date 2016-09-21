from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Label
from kivy.properties import StringProperty



class StringLoop(App):
    def __init__(self, **kwargs):
        """
        Construct main app
        """
        super().__init__(**kwargs)
        self.strings = ["Hello", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    def build(self):
        """
        Build the Kivy GUI
        :return: reference to the root Kivy widget
        """
        self.title = "String Looping"
        self.root = Builder.load_file('string_loop.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """
        Create buttons from dictionary entries and add them to the GUI
        :return: None
        """
        for sentence in self.strings:
            # create a button for each string entry
            temp_label = Label(text=sentence)
            # add the button to the "stringsBox" using add_widget()
            self.root.ids.stringsBox.add_widget(temp_label)


StringLoop().run()
