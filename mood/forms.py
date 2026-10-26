from django import forms

MOODS = [
    ("1", "Sehr schlecht"),
    ("2", "Schlecht"),
    ("3", "Neutral"),
    ("4", "Gut"),
    ("5", "Sehr gut"),
]


class MoodForm(forms.Form):
    score = forms.ChoiceField(choices=MOODS, error_messages={
        "required": "Bitte wähle einen Smiley aus.",
        "invalid_choice": "Diese Stimmung ist nicht gültig.",
    })
