# Python for Algorithms, Data-Structures, and Interviews!

## Welcome to the repository for the Udemy Course: Python for Algorithms, Data Structures, and Interviews!

This is the ultimate course in preparing you for your technical interviews and landing the job of your dreams!

Get the entire course, including full video content, solution walkthroughs, discussion forums, instructor support, and much more for only $20 by using the [discount link](https://www.udemy.com/python-for-data-structures-algorithms-and-interviews/?couponCode=github_discount)!

---

## Using Docker to run class notebooks and exercises

![image](https://github.com/kevinknights29/Airflow_Docs_LLM_App/assets/74464814/339aa9d3-32f9-404e-b449-4b493d015d74)

![image](https://github.com/kevinknights29/Airflow_Docs_LLM_App/assets/74464814/ef50ac23-b023-4b8b-bde8-d2775c240cc9)

In this repo you can find a series of Docker files:

- A [Dockerfile](./Dockerfile), which builds a jupyter lab container with all class materials.
- A [docker-compose.yml](./docker-compose.yml), which simplifies the build, start and stopage of the jupyterlab environment.
- A [.dockerignore](./.dockerignore), which exclude files from getting into the container.

### Usage

1. For first time usage, you need to build the Docker image:

```bash
docker compose build .
```

2. After that you can start the container with:

```bash
docker compose up -d
```

3. Go to Docker desktop, to retrieve your jupyterlab access URL.

    - Click the container name, to open the logs.
    - Retrive the jupyterlab URL, it should look like: `http://127.0.0.1:8888/lab?token=4150032f3603c85febf54b8b40bb761a2eb46e2fb593d5dc`

![image](https://github.com/kevinknights29/Airflow_Docs_LLM_App/assets/74464814/661f3747-2b2e-4387-9c79-64af1d8bc56e)

4. To stop the container, run:

```bash
docker compose down
```
