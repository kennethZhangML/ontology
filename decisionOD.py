import random

class OptimizationTaskSimulation:
    def __init__(self):
        self.reviewer_paper_affinities = {
            'Reviewer1': ['Paper1', 'Paper2', 'Paper3'],
            'Reviewer2': ['Paper2', 'Paper4'],
            'Reviewer3': ['Paper1', 'Paper3', 'Paper5'],
            'Reviewer4': ['Paper2', 'Paper5']
        }

    def simulate(self):
        print("Optimization Task Simulation:")
        print("-----------------------------")
        
        papers = ['Paper1', 'Paper2', 'Paper3', 'Paper4', 'Paper5']
        reviewers = ['Reviewer1', 'Reviewer2', 'Reviewer3', 'Reviewer4']
        
        random.shuffle(papers)
        
        for paper in papers:
            reviewer = random.choice(reviewers)
            
            if paper in self.reviewer_paper_affinities[reviewer]:
                print(f"Assigned {paper} to {reviewer}")
            else:
                print(f"No suitable reviewer found for {paper}")

class PlanningTaskSimulation:
    def __init__(self):
        self.preferences = {
            'Museum': ['Morning', 'Afternoon'],
            'Park': ['Afternoon', 'Evening'],
            'Restaurant': ['Evening']
        }

    def simulate(self):
        print("Planning Task Simulation:")
        print("-------------------------")

        places = ['Museum', 'Park', 'Restaurant']
        random.shuffle(places)

        for place in places:
            preferences = self.preferences[place]
            time_slot = random.choice(preferences)
            print(f"Scheduled {place} for {time_slot}")

class MediationTaskSimulation:
    def __init__(self):
        self.users = ['User1', 'User2', 'User3', 'User4']
        self.assistant = 'Assistant'

    def simulate(self):
        print("Mediation Task Simulation:")
        print("--------------------------")

        available_time_slots = ['Morning', 'Afternoon', 'Evening']
        random.shuffle(available_time_slots)

        for user in self.users:
            time_slot = random.choice(available_time_slots)
            print(f"{user} can meet in the {time_slot}")
        
if __name__ == "__main__":

    simulation = OptimizationTaskSimulation()
    simulation.simulate()

    simulation = PlanningTaskSimulation()
    simulation.simulate()

    simulation = MediationTaskSimulation()
    simulation.simulate()
