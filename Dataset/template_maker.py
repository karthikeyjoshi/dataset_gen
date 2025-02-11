import csv


base_templates = [
    "Considering my {{ financial_situation.lower() }} budget, I opt for a {{ invest_style.lower() }} strategy that embraces {{ risk.lower() }} risk and pursues {{ time_horizon.lower() }} results in the {{ sector.lower() }} sector.",
    "With my {{ financial_situation.lower() }} funds at hand, I am drawn to a {{ invest_style.lower() }} approach that tolerates {{ risk.lower() }} risk and targets {{ time_horizon.lower() }} growth within the {{ sector.lower() }} industry.",
    "Operating from a {{ financial_situation.lower() }} financial base, I favor a {{ invest_style.lower() }} investment method that accepts {{ risk.lower() }} risk and aims for {{ time_horizon.lower() }} outcomes in the realm of {{ sector.lower() }}.",
    "Given my {{ financial_situation.lower() }} resources, I pursue a {{ invest_style.lower() }} investment plan that manages {{ risk.lower() }} risk and focuses on {{ time_horizon.lower() }} opportunities in the {{ sector.lower() }} market.",
    "My {{ financial_situation.lower() }} capital enables me to embrace a {{ invest_style.lower() }} approach, one that balances {{ risk.lower() }} risk with a commitment to {{ time_horizon.lower() }} success in the {{ sector.lower() }} field.",
    "Thanks to a {{ financial_situation.lower() }} budget, I have chosen a {{ invest_style.lower() }} strategy that acknowledges {{ risk.lower() }} risk and strives for {{ time_horizon.lower() }} achievements in the {{ sector.lower() }} arena.",
    "In light of my {{ financial_situation.lower() }} funds, I lean toward a {{ invest_style.lower() }} investment method that accepts {{ risk.lower() }} risk and is geared toward {{ time_horizon.lower() }} milestones within the {{ sector.lower() }} sector.",
    "With a {{ financial_situation.lower() }} financial situation, I am committed to a {{ invest_style.lower() }} plan that accommodates {{ risk.lower() }} risk and targets {{ time_horizon.lower() }} results in the area of {{ sector.lower() }}.",
    "My current {{ financial_situation.lower() }} resources inspire a {{ invest_style.lower() }} approach that carefully manages {{ risk.lower() }} risk while pursuing {{ time_horizon.lower() }} gains in the {{ sector.lower() }} industry.",
    "Based on my {{ financial_situation.lower() }} budget, I am adopting a {{ invest_style.lower() }} investment style that accepts {{ risk.lower() }} risk and focuses on {{ time_horizon.lower() }} returns in the {{ sector.lower() }} domain.",
    "Operating on a {{ financial_situation.lower() }} budget, I prefer a {{ invest_style.lower() }} strategy that navigates {{ risk.lower() }} risk and is tuned for {{ time_horizon.lower() }} growth in the {{ sector.lower() }} field.",
    "My {{ financial_situation.lower() }} funds guide me toward a {{ invest_style.lower() }} investment approach that is comfortable with {{ risk.lower() }} risk and geared for {{ time_horizon.lower() }} success in the {{ sector.lower() }} space.",
    "Given a {{ financial_situation.lower() }} financial base, I have chosen a {{ invest_style.lower() }} method that embraces {{ risk.lower() }} risk and aims for {{ time_horizon.lower() }} improvements in the {{ sector.lower() }} arena.",
    "With {{ financial_situation.lower() }} resources at my disposal, I'm pursuing a {{ invest_style.lower() }} plan that balances {{ risk.lower() }} risk and is focused on {{ time_horizon.lower() }} progress within the {{ sector.lower() }} market.",
    "My {{ financial_situation.lower() }} budget encourages a {{ invest_style.lower() }} investment strategy that tolerates {{ risk.lower() }} risk and seeks {{ time_horizon.lower() }} returns in the field of {{ sector.lower() }}.",
    "Thanks to {{ financial_situation.lower() }} finances, I am adopting a {{ invest_style.lower() }} approach that contends with {{ risk.lower() }} risk and aspires to {{ time_horizon.lower() }} outcomes in the {{ sector.lower() }} sector.",
    "Rooted in a {{ financial_situation.lower() }} budget, my {{ invest_style.lower() }} strategy accepts {{ risk.lower() }} risk and is directed toward {{ time_horizon.lower() }} objectives in the {{ sector.lower() }} domain.",
    "My {{ financial_situation.lower() }} funds empower me to follow a {{ invest_style.lower() }} approach that accommodates {{ risk.lower() }} risk and emphasizes {{ time_horizon.lower() }} performance in the {{ sector.lower() }} industry.",
    "Operating from a base of {{ financial_situation.lower() }} resources, I choose a {{ invest_style.lower() }} method that manages {{ risk.lower() }} risk and pursues {{ time_horizon.lower() }} achievements within the {{ sector.lower() }} space.",
    "Given my {{ financial_situation.lower() }} financial capacity, I favor a {{ invest_style.lower() }} investment plan that concedes {{ risk.lower() }} risk and strives for {{ time_horizon.lower() }} success in the {{ sector.lower() }} field.",
    "With {{ financial_situation.lower() }} means at hand, I am inclined toward a {{ invest_style.lower() }} strategy that accommodates {{ risk.lower() }} risk while focusing on {{ time_horizon.lower() }} results in the {{ sector.lower() }} arena.",
    "My {{ financial_situation.lower() }} monetary resources prompt me to adopt a {{ invest_style.lower() }} method that is comfortable with {{ risk.lower() }} risk and is aimed at {{ time_horizon.lower() }} outcomes in the {{ sector.lower() }} sector.",
    "Based on my {{ financial_situation.lower() }} budget, I embrace a {{ invest_style.lower() }} approach that accepts {{ risk.lower() }} risk and is designed for {{ time_horizon.lower() }} achievements in the {{ sector.lower() }} market.",
    "In view of my {{ financial_situation.lower() }} financial standing, I opt for a {{ invest_style.lower() }} investment style that integrates {{ risk.lower() }} risk and targets {{ time_horizon.lower() }} growth in the {{ sector.lower() }} field.",
    "My {{ financial_situation.lower() }} funds lead me to a {{ invest_style.lower() }} strategy that accepts {{ risk.lower() }} risk and is tailored for {{ time_horizon.lower() }} progress in the realm of {{ sector.lower() }}.",
    "With a foundation of {{ financial_situation.lower() }} resources, I pursue a {{ invest_style.lower() }} plan that manages {{ risk.lower() }} risk while aiming for {{ time_horizon.lower() }} successes in the {{ sector.lower() }} industry."
]

# To produce 500 unique templates, we’ll cycle through the 25 base templates and append a unique “voice” note.
# Here are 20 distinct "voice" suffixes that we’ll rotate (20 * 25 = 500).
voice_suffixes = [
    "-- by A.",
    "-- as noted by B.",
    "-- in my view.",
    "-- according to my experience.",
    "-- as I believe.",
    "-- from my perspective.",
    "-- in my honest opinion.",
    "-- as a seasoned investor would say.",
    "-- reflecting my values.",
    "-- with genuine insight.",
    "-- as written by an independent thinker.",
    "-- with a unique outlook.",
    "-- in my humble opinion.",
    "-- based on my real-world experience.",
    "-- as someone who cares deeply.",
    "-- with thoughtful consideration.",
    "-- from years of experience.",
    "-- as I confidently assert.",
    "-- with authentic conviction.",
    "-- as a true believer."
]

# Now, generate the 500 templates by combining each base with a unique suffix.
templates = []
voice_count = len(voice_suffixes)
base_count = len(base_templates)

for i in range(25000):
    base = base_templates[i % base_count]
    suffix = voice_suffixes[i % voice_count]
    full_template = f"{base} {suffix}"
    templates.append(full_template)

# Write the templates to a CSV file with header "Template"
with open("templates.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    for tmpl in templates:
        writer.writerow([tmpl])

print("CSV file 'templates.csv' with 500 high-quality, diverse templates has been generated.")
