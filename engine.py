import torch
from transformers import pipeline

class EmotionEngine:
    def __init__(self):
        # We use DistilBERT: Smaller, Faster, Cheaper!
        # This model is already fine-tuned on GoEmotions
        # We use DistilBERT local model after training
        self.model_name = "./final_emotion_model_v2"
        # Fallback to base if training isn't done yet (though this won't work perfectly without training)
        # self.model_name = "distilbert-base-uncased" 
        print(f"⚙️ Loading the Brain: {self.model_name}...")
        
        # Load the pipeline
        try:
            self.classifier = pipeline(
                "text-classification", 
                model=self.model_name, 
                top_k=None # Returns all emotions with scores
            )
        except Exception as e:
            print(f"⚠️ specific model not found locally. Please run train.py first! Error: {e}")
            self.classifier = None
        
        # Mapping 6 Business Emotions to Action Buckets
        self.action_map = {
            'joy': 'PROMOTER', 
            'love': 'PROMOTER',
            'anger': 'CRITICAL',
            'sadness': 'CRITICAL',
            'fear': 'URGENT',
            'surprise': 'MONITOR'
        }

    def predict(self, text, threshold=0.6):
        if self.classifier is None:
            return {"label": "Error", "score": 0.0, "action": "Model Not Found"}

        results = self.classifier(text)[0]
        
        # Filter by threshold for "Uncertainty Logic"
        top_prediction = results[0] # The one with highest score
        
        if top_prediction['score'] < threshold:
            return {
                "label": "Ambiguous",
                "score": top_prediction['score'],
                "action": "Human Review Required 🔍"
            }
        
        # Get the business action
        action = self.action_map.get(top_prediction['label'], 'General Monitor 📊')
        
        return {
            "label": top_prediction['label'],
            "score": round(top_prediction['score'], 4),
            "action": action
        }

# Quick Test
if __name__ == "__main__":
    engine = EmotionEngine()
    print(engine.predict("I am so frustrated with the slow shipping!"))