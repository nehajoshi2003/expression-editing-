from transformers import pipeline

# Load a pre-trained emotion detection model
emotion_classifier = pipeline("text-classification", 
                              model="j-hartmann/emotion-english-distilroberta-base", 
                              return_all_scores=False)

def detect_emotion(text):
    result = emotion_classifier(text)[0]
    emotion = result['label']
    score = result['score']
    return emotion, score

# Example
if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    emotion, score = detect_emotion(sentence)
    print(f"Detected Emotion: {emotion} (confidence: {score:.2f})")
