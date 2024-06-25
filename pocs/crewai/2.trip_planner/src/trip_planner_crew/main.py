import os
from dotenv import load_dotenv
load_dotenv()

from trip_planner_crew.crew import TripPlannerCrew

def run():
    inputs = {
        # 'company_name': os.getenv('COMPANY_NAME'),
        # 'company_name': 'Tesla',
        'origin': "Brasilia",
        'cities': "Rio de janeiro",
        'range': "2025-01-01 a 2025-02-01",
        'interests': "Praias e passeios",
    }
    crew = TripPlannerCrew().crew()
    results = crew.kickoff(inputs=inputs)
    print("results:")
    print(results)
    
if __name__ == '__main__':
    run()