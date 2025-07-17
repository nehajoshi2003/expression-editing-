# main.py
from emotion_detector import get_emotions
from emotion_viewer import show_expression_sequence

import time
from nltk.tokenize import sent_tokenize
import nltk
nltk.download('punkt')  # Only needed once
import spacy
nlp = spacy.load("en_core_web_sm")
paragraph = input("Enter a paragraph describing emotions: ")
sentences = [sent.text for sent in nlp(paragraph).sents]
EMOTION_MAP = {
    "Joy": "Happy",
    "Anger": "Anger",
    "Fear": "Fear",
    "Sadness": "Sad",
    "Surprise": "Surprise"
}




# Detect emotions per sentence
ordered_emotions = []
for sentence in sentences:
    emotions = get_emotions(sentence)
    for emo in emotions:
        if emo not in ordered_emotions:
            ordered_emotions.append(emo)

print("Detected emotions:", list(set(ordered_emotions)))
print("Ordered emotions based on paragraph:", ordered_emotions)

# Map to filenames
mapped_expressions = []
for emotion in ordered_emotions:
    if emotion in EMOTION_MAP:
        mapped_expressions.append(EMOTION_MAP[emotion])
    else:
        print(f"⚠️ No mapped file for emotion: {emotion}")

print("Final expression list to show:", mapped_expressions)

# Show them
show_expression_sequence(mapped_expressions)
