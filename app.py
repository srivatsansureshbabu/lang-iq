from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.uix.textinput import TextInput

# Set light green background
Window.clearcolor = get_color_from_hex('#b3ffb3')

# ------------------ Functions outside the class ------------------

def createTitle(layout):
    title = Label(
        text="[b][i]LangIQ[/i][/b]",
        markup=True,
        font_size='36sp',
        color=get_color_from_hex('#006600'),
        size_hint=(1, 0.25),
        halign='center',
        valign='middle'
    )
    title.bind(size=title.setter('text_size'))
    layout.add_widget(title)

def createEnglishInput(layout):
    # Horizontal layout for label + textbox
    horizontalLayout = BoxLayout(orientation='horizontal', spacing=10, size_hint=(1, 0.15))

    englishTitle = Label(
        text="[b][i]Insert English Text > [/i][/b]",
        markup=True,
        font_size='24sp',
        color=get_color_from_hex('#006600'),
        size_hint=(0.4, 1),
        halign='right',
        valign='middle'
    )
    englishTitle.bind(size=englishTitle.setter('text_size'))

    englishInput = TextInput(
        hint_text="Type English text here...",
        multiline=False,
        size_hint=(0.6, 1)
    )

    # Add label and input to horizontal layout
    horizontalLayout.add_widget(englishTitle)
    horizontalLayout.add_widget(englishInput)

    # Add horizontal layout to main vertical layout
    layout.add_widget(horizontalLayout)

    return englishInput

def createResultLabel(layout):
    resultLabel = Label(
        text="Press the button!",
        font_size='24sp',
        color=(0, 0, 0, 1),
        size_hint=(1, 0.2),
        halign='center',
        valign='middle'
    )
    resultLabel.bind(size=resultLabel.setter('text_size'))
    layout.add_widget(resultLabel)
    return resultLabel

def createButton(layout, englishInput, resultLabel, tamilOutput):
    translateButton = Button(
        text="Translate",
        font_size='24sp',
        size_hint=(0.6, 0.2),
        pos_hint={'center_x': 0.5},
        background_color=get_color_from_hex('#66cc66')
    )

    def onPress(instance):
        tamilOutput.text = englishInput.text
        resultLabel.text = f"You typed: {englishInput.text}"

    translateButton.bind(on_press=onPress)
    layout.add_widget(translateButton)

def createTamilOutput(layout):
    """
    Creates a horizontal layout with a label 'Tamil Output >' 
    and a TextInput to display the translation output, aligned with English input.
    """
    horizontalLayout = BoxLayout(orientation='horizontal', spacing=10, size_hint=(1, 0.15))

    tamilTitle = Label(
        text="[b][i]Tamil Output > [/i][/b]",
        markup=True,
        font_size='24sp',
        color=get_color_from_hex('#006600'),
        size_hint=(0.4, 1),      # same as English label
        halign='right',
        valign='middle'
    )
    tamilTitle.bind(size=tamilTitle.setter('text_size'))

    tamilOutput = TextInput(
        hint_text="Translation will appear here...",
        multiline=False,
        readonly=True,
        size_hint=(0.6, 1)       # same as English textbox
    )

    horizontalLayout.add_widget(tamilTitle)
    horizontalLayout.add_widget(tamilOutput)

    layout.add_widget(horizontalLayout)

    return tamilOutput

# ------------------ Kivy App ------------------

class LangIQApp(App):
    def build(self):
        self.mainLayout = BoxLayout(orientation='vertical', padding=[20, 50, 20, 50], spacing=30)

        # Build UI using external functions
        createTitle(self.mainLayout)
        self.englishInput = createEnglishInput(self.mainLayout)
        self.resultLabel = createResultLabel(self.mainLayout)
        self.tamilOutput = createTamilOutput(self.mainLayout)

        createButton(self.mainLayout, self.englishInput, self.resultLabel, self.tamilOutput)

        return self.mainLayout

if __name__ == "__main__":
    LangIQApp().run()
