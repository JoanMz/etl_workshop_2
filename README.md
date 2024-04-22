<h1 align=center>📊 DataFlow Spotify 📊</h1>

![joanmz_spotify_c286256b-e32e-42ee-ae35-c56ad377fa0e](https://github.com/JoanMz/etl_workshop_2/assets/103477035/5155c297-2ce3-480e-aecb-aa95c57acea0)

#### Description

This project aims to create a data pipeline that integrates data from two different sources: CSV files and a SQL database containing information about Grammy-nominated songs, as well as data retrieved from the Spotify API. The objective is to identify and analyze the provided data to merge them effectively, thereby generating a more valuable analysis by complementing the data. The challenge also involves establishing an ETL (Extract, Transform, Load) process using Airflow. Through this process, we orchestrate the ETL tasks to clean and merge the data, subsequently storing it in both a database and Google Drive via its API as a CSV file.

#### Requirements

##### Technologies Used

- Python
- Airflow
- Google Drive API

##### Optional Tools

- Docker
- Windows Subsystem for Linux (WSL)
- Power BI (for dashboard presentation and analytics)

#### Installation

Follow these steps to set up the project:

1. **Install and Verify WSL**:
   - [WSL Installation Guide](https://docs.microsoft.com/en-us/learn/modules/get-started-with-windows-subsystem-for-linux/)

2. **Install Required Programs**:
   - Install Python 3 (minimum version 3.9)
   - Install Docker: [Docker Engine Installation Guide](https://docs.docker.com/engine/install/ubuntu/)
   - Set the AIRFLOW_HOME environment variable: 
     ```
     echo export AIRFLOW_HOME=$(pwd) >> ~/.bashrc
     ```
   - Install Airflow via pip: [Airflow Installation Guide](https://airflow.apache.org/docs/apache-airflow/stable/installation.html)

3. **Download Docker Image for the Database**:
   - Pull the PostgreSQL image: 
     ```
     docker pull postgres:16.2-alpine3.19
     ```

4. **Create Password Files and Virtual Environment**:
   - Create the necessary password files (`.env`, `docker-secrets`)
   - Create a virtual environment: 
     ```
     python3 -m venv venv
     ```
5. **Instal python requirements**:
   ```
   pip install -r requirements.txt
   ```
#### Project Structure

The project directory structure is as follows:

- **Dags**: Contains Airflow DAG files.
- **Data**: Directory for reading and storing CSV files.
- **DB_Connection**: Contains functionalities for managing the database.
- **Drive**: Contains functionalities for managing the Google Drive API.
- **Notebooks**: Used for data exploration and analysis, defining the requirements for DAGs.
- **postgres-db-volume**: Volume used by Docker.

#### Docker Compose Configuration

```yaml
services:
  postgresdb:
    image: postgres:16.2-alpine3.19
    volumes:
      - postgres-db-volume:/var/lib/postgresql/data
    env_file:
      - ./docker-secrets
    ports:
      - 54321:5432

volumes:
  postgres-db-volume:.

```
#### How to Run the Project

Follow these steps to run the project:

1. Start the Docker container: 
sudo docker-compose up
2. Enter the container and create the database (e.g., workshop_2):
```bash
sudo docker exec -it etl_workshop_2-postgresdb-1 /bin/bash
psql -U postgres
```
