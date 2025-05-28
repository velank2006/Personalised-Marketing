
import random

# Sample data
users = [
    {"id": 1, "name": "Alice", "interests": ["fashion", "skincare"], "purchase_history": ["dress", "lipstick"]},
    {"id": 2, "name": "Bob", "interests": ["electronics", "gaming"], "purchase_history": ["headphones", "mouse"]},
    {"id": 3, "name": "Carol", "interests": ["books", "wellness"], "purchase_history": ["novel", "yoga mat"]}
]

products = {
    "fashion": ["sunglasses", "handbag", "sneakers"],
    "skincare": ["moisturizer", "face mask", "serum"],
    "electronics": ["smartwatch", "tablet", "Bluetooth speaker"],
    "gaming": ["gaming chair", "keyboard", "VR headset"],
    "books": ["thriller novel", "poetry book", "biography"],
    "wellness": ["meditation app", "protein shake", "foam roller"]
}

offers = [
    "20% OFF on your next purchase!",
    "Buy 1 Get 1 Free offer!",
    "Exclusive access to early product launches!",
    "Free shipping for the next 3 orders!"
]

def recommend_products(user):
    recommendations = []
    for interest in user["interests"]:
        recommendations += random.sample(products.get(interest, []), k=1)
    return recommendations

def generate_offer():
    return random.choice(offers)

def personalize_marketing(user):
    print(f"Hello {user['name']}!")
    print("Based on your interests, we recommend:")
    for product in recommend_products(user):
        print(f" - {product}")
    print("Special offer just for you:")
    print(f" - {generate_offer()}")
    print("-" * 40)

# Simulate personalized marketing for all users
for user in users:
    personalize_marketing(user)





