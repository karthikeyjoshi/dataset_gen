import random
import csv
from datetime import datetime
from jinja2 import Template
from faker import Faker
import nlpaug.augmenter.word as naw

# ----------------------------
# Define shorter phrase templates
# ----------------------------

growth_templates = [
    "I want high growth despite some risk.",
    "I'm aiming for high returns over time.",
    "I prefer aggressive growth opportunities."
]

income_templates = [
    "I need steady income with minimal risk.",
    "My priority is regular, reliable returns.",
    "I favor investments that generate consistent cash flow."
]

balanced_templates = [
    "I seek a balanced mix of growth and income.",
    "I'm looking for a portfolio that balances risk and reward.",
    "I want a strategy that offers both growth and stability."
]

risk_templates = {
    'Low': [
        "My risk tolerance is very low.",
        "I prefer investments with minimal risk.",
        "Safety is my main concern."
    ],
    'Medium': [
        "I'm comfortable with moderate risk.",
        "I accept some risk for better returns.",
        "I can handle a fair degree of volatility."
    ],
    'High': [
        "I'm willing to take high risks for high rewards.",
        "I accept significant volatility for aggressive growth.",
        "High risk is acceptable if the potential return is great."
    ]
}

time_horizon_templates = {
    'Short-term': [
        "I need results quickly.",
        "I'm focused on short-term gains.",
        "I prefer investments that mature fast."
    ],
    'Medium-term': [
        "I'm planning for the next few years.",
        "I want a strategy that works over 3-5 years.",
        "I'm looking at moderate-term investments."
    ],
    'Long-term': [
        "I'm investing for the long haul.",
        "I seek long-term growth.",
        "I'm planning to invest for over 5 years."
    ]
}

financial_situation_templates = {
    'Low': [
        "I have a limited budget.",
        "My funds are modest.",
        "I have small amounts to invest."
    ],
    'Medium': [
        "I have a comfortable amount to invest.",
        "My financial situation is stable.",
        "I have a decent budget for investing."
    ],
    'High': [
        "I have abundant capital.",
        "I'm financially secure and can invest aggressively.",
        "I have a strong financial foundation."
    ]
}

sectors = {
    'Technology': [
        "I like the technology sector.",
        "I'm interested in tech innovations.",
        "I favor investments in technology."
    ],
    'Healthcare': [
        "I support healthcare advancements.",
        "I prefer investments in healthcare.",
        "I'm drawn to the healthcare industry."
    ],
    'Finance': [
        "I'm interested in finance.",
        "I prefer financial sector investments.",
        "I like the stability of finance."
    ],
    'Energy': [
        "I favor energy investments.",
        "I like opportunities in the energy sector.",
        "I'm interested in both traditional and renewable energy."
    ],
    'Consumer Goods': [
        "I prefer consumer goods for steady returns.",
        "I'm interested in the consumer goods sector.",
        "I favor investments in everyday products."
    ],
    'Real Estate': [
        "I like real estate for its stability.",
        "I'm interested in property investments.",
        "Real estate appeals to me."
    ],
    'Utilities': [
        "I value the stability of utilities.",
        "Utilities are my preferred sector.",
        "I'm drawn to investments in utilities."
    ],
    'Telecom': [
        "I like the telecom sector.",
        "I'm interested in telecommunications.",
        "Telecom investments attract me."
    ]
}

# ----------------------------
# Revised Jinja2 Template for Concise Input
# ----------------------------
# Read in multiple templates from a CSV file
templates = []
with open("templates.csv", "r", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        templates.append(row["Template"])

# ----------------------------
# Dynamic Generation Function
# ----------------------------
def generate_user_input():
    # Choose a random template each time the function is called
    template_str = random.choice(templates)
    
    # Choose investment style and corresponding statement
    invest_style = random.choice(["Growth", "Income", "Balanced"])
    if invest_style == "Growth":
        chosen_invest = random.choice(growth_templates)
    elif invest_style == "Income":
        chosen_invest = random.choice(income_templates)
    else:
        chosen_invest = random.choice(balanced_templates)

    # Choose risk preference, time horizon, financial situation, and sector
    risk_pref = random.choice(["Low", "Medium", "High"])
    chosen_risk = random.choice(risk_templates[risk_pref])

    time_horizon = random.choice(["Short-term", "Medium-term", "Long-term"])
    chosen_time_horizon = random.choice(time_horizon_templates[time_horizon])

    fin_situation = random.choice(["Low", "Medium", "High"])
    chosen_fin_situation = random.choice(financial_situation_templates[fin_situation])

    sector_choice = random.choice(list(sectors.keys()))
    chosen_sector = random.choice(sectors[sector_choice])

    # Generate user data using Faker (can be omitted from the synthetic input text if desired)
    fake = Faker()
    user_name = fake.first_name()  # Use just first name for brevity
    generation_date = datetime.now().strftime("%Y-%m-%d")

    # Build context for template rendering
    context = {
        "financial_situation": chosen_fin_situation,
        "invest_style": invest_style,
        "risk": chosen_risk,
        "time_horizon": chosen_time_horizon,
        "sector": chosen_sector,
        "user_name": user_name,
        "generation_date": generation_date
    }

    template = Template(template_str)
    generated_text = template.render(context)
    final_text = generated_text.strip()
    return final_text, invest_style, risk_pref, time_horizon, fin_situation, sector_choice

# ----------------------------
# Optional: NLP Augmentation (tuned for brevity)
# ----------------------------
def augment_text(text):
    try:
        # Use a light augmentation that doesn't overly expand text length.
        aug = naw.SynonymAug(aug_src='wordnet', aug_min=1, aug_max=2)
        augmented = aug.augment(text)
        # Ensure the augmented text is not too long (truncate if necessary)
        return augmented if len(augmented) <= 250 else augmented[:250]
    except Exception as e:
        print("NLP Augmentation failed; returning original text.", e)
        return text

# ----------------------------
# Save to CSV Function
# ----------------------------
def save_to_csv(data, filename="user_input_data.csv"):
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(data)

# ----------------------------
# Main Function: Data Generation Pipeline
# ----------------------------
def main(num_samples=100):
    # Write header to CSV file
    header = ["user_input", "invest_style", "risk_pref", "time_horizon", "fin_situation", "sector_choice"]
    with open("user_input_data.csv", mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
    
    for _ in range(num_samples):
        # Generate base text and associated traits
        generated_text, invest_style, risk_pref, time_horizon, fin_situation, sector_choice = generate_user_input()
        # Optionally augment the text for variability, ensuring brevity
        final_text = augment_text(generated_text)
        # Save the final text along with traits
        save_to_csv([final_text, invest_style, risk_pref, time_horizon, fin_situation, sector_choice])
    
    print(f"Generated {num_samples} entries and saved to 'user_input_data.csv'.")

# ----------------------------
# Entry Point
# ----------------------------
if __name__ == "__main__":
    main(30000)
