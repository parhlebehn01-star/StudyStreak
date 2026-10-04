import json
import os
from datetime import date, timedelta
from quotes import quotes
import random

DATA_FILE = "data.json"


def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        content = f.read().strip()
        if not content: 
            return {}
        return json.loads(content)
    
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)
            
            
   
def mark_day(status):
    data = load_data()
    data[date.today().isoformat()] = status
    save_data(data)
    return get_situation(data)
    
    
def get_streak(data):
    streak = 0
    check  = date.today()
    while True:
        key = check.isoformat()
        if data.get(key) == "studied":
             streak += 1
             check -= timedelta(days=1)
        else:
             break
    return streak
        
        
def missed_days_this_week(data):
    count = 0
    check = date.today()
    for _ in range(7):
        if data.get(check.isoformat()) == "missed":
            count +=1
        check -= timedelta(days=1)
    return count
            
            
def get_situation(data):
    yesterday = (date.today() - timedelta(days=1)).isoformat()
    streak = get_streak(data)
    missed_week = missed_days_this_week(data)
        
    if streak == 0 and data.get(yesterday) =="studied":
        return "streak_broken"
    if missed_week >= 3:
        return "tough_week"
    if data.get(yesterday) == "missed":
        return "returned"
    return "missed_once"
    
def get_quote(situation):
        return random.choice(quotes[situation]) 
        
                
        
    
    
    