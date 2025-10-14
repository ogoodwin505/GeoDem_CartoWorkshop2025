# Creating Cutting-Edge Geodemographic Classifications from Scratch in Python

Resources for the workshop **“Creating Cutting-Edge Geodemographic Classifications from Scratch in Python”**, presented at the [Spatial Data Science Conference 2025](https://spatial-data-science-conference.com/2025/newyork).

📘 **Web tutorial:** [ogoodwin505.github.io/GeoDem_CartoWorkshop2025](https://ogoodwin505.github.io/GeoDem_CartoWorkshop2025/)  
💻 **Main Notebook:** [`creatinggeodem.ipynb`](creatinggeodem.ipynb)


### Data

The data used in this workshop is available from the Geographic Data Service [dataset](https://data.geods.ac.uk/dataset/creating-an-open-geodemographic-classification-using-k-means-clustering-in-python). You will need to register for a free account to download the data.
Download the `input_data_1.zip` file and place it in the same directory as this notebook. The notebook will unzip the data to a folder called `input_data`.

The notebook can be run in Google Colab or locally on your machine. Instructions for both options are provided below.

## Running the Notebook in Google Colab

You can run the notebook in Google Colab. This is a free cloud-based environment that allows you to run Jupyter notebooks without needing to install anything on your local machine. You will need a Google account to use Colab.

 [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ogoodwin505/GeoDem_CartoWorkshop2025/blob/main/creatinggeodem.ipynb)

You will need to upload the data to the Colab environment. To do this, you can use the file upload feature in Colab to upload the zipped folder input_data_1.zip to the same directory as the notebook. The data will be unzipped by code in the notebook.

You will also need to install the required packages in the Colab environment. You can do this by uncommenting and running the following code cell in the notebook:

```python
# !pip install pandas geopandas pyarrow scikit-learn clustergram umap-learn seaborn plotly matplotlib numpy keplergl openai
# from google.colab import output
# output.enable_custom_widget_manager()
```

## Running the Notebook Locally
To run this notebook locally you will need to have Python installed on your machine.

Clone and access the repository:

```bash
git clone https://github.com/ogoodwin505/GeoDem_CartoWorkshop2025.git
cd GeoDem_CartoWorkshop2025
```

There are a number of python packages that need to be installed to run this notebook. It is recommended to use a virtual environment to manage these dependencies.

```bash
python -m venv .venv
```
Activate the virtual environment:
```bash
# macOS / Linux
source .venv/bin/activate
```
```bash
# Windows (Command Prompt)
.venv\Scripts\activate.bat
```
```bash
# Windows (PowerShell)
 .\venv\Scripts\Activate.ps1
```

Install the required packages:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```



You can then start Jupyter Notebook or Jupyter Lab to run the notebook.

```bash
jupyter notebook creatinggeodem.ipynb
```
or
```bash
jupyter lab creatinggeodem.ipynb
```



# Workshop Content

This notebook contains the full workflow for producing a geodemographic classification from scratch in python using k-means clustering. 

The `creatinggeodem.ipynb` notebook contains the full code and explanatory text for the workshop.  
The key steps covered in the notebook are:

* **Data Access and Processing:**
    * Access UK Census data and process using Pandas.
    * Select a specific region of interest (e.g., Liverpool City Region, Greater Manchester, Greater London).

* **Census Data Analysis and Variable selection:**
    * Select relevant Census variables for clustering.
    * Standardise variables.
    * Perform correlation & variance analysis to identify potentially redundant variables.
    * Alternative variable selection methods (e.g., PCA, Autoencoders).

* **Clustering:**
    * Determine optimal number of clusters using Clustergrams.
    * Apply K-Means clustering to classify areas based on selected variables.
    * Perform top-down hierarchical clustering to divide clusters into subgroups.
    
* **Analytical Techniques:**
    * Use UMAP (Uniform Manifold Approximation and Projection) to visualise high-dimensional embeddings in 2D.

* **Visualisation and Communication:**
    * Visualise clusters and subclusters using Kepler.gl for interactive mapping.
    * Explore cluster characteristics using summary statistics and index scores.
    * Export results to various formats (GeoPackage, Parquet) for use in GIS software.
    
* **Cluster Naming with LLMs:**
    * Use Large Language Models (LLMs) to generate descriptive names and summaries for clusters based on their characteristics.
