"""
data_loader.py  —  GoEmotions Dataset Fetcher
Fetches ~58k Reddit comments labeled with 27 emotions + neutral
from Google's GoEmotions dataset via HuggingFace Datasets.

Reference: https://www.tensorflow.org/datasets/catalog/goemotions
"""

from datasets import load_dataset
import pandas as pd

ALL_LABELS = [
    'admiration', 'amusement', 'anger', 'annoyance', 'approval',
    'caring', 'confusion', 'curiosity', 'desire', 'disappointment',
    'disapproval', 'disgust', 'embarrassment', 'excitement', 'fear',
    'gratitude', 'grief', 'joy', 'love', 'nervousness',
    'optimism', 'pride', 'realization', 'relief', 'remorse',
    'sadness', 'surprise', 'neutral'
]

# Our 6 Business-Critical Emotions
TARGET_EMOTIONS = ['joy', 'love', 'anger', 'sadness', 'fear', 'surprise']
EMOTION_LABELS = ALL_LABELS # Keep reference for loading


def load_goemotions_to_df(num_samples: int = 5000) -> pd.DataFrame:
    """
    Downloads GoEmotions from HuggingFace, maps integer label IDs to 
    human-readable emotion names, and saves to mock_data.csv.

    Args:
        num_samples: Number of rows to save (default 5000 for fast MVP).
                     Set to None to load the entire training split (~43k rows).

    Returns:
        pd.DataFrame with columns: text, label_id, emotion
    """
    print("🚀 Fetching GoEmotions from HuggingFace Servers...")

    # The 'simplified' config has 28 labels (27 emotions + neutral)
    # mapped as integer IDs in a 'labels' column (multi-label list).
    # Download is only ~4 MB — very lightweight!
    dataset = load_dataset("go_emotions", "simplified", split="train")

    data = []
    limit = num_samples if num_samples else len(dataset)

    for i, example in enumerate(dataset):
        if i >= limit:
            break

        text = example['text']
        labels = example['labels']  # list of integer IDs, e.g. [0, 4]

        # Filter for our 6 Business Critical Emotions
        # If the label isn't in our list, we skip it (or treat as neutral/ignore)
        # 27 is neutral in the simplified dataset
        label_id = labels[0] if labels else 27
        if label_id >= len(EMOTION_LABELS): continue # Safety check

        original_emotion = EMOTION_LABELS[label_id]
        
        # We only keep rows that match our target list
        if original_emotion in TARGET_EMOTIONS:
            data.append({
                'text': text,
                'label': original_emotion,
                'label_id': TARGET_EMOTIONS.index(original_emotion) # Remap to 0-5
            })

    df = pd.DataFrame(data)

    df = pd.DataFrame(data)

    if df.empty:
        print("⚠️ Warning: No data found matching target emotions!")
        return df

    # We already have 'emotion' column from the loop above, and 'label_id' is 0-5
    df['emotion'] = df['label'] # Just ensuring column name matches expectations

    print(f"✅ Data Ready! {len(df)} rows loaded.")
    print(f"📊 Emotion distribution (top 10):")
    print(df['emotion'].value_counts().head(10).to_string())
    print(f"\n🔍 Sample rows:")
    print(df.head().to_string(index=False))

    # Save locally so we don't re-download every time
    df.to_csv('mock_data.csv', index=False)
    print(f"\n💾 Saved to mock_data.csv ({len(df)} rows)")

    return df


if __name__ == "__main__":
    load_goemotions_to_df()