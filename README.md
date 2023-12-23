Building a Scalable Data Warehouse for Traffic Analysis: A Weekly Challenge Report for 10 Academy


INTRODUCTION

     In response to the Weekly Challenge posed by 10 Academy Cohort A, I have undertaken the task of creating a robust and scalable data warehouse. The primary  objective of the task was : 
To analyze vehicle trajectory data obtained from swarm UAV(drones).

    The following comprehensive report, it will delve into the complex and intricate details of the approach, critical decisions made and the implementation of tech stack utilization such as Airflow and Redash.



TECH STACK OVERVIEW

Data warehouse( PostgreSQL): I have chosen PostgreSQL due to its proven robustness, scalability, and excellent performance for data, which is crucial for the analysis of the vehicle trajectories.

Orchestration Service(Airflow): Airflow serves as the backbone for managing the workflow task scheduling and orchestration. A dag ensures the seamless loading of data into the database and separates the Prod, Dev and Staging.

ELT tool (DBT):  I have implemented ELT technique on the raw data using dbt, empowering analytics to set up the workflows on demand. It also plays a huge role in the generation of documentation and the execution of transformations ensuring data consistency and reliability.

Reporting Environment(Redash) : Even Though the integration hasn’t been finished I have tried to use Redash as the intuitive reporting tool to make dashboards that are crafted to visualize traffic data.


