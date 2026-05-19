import pandas as pd
import random

# Mapping based on data_loader.py and training config
# 0: Joy, 1: Love, 2: Anger, 3: Sadness, 4: Fear, 5: Surprise

EMOTION_MAP = {
    'joy': 0,
    'love': 1,
    'anger': 2,
    'sadness': 3,
    'fear': 4,
    'surprise': 5
}

# ------------------------------------------------------------------
# Diverse Test Templates
# ------------------------------------------------------------------

# JOY (0) - Satisfaction, success, ease of use
joy_templates = [
    "I'm thrilled with how easy the {product} was to set up!",
    "The new update is fantastic, everything runs so smoothly now.",
    "Finally found a solution that actually works as advertised. Great job!",
    "Customer support was helpful and resolved my issue in minutes.",
    "The dashboard gives me exactly the insights I need. Perfect!",
    "Highly impressed with the speed of delivery. Arrived early!",
    "This software has saved our team hours of work every week.",
    "The quality of the materials is excellent. Very satisfied.",
    "A seamless experience from checkout to unboxing.",
    "I'm enjoying using this platform, it's very intuitive."
]

# LOVE (1) - Strong passion, brand loyalty, delight
love_templates = [
    "I absolutely love this brand! You guys are the best.",
    "This is hands down the best {product} I've ever owned.",
    "I'm obsessed with the design. It's beautiful!",
    "Thank you for creating such an amazing community. ❤️",
    "I can't imagine running my business without this tool anymore.",
    "You won a loyal customer for life. Keep it up!",
    "The attention to detail is incredible. I'm in love with it.",
    "Superb! I've recommended it to all my colleagues.",
    "This features is a lifesaver! Love it!",
    "Truly outstanding service that goes above and beyond."
]

# ANGER (2) - Frustration, bugs, poor service
anger_templates = [
    "This is ridiculous. The app crashes every time I open it.",
    "I've been waiting for a refund for weeks! Unacceptable.",
    "Worst customer service experience ever. No one answers the phone.",
    "The {product} broke immediately after the warranty expired.",
    "Stop sending me spam emails! I unsubscribed three times.",
    "The instructions are completely wrong. Waste of time.",
    "I am very angry about the hidden fees on my bill.",
    "Your latest update ruined the workflow. Fix it now!",
    "Don't buy this. It's a scam.",
    "The driver was rude and threw the package on the ground."
]

# SADNESS (3) - Disappointment, regret, loss
sadness_templates = [
    "I was really hoping this would work, but it didn't.",
    "Sad to see the quality go down over the years.",
    "Unfortunately, the {product} doesn't fit my needs.",
    "I miss the old version. The new one is confusing.",
    "Disappointed that the feature I paid for isn't included.",
    "It's a shame, I really wanted to like this product.",
    "I regret buying this. Should have done more research.",
    "The item arrived damaged and now it's out of stock.",
    "Sorry to say, but I'll be cancelling my subscription.",
    "It's just not what it used to be. Very disappointing."
]

# FEAR (4) - Security, data loss, urgent risks
fear_templates = [
    "Is my data safe? I see suspicious login attempts.",
    "The battery is overheating and I'm worried it might catch fire.",
    "I'm scared I lost all my files after the sync failed.",
    "There's a serious security vulnerability in the login page.",
    "Please help! My account has been hacked.",
    "I'm afraid to use this on my main computer due to the virus warning.",
    "Urgent! The server is down and we are losing customers.",
    "The tracking says delivered but I can't find it. I'm worried it was stolen.",
    "This feels unsafe. The verification process is flawed.",
    "I'm panic-stricken. I verified the transaction but it's not showing up."
]

# SURPRISE (5) - Unexpected results, confusion, shock
surprise_templates = [
    "Wow, I didn't expect it to arrive so quickly!",
    "I'm surprised by how many features are included in the free plan.",
    "The box was huge! I wasn't expecting that.",
    "Wait, checking out was instant? That was fast.",
    "I was shocked to see the price drop so much.",
    "Oh! I didn't know it could do that.",
    "Actually, this is much better than I thought it would be.",
    "I'm confused, the manual says one thing but the app does another.",
    "Startled by the loud notification sound. Can I change it?",
    "It's surprisingly heavy for its size."
]

products = ["laptop", "service", "app", "subscription", "interface", "tool", "platform", "delivery", "update", "system"]

data = []

# Generate 50 test samples
# Ensure balanced distribution for testing
for _ in range(50):
    emotion_key = random.choice(list(EMOTION_MAP.keys()))
    product = random.choice(products)
    
    if emotion_key == 'joy':
        text = random.choice(joy_templates).format(product=product)
    elif emotion_key == 'love':
        text = random.choice(love_templates).format(product=product)
    elif emotion_key == 'anger':
        text = random.choice(anger_templates).format(product=product)
    elif emotion_key == 'sadness':
        text = random.choice(sadness_templates).format(product=product)
    elif emotion_key == 'fear':
        text = random.choice(fear_templates).format(product=product)
    elif emotion_key == 'surprise':
        text = random.choice(surprise_templates).format(product=product)
        
    label_id = EMOTION_MAP[emotion_key]
    
    data.append([text, label_id, emotion_key])

# Specific Edge Cases for Business Testing
edge_cases = [
    ["The product is okay, but I'm worried about the long-term support.", 4, "fear"],  # Mixed neutral/fear
    ["I hate the new logo, but the service is still great.", 2, "anger"],            # Mixed anger/joy -> likely anger dominates
    ["Oh my god, the new feature is finally here!", 5, "surprise"],                 # Excitement/Surprise
    ["We are shutting down our account due to lack of usage.", 3, "sadness"],         # Churn signal (Sadness/Disappointment)
    ["URGENT: The payment gateway is throwing 500 errors.", 4, "fear"]               # Critical infra issue
]

data.extend(edge_cases)

df = pd.DataFrame(data, columns=['text', 'label_id', 'emotion'])
filename = 'test_dataset.csv'
df.to_csv(filename, index=False)

print(f"✅ Generated {len(df)} test samples in '{filename}' covering all 6 business emotions.")
print(df['emotion'].value_counts())
