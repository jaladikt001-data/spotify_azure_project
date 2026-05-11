# spotify_azure_project

Spotify End-to-End Data Engineering Project (Azure + Databricks)
Overview

This project demonstrates an end-to-end data engineering pipeline built on Microsoft Azure and Databricks using Spotify data. The goal is to design a scalable, production-style data pipeline covering ingestion, storage, transformation, and analytics using modern data engineering best practices.
Architecture

The project follows a modern cloud data engineering architecture:

    Azure Data Factory (ADF) – data ingestion and orchestration
    Azure Data Lake Storage Gen2 (ADLS) – raw, processed, and curated data storage , Centralized data storage
    Azure Databricks – Distributed data processing using PySpark
    Bronze / Silver / Gold layered architecture – For reliability and scalability

Data Flow

    Spotify data is ingested using Azure Data Factory
    Raw data is stored in ADLS Gen2 (Bronze layer)
    Data is incrementally cleaned and transformed using PySpark in Databricks (Silver layer)
    Analytics-ready dimensional data is created in the Gold layer using Slowly Changing Dimension Type 2 (SCD Type 2)

Incremental Loading Strategy

    The pipeline is designed using incremental data loading instead of full reloads.

    New records are identified using ingestion timestamps / load dates

    Only newly arrived data is processed in the Bronze layer

    Incremental transformations are applied in Silver layer

    Upserts and historical tracking are handled in the Gold layer using SCD Type 2
    Benifits:
        Reduced processing time
        Lower compute cost
        Preserves full history of changes
        Scales efficiently as data volume grows

Technologies Used

    Azure Data Factory
    Azure Data Lake Storage Gen2
    Azure Databricks
    PySpark
    Python
    GitHub

Key Features

    End-to-end Azure-Databricks-based data pipeline
    Incremental data processing
    Layered data architecture (Bronze, Silver, Gold)
    Slowly Changing Dimension (SCD Type 2) implementation in Gold layer
    Modular and readable PySpark transformations
    Cloud-scalable design aligned with real-world practices

Learning Outcomes

    Practical experience with Azure data services
    Practical implementation of incremental loading
    Improved understanding of real-world data pipeline design
    Hands-on Databricks and PySpark development
    Understanding of real-world data pipeline design
    Improved data modeling and transformation skills

Future Improvements

    Add data quality validation checks
    Enhance watermark-based incremental logic
    Optimize SCD Type 2 merge performance
    Add monitoring and alerting
    Integrate BI tools for visualization
