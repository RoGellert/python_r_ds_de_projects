import os

if __name__ == '__main__':
    # I just tried different methods to change PATH =)
    os.environ["AIRFLOW_HOME"] = "D:/Projects/DS_projects/Airflow"
    print(os.environ["AIRFLOW_HOME"])
