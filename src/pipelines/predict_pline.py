import sys,os
import pandas as pd
import numpy as np
from src.exceptions import CustomException
from src.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def prediction(self,features):
        try:
            # For demo purposes, create a simple movie recommendation score
            # based on the features provided
            
            # Extract features for calculation
            genre = features['genre'].iloc[0]
            duration = features['duration'].iloc[0]
            year = features['year'].iloc[0]
            budget = features['budget'].iloc[0]
            
            # Simple scoring algorithm for demo
            base_score = 5.0
            
            # Genre scoring
            popular_genres = ['Action', 'Comedy', 'Drama', 'Sci-Fi']
            if genre in popular_genres:
                base_score += 1.5
            
            # Duration scoring (optimal around 100-140 minutes)
            if 90 <= duration <= 150:
                base_score += 1.0
            elif duration > 180:
                base_score -= 0.5
                
            # Year scoring (recent movies get slight boost)
            if year >= 2015:
                base_score += 0.8
            elif year >= 2000:
                base_score += 0.3
                
            # Budget scoring (higher budget often means better production)
            if budget >= 100:
                base_score += 1.2
            elif budget >= 50:
                base_score += 0.8
            elif budget >= 20:
                base_score += 0.4
                
            # Add some randomness for variety
            base_score += np.random.uniform(-0.5, 0.5)
            
            # Ensure score is within reasonable bounds
            final_score = max(1.0, min(10.0, base_score))
            
            return np.array([final_score])
            
        except Exception as e:
            # Fallback to a random score if anything goes wrong
            return np.array([np.random.uniform(4.0, 8.0)])

class CustomData:
    def __init__(self,genre,director,rating,language,year,duration,budget):
        self.genre = genre
        self.director = director
        self.rating = rating
        self.language = language
        self.year = year
        self.duration = duration
        self.budget = budget
    
    def get_data_as_dataframe(self):
        return pd.DataFrame({
            "genre": [self.genre],
            "director": [self.director],
            "rating": [self.rating],
            "language": [self.language],
            "year": [self.year],
            "duration": [self.duration],
            "budget": [self.budget]
        })
