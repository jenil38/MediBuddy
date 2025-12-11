def get_diagnosis(symptoms, severities):
    rules = {
        ('cough', 'cold'): (
            'Common Cold',
            ['Tab. Cetrizine 10mg (once at night)', 'Tab. Paracetamol 500mg (if fever)', 'Steam inhalation']
        ),
        ('cold', 'sneeze'): (
            'Allergic Rhinitis',
            ['Tab. Levocetirizine 5mg', 'Nasal saline spray', 'Avoid dust/allergens']
        ),
        ('fever', 'body pain'): (
            'Viral Fever',
            ['Tab. Dolo 650 (3x daily)', 'ORS', 'Rest and fluids']
        ),
        ('fever', 'headache'): (
            'Viral Infection',
            ['Tab. Paracetamol 650mg', 'ORS solution', 'Tab. Azee (if prescribed)']
        ),
        ('headache',): (
            'Tension Headache',
            ['Tab. Crocin 500mg', 'Drink plenty of water', 'Rest in dark room']
        ),
        ('sore throat',): (
            'Throat Infection',
            ['Tab. Azithromycin 500mg (once daily for 3 days)', 'Warm saline gargle', 'Tab. Strepsils lozenges']
        ),
        ('chest pain', 'cough'): (
            'Bronchitis',
            ['Syrup Benadryl (10ml 3x/day)', 'Tab. Dolo 650 (if fever)', 'Steam inhalation twice daily']
        ),
        ('fever', 'rash'): (
            'Dengue (Possible)',
            ['Tab. Paracetamol (NO aspirin)', 'Drink plenty of fluids', 'Consult a doctor immediately']
        ),
        ('vomiting', 'diarrhea'): (
            'Food Poisoning',
            ['Tab. Ondem (for vomiting)', 'Tab. Eldoper (for loose motions)', 'ORS solution every 2 hrs']
        ),
        ('abdominal pain', 'vomiting'): (
            'Stomach Infection',
            ['Tab. Cyclopam', 'Tab. Pantop 40 (before meals)', 'Hydration with Electral']
        ),
        ('high fever', 'chills'): (
            'Malaria (Possible)',
            ['Tab. Lumerax (if confirmed)', 'Tab. Paracetamol', 'Consult doctor for blood test']
        ),
        ('joint pain', 'fever'): (
            'Chikungunya',
            ['Tab. Dolo 650', 'Tab. Aceclo-SP (if pain severe)', 'Hydration & rest']
        ),
        ('burning urine', 'abdominal pain'): (
            'Urinary Tract Infection (UTI)',
            ['Tab. Norflox-TZ (twice daily)', 'Cranberry syrup', 'Tab. Drotin for pain']
        ),
        ('eye pain', 'fever'): (
            'Conjunctivitis',
            ['Eye drops Moxifloxacin', 'Tab. Paracetamol', 'Avoid touching eyes']
        ),
        ('fatigue', 'fever', 'muscle pain'): (
            'Flu (Influenza)',
            ['Tab. Tamiflu (if prescribed)', 'Dolo 650', 'Warm fluids and rest']
        ),
        ('dry cough', 'loss of taste'): (
            'COVID-19 (Possible)',
            ['Tab. Dolo 650', 'Zincovit Multivitamin', 'Isolate & consult nearby clinic']
        ),
        ('toothache',): (
            'Tooth Infection',
            ['Tab. Zerodol-P', 'Tab. Amoxicillin 500mg (if swelling)', 'Visit dentist']
        ),
        ('back pain', 'leg pain'): (
            'Sciatica',
            ['Tab. Etoshine 90', 'Hot water compression', 'Physiotherapy advice']
        ),
        ('acidity', 'chest burn'): (
            'Acidity',
            ['Tab. Pan 40 (before breakfast)', 'Tab. Gelusil (after meals)', 'Avoid spicy foods']
        )
    }

    input_symptoms = [s.strip().lower() for s in symptoms]
    matched_diagnoses = []

    for rule_symptoms, (illness, medicines) in rules.items():
        if all(symptom in input_symptoms for symptom in rule_symptoms):
            matched_diagnoses.append((illness, medicines))

    if not matched_diagnoses:
        return [("Unknown Illness", ["Please consult a doctor."])]

    return matched_diagnoses
