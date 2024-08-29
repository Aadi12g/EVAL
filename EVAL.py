# EVAL Q1
import random
def generate(height,weight,preferred_sport):
    diet_plan={
        'Breakfast': 'fruits',
        'Lunch': ' vegetables',
        'Dinner': 'Pulses',
        'Snacks': 'Nuts and yoghurt'
    }
    if preferred_sport in ['cricket', 'football']:
        diet_plan['Lunch'] = 'rice and vegetables'
    elif preferred_sport == 'javelin throw':
        diet_plan['Breakfast'] = 'Protein shake'
    
    return diet_plan
def recommend(agility,speed,strength):
    sports={
        'cricket':{'agility': 6, 'speed': 5, 'strength': 7},
        'football':{'agility': 8, 'speed': 7, 'strength': 6},
        'chess':{'agility': 2, 'speed': 3, 'strength': 2},
        'javelin throw':{'agility': 4, 'speed': 5, 'strength': 9}
    }
    best_match = None
    best_score=30
    for sport,attributes in sports.items():
        score=(agility * attributes['agility'] +
                 speed * attributes['speed'] +
                 strength * attributes['strength'])
        if score>best_score:
            best_score=score
            best_match=sport
    
    return best_match
def manage():
    students={}
    students[1]={
        'name':'John Doe',
        'class':'10A',
        'height':175,  # in cm
        'weight':70,   # in kg
        'preferred_sport':'football',
        'agility':5,
        'speed':6,
        'strength':4
    }
    students[2] = {
        'name':'Jane Smith',
        'class':'10B',
        'height':160,
        'weight': 55,
        'preferred_sport':'javelin throw',
        'agility':8,
        'speed':5,
        'strength':9
    }
    for student_id,details in students.items():
        print(f"Student ID: {student_id}")
        print(f"Name: {details['name']}")
        print(f"Class: {details['class']}")
        print(f"Height: {details['height']} cm")
        print(f"Weight: {details['weight']} kg")
        print(f"Preferred Sport: {details['preferred_sport']}")
        diet_plan = generate(details['height'], details['weight'], details['preferred_sport'])
        print("Personalized Diet Plan:")
        for meal, food in diet_plan.items():
            print(f"{meal}:{food}")
        recommended_sport = recommend(details['agility'], details['speed'], details['strength'])
        print(f"Recommended Sport based on attributes: {recommended_sport}")
        
