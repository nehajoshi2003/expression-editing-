from transformers import pipeline
EMOTION_MAP = {
    "Joy": "Happy",
    "Anger": "Anger",
    "Fear": "Fear",
    "Sadness": "Sad",
    "Surprise": "Surprise"
}

def get_emotions(paragraph):
    classifier = pipeline(
        "text-classification",
        model="j-hartmann/emotion-english-distilroberta-base",
        top_k=2
    )
    results = classifier(paragraph)
    
    # Handle both single and multi result cases
    if isinstance(results[0], list):
        results = results[0]

    return [r['label'].capitalize() for r in results]
