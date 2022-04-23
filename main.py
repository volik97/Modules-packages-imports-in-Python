from Application.salary import calculate_salary
from Application.Database.people import get_employes
from datetime import datetime

if __name__ == '__main__':
    print(datetime.today())
    calculate_salary()
    get_employes()