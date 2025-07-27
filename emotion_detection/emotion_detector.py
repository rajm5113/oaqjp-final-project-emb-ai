from transformers import pipeline

classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", top_k=None)

def emotion_detector(text_to_analyze):
    try:
        result = classifier(text_to_analyze)[0]
        emotions = {entry['label'].lower(): round(entry['score'], 2) for entry in result}
        dominant_emotion = max(emotions, key=emotions.get)
        emotions["dominant_emotion"] = dominant_emotion
        return emotions
    except Exception as e:
        return {"error": str(e)}

