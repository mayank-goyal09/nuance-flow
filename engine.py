import torch
from transformers import pipeline

class EmotionEngine:
    def __init__(self):
        # We use DistilBERT fine-tuned model
        # 1. Try local path first
        self.local_model_path = "./final_emotion_model_v2"
        # 2. Hugging Face repository ID for remote deployment
        self.hf_model_id = "mayankg09/emotion-analytics-distilbert"
        
        import os
        if os.path.isdir(self.local_model_path):
            self.model_name = self.local_model_path
            print(f"⚙️ Loading local model from: {self.model_name}...")
        else:
            self.model_name = self.hf_model_id
            print(f"⚙️ Local model not found. Loading from Hugging Face Hub: {self.model_name}...")
        
        # Load the pipeline
        try:
            self.classifier = pipeline(
                "text-classification", 
                model=self.model_name, 
                top_k=None # Returns all emotions with scores
            )
            print(f"✅ Successfully loaded model: {self.model_name}")
        except Exception as e:
            print(f"⚠️ Failed to load model '{self.model_name}'. Error: {e}")
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