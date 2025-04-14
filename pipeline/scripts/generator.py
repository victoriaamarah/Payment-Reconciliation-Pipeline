import random
import json
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

def generate_stripe_payment_intent():
    return {
        "id": f"pi_{fake.lexify(text='????????????????')}",
        "amount": random.randint(500, 100000),
        "currency": random.choice(["usd", "eur", "gbp", "cad"]),
        "status": random.choice(["succeeded", "requires_payment_method", "processing", "requires_action", "canceled"]),
        "description": fake.sentence(nb_words=4),
        "customer_email": fake.email(),
        "created": int(fake.date_time_between(start_date="-30d", end_date="now").timestamp()),
        "payment_method": f"pm_{fake.lexify(text='????????????????')}",
        "payment_method_details": {
            "type": "card",
            "card": {
                "brand": random.choice(["visa", "mastercard", "amex"]),
                "last4": fake.credit_card_number()[-4:],
                "exp_month": random.randint(1, 12),
                "exp_year": random.randint(2025, 2030)
            }
        },
        "metadata": {
            "order_id": fake.uuid4()
        }
    }

def save_json(file_path="stripe_payments.json"):
    count = random.randint(50, 100)
    print(f"Generating {count} records...")
    data = [generate_stripe_payment_intent() for _ in range(count)]
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)
    print(f"✅ Saved JSON to {file_path}")
    return file_path
