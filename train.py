from transformers import AutoModelForSequenceClassification, TrainingArguments, Trainer
import numpy as np
from sklearn.metrics import accuracy_score, f1_score
from preprocess import train_dataset, val_dataset  # Import the datasets!

# 1. Load the Model Architecture
# We use DistilBERT + a 'head' for 6 Business Classes
# (Joy, Love, Anger, Sadness, Fear, Surprise)
TARGET_EMOTIONS = ['joy', 'love', 'anger', 'sadness', 'fear', 'surprise']
id2label = {i: label for i, label in enumerate(TARGET_EMOTIONS)}
label2id = {label: i for i, label in enumerate(TARGET_EMOTIONS)}

model = AutoModelForSequenceClassification.from_pretrained(
    "distilbert-base-uncased", 
    num_labels=6,
    id2label=id2label,
    label2id=label2id
)

# 2. Define Metrics (To see how well we are doing)
def compute_metrics(eval_pred):
    logits, labels = eval_pred
    predictions = np.argmax(logits, axis=-1)
    # F1 score is better for business because some emotions are rare!
    f1 = f1_score(labels, predictions, average='weighted')
    acc = accuracy_score(labels, predictions)
    return {"accuracy": acc, "f1": f1}

# 3. Training Settings (The "Strategy")
training_args = TrainingArguments(
    output_dir="./emotion_model_results",
    num_train_epochs=6,              # 6 rounds through the data for perfect convergence
    per_device_train_batch_size=16,  # Adjust based on your RAM
    per_device_eval_batch_size=64,
    warmup_steps=10,                 # Fast ramp up for small dataset!
    weight_decay=0.01,               # Prevents 'overfitting'
    logging_dir='./logs',
    logging_steps=10,
    eval_strategy="epoch",            # Check progress after every round (Renamed from evaluation_strategy)
    save_strategy="epoch",
    load_best_model_at_end=True,      # Keep the 'smartest' version
)

# 4. The Trainer (The "Coach")
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,     # From our previous step
    eval_dataset=val_dataset,       # From our previous step
    compute_metrics=compute_metrics,
)

# 5. EXECUTE!
print("Training is starting... Your laptop might get warm!")
trainer.train()

# 6. Save the Final 'Brain' and Tokenizer
trainer.save_model("./final_emotion_model_v2")
from preprocess import tokenizer
tokenizer.save_pretrained("./final_emotion_model_v2")
print("SUCCESS! The model and tokenizer are trained and saved in './final_emotion_model_v2'")