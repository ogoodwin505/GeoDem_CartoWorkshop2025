# Creating Cutting-Edge Geodemographic Classifications from Scratch in Python


## Setup 


There are a number of python packages that need to be installed to run this notebook. It is recommended to use a virtual environment to manage these dependencies.

```bash
python -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows (PowerShell)
.venv/Scripts/Activate.ps1

pip install --upgrade pip
pip install pandas geopandas pyarrow scikit-learn clustergram umap-learn seaborn plotly matplotlib numpy keplergl
```

# Workshop Content

This notebook contains the full workflow for producing a geodemographic classification from scratch in python using k-means clustering. 

* **Data Access and Processing:**
    * Access UK census data and process using Pandas.
    * Select a specific region of interest (e.g., Liverpool City Region, Greater Manchester, Greater London).

* **Census Data Analysis and Variable selection:**
    * Select relevant census variables for clustering.
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