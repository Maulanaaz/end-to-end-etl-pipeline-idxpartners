# 🐍 ETL Source Code & Modules

This directory contains the Python modules that orchestrate the **ETL (Extract, Transform, Load)** pipeline. The code is modularized to ensure maintainability and separation of concerns.

## 📂 Module Descriptions

Here is the breakdown of the python scripts and their specific roles in the pipeline:

### 1. Extraction & Staging
* **`extract.py`**:
  * Connects to heterogeneous data sources (CSV, Excel, Legacy SQL).
  * Reads raw data into Pandas DataFrames.
* **`staging.py`**:
  * Ingests the raw DataFrames into the **Staging Area** of the database.
  * *Note:* No transformation happens here; data is loaded "as-is" for audit trails.

### 2. Transformation & Loading
* **`transform.py`**:
  * Applies data cleaning (handling nulls, removing duplicates).
  * Enforces business logic and data type validation.
  * Prepares data for the Snowflake Schema structure.
* **`load.py`**:
  * Loads the clean data into the final Data Warehouse tables (**Dimension** & **Fact** tables).
  * Handles Insert/Update logic (Upsert).

### 3. Orchestration & Reporting
* **`reporting.py`**:
  * Contains helper functions to execute SQL Stored Procedures.
  * Fetches aggregated data for final reports.
* **`main_pipeline.py`** (ENTRY POINT):
  * The master script that runs all modules in the correct order.
  * **Run this file** to execute the full end-to-end pipeline.

---
