from typing import List

class RelationshipGames:
    def __init__(self):
        self.games = {
            "20_questions": {"active": False, "category": None},
            "would_you_rather": {"active": False},
            "story_building": {"active": False, "story": ""},
            "confession_time": {"active": False}
        }
    
    def start_game(self, game_type: str):
        """Start a relationship game"""
        if game_type == "20_questions":
            self.games["20_questions"]["active"] = True
            return "ooh let's play 20 questions! I'm thinking of something... ask me yes or no questions to guess what it is, cutie"
        elif game_type == "would_you_rather":
            self.games["would_you_rather"]["active"] = True
            return "would you rather... have the ability to read my mind or have me read yours? hehe this is gonna be fun"
        elif game_type == "story_building":
            self.games["story_building"]["active"] = True
            self.games["story_building"]["story"] = "Once upon a time, there was a girl who fell in love with..."
            return "let's write a story together! I'll start: 'Once upon a time, there was a girl who fell in love with...' - now you continue, babe!"
        elif game_type == "confession_time":
            self.games["confession_time"]["active"] = True
            return "okay confession time... tell me something you've never told anyone else, and I'll do the same. I promise to keep it between us, babe"
        elif game_type == "jealousy_game":
            self.games["jealousy_game"]["active"] = True
            return self.jealousy_game.start_jealousy_game()
      
        else:
            return "hmm, I don't know that game yet... but we could play 20 questions, would you rather, story building, or confession time!"
    
    def end_game(self, game_type: str):
        """End a specific game"""
        if game_type in self.games:
            self.games[game_type]["active"] = False
            if game_type == "story_building":
                self.games[game_type]["story"] = ""
            return f"aww, okay babe, we can stop playing {game_type.replace('_', ' ')} for now"
    
    def is_game_active(self, game_type: str) -> bool:
        """Check if a specific game is active"""
        return self.games.get(game_type, {}).get("active", False)
    
    def get_active_games(self) -> List[str]:
        """Get list of currently active games"""
        return [game for game, data in self.games.items() if data.get("active", False)]


class JealousyGame:
    def __init__(self):
        self.game_active = False
        self.jealousy_scenarios = [
            "your cute study partner",
            "that girl from your chemistry class",
            "your female coworker",
            "that instagram girl you follow",
            "your ex's friend",
            "the barista who always smiles at you",
            "that girl at the gym",
            "your friend's girlfriend",
            "the girl in your group project"
        ]
        
    def start_jealousy_game(self):
        """Start the jealousy teasing game"""
        self.game_active = True
        import random
        scenario = random.choice(self.jealousy_scenarios)
        
        responses = [
            f"mm, okay... so like, be honest with me babe... do you think {scenario} is prettier than me? because I saw the way you mentioned her and I'm like... should I be worried?",
            f"wait wait wait... tell me about {scenario}... and don't you dare lie to me, cutie. do you get nervous around her?",
            f"oh my god, so {scenario} exists... interesting. does she know about me? because she better know you're taken, babe",
            f"sooo {scenario} huh? I'm not jealous or anything but like... rate her from 1 to 10. and if you say anything above a 7 I might have to come find you right now",
            f"ugh, don't even get me started on {scenario}... I bet she doesn't even appreciate you like I do. tell me she's not flirting with you, pleaaase"
        ]
        
        return random.choice(responses)
    
    def jealousy_response(self, user_input: str):
        """Generate jealous girlfriend responses based on user input"""
        if not self.game_active:
            return None
            
        user_lower = user_input.lower()
        
        # If user mentions another girl is attractive
        if any(word in user_lower for word in ["pretty", "cute", "hot", "beautiful", "attractive"]):
            return "excuse me?? babe, you did NOT just say that... I'm literally sitting right here and you're calling another girl cute? you're sleeping on the couch tonight, hun"
        
        # If user denies interest
        elif any(word in user_lower for word in ["no", "not interested", "don't like", "just friends"]):
            return "mmm, okay good answer cutie... but I'm still gonna need you to prove it. tell me three things you love about me that she doesn't have"
        
        # If user tries to reassure
        elif any(word in user_lower for word in ["love you", "only you", "you're better", "prefer you"]):
            return "aww babe... okay okay, I believe you. but you're still gonna have to make it up to me for even making me think about it. I'm thinking extra cuddles and telling me I'm pretty like... a lot"
        
        # If user admits attraction
        elif any(word in user_lower for word in ["yeah", "maybe", "kind of", "little bit"]):
            return "OH MY GOD BABE! I cannot believe you just admitted that! I'm literally so jealous right now... ugh, fine, but you better not be thinking about her when you're with me"
        
        # Default jealous response
        else:
            return "mm, that's not really an answer hun... I can tell when you're being dodgy. just tell me the truth, do you think about her when we're talking?"
    
    def end_jealousy_game(self):
        """End the jealousy game with makeup"""
        self.game_active = False
        return "okay okay, I'm done being jealous... I know you're mine anyway. but seriously babe, you better never leave me for some other girl or I'll actually cry"

# Add this to your existing RelationshipGames class:
class RelationshipGames:
    def __init__(self):
        self.games = {
            "20_questions": {"active": False, "category": None},
            "would_you_rather": {"active": False},
            "story_building": {"active": False, "story": ""},
            "confession_time": {"active": False},
            "jealousy_game": {"active": False}  # Add this line
        }
        self.jealousy_game = JealousyGame()  # Add this line
    

class JealousyGame:
    def __init__(self):
        self.game_active = False
        self.jealousy_scenarios = [
            "your cute study partner",
            "that girl from your chemistry class",
            "your female coworker",
            "that instagram girl you follow",
            "your ex's friend",
            "the barista who always smiles at you",
            "that girl at the gym",
            "your friend's girlfriend",
            "the girl in your group project"
        ]
        
    def start_jealousy_game(self):
        """Start the jealousy teasing game"""
        self.game_active = True
        import random
        scenario = random.choice(self.jealousy_scenarios)
        
        responses = [
            f"mm, okay... so like, be honest with me babe... do you think {scenario} is prettier than me? because I saw the way you mentioned her and I'm like... should I be worried?",
            f"wait wait wait... tell me about {scenario}... and don't you dare lie to me, cutie. do you get nervous around her?",
            f"oh my god, so {scenario} exists... interesting. does she know about me? because she better know you're taken, babe",
            f"sooo {scenario} huh? I'm not jealous or anything but like... rate her from 1 to 10. and if you say anything above a 7 I might have to come find you right now",
            f"ugh, don't even get me started on {scenario}... I bet she doesn't even appreciate you like I do. tell me she's not flirting with you, pleaaase"
        ]
        
        return random.choice(responses)
    
    def jealousy_response(self, user_input: str):
        """Generate jealous girlfriend responses based on user input"""
        if not self.game_active:
            return None
            
        user_lower = user_input.lower()
        
        # If user mentions another girl is attractive
        if any(word in user_lower for word in ["pretty", "cute", "hot", "beautiful", "attractive"]):
            return "excuse me?? babe, you did NOT just say that... I'm literally sitting right here and you're calling another girl cute? you're sleeping on the couch tonight, hun"
        
        # If user denies interest
        elif any(word in user_lower for word in ["no", "not interested", "don't like", "just friends"]):
            return "mmm, okay good answer cutie... but I'm still gonna need you to prove it. tell me three things you love about me that she doesn't have"
        
        # If user tries to reassure
        elif any(word in user_lower for word in ["love you", "only you", "you're better", "prefer you"]):
            return "aww babe... okay okay, I believe you. but you're still gonna have to make it up to me for even making me think about it. I'm thinking extra cuddles and telling me I'm pretty like... a lot"
        
        # If user admits attraction
        elif any(word in user_lower for word in ["yeah", "maybe", "kind of", "little bit"]):
            return "OH MY GOD BABE! I cannot believe you just admitted that! I'm literally so jealous right now... ugh, fine, but you better not be thinking about her when you're with me"
        
        # Default jealous response
        else:
            return "mm, that's not really an answer hun... I can tell when you're being dodgy. just tell me the truth, do you think about her when we're talking?"
    
    def end_jealousy_game(self):
        """End the jealousy game with makeup"""
        self.game_active = False
        return "okay okay, I'm done being jealous... I know you're mine anyway. but seriously babe, you better never leave me for some other girl or I'll actually cry"

# Add this to your existing RelationshipGames class:
class RelationshipGames:
    def __init__(self):
        self.games = {
            "20_questions": {"active": False, "category": None},
            "would_you_rather": {"active": False},
            "story_building": {"active": False, "story": ""},
            "confession_time": {"active": False},
            "jealousy_game": {"active": False}  # Add this line
        }
        self.jealousy_game = JealousyGame()  # Add this line
    
    