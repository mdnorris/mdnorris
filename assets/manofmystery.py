class InternationalManOfMystery:
    def __init__(self, name, alma_mater, primary_skills):
        self.name = name
        self.alma_mater = alma_mater
        self.primary_skills = primary_skills
        self.mysterious = True
        self.origin = "Unknown"
        
    def describe(self):
        description = (
            f"{self.name} graduated from {self.alma_mater}, though little is known of his years there.\n"
            "He moves through cities with a passport that raises questions, and speaks just enough\n"
            "of every language to slip into any conversation undetected. The only certainty is his \n"
            "discerning taste and a sharp intellect."
        )
        return description
    
    def perform_task(self, task):
        print(f"{self.name} executes '{task}' with effortless precision and discretion.")
        if task.lower() in self.primary_skills:
            print(f"Indeed, {self.name} has mastered '{task}' — the mark of a true professional.")
        else:
            print(f"No one expected {self.name} to be skilled in '{task}', but no one should be surprised.")

# Create a character profile for Matt Norris, Sorbonne graduate and international man of mystery
matt_norris = InternationalManOfMystery(
    name="Matt Norris",
    alma_mater="Sorbonne",
    primary_skills=["intelligence gathering", "geospatial analysis", "linguistics"]
)

# Let's get to know the mysterious Mr. Norris
print(matt_norris.describe())
matt_norris.perform_task("intelligence gathering")
