import pandas as pd
from sklearn.model_selection import train_test_split
import torch
from transformers import AutoTokenizer

# 1. Load your downloaded data
df = pd.read_csv('mock_data.csv')

# 2. Split the data (80% Train, 20% Test)
# This is crucial for professional projects to avoid 'overfitting'
# 2. Split the data (80% Train, 20% Test)
# We now have exactly 6 classes (0-5)
train_texts, val_texts, train_labels, val_labels = train_test_split(
    df['text'].tolist(), 
    df['label_id'].tolist(), # These are now 0-5
    test_size=0.2, 
    random_state=42
)

# 3. Load the Tokenizer
# We use DistilBERT because it's fast and lightweight for your laptop
model_checkpoint = "distilbert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)

# 4. Create the Tokenization Function
def tokenize_data(texts):
    return tokenizer(
        texts, 
        padding=True, 
        truncation=True, 
        max_length=128, # Keeping it short for speed
        return_tensors="pt" # Output as PyTorch tensors
    )

class EmotionDataset(torch.utils.data.Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __getitem__(self, idx):
        item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        item['labels'] = torch.tensor(self.labels[idx])
        return item

    def __len__(self):
        return len(self.labels)

# Prepare the final datasets
train_encodings = tokenize_data(train_texts)
val_encodings = tokenize_data(val_texts)

train_dataset = EmotionDataset(train_encodings, train_labels)
val_dataset = EmotionDataset(val_encodings, val_labels)
print(f"Preprocessing Done! Training on {len(train_texts)} samples.")