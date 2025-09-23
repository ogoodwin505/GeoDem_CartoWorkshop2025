# Setup 


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

This notebook contains the workflow for produceding a geodemographic classification in python using k-means clustering. It follows a process similar to that described in the 2021 OAC Paper [@2021_oac].


* **Data Access and Processing:**
    * Access UK census data and process using Pandas

* **Census Data Analysis and Variable selection:**
    * Perform correlation analysis to identify redundant variables
    * Use PCA (Principal Component Analysis) to reduce dimensionality and identify key components
    * Select variables based on explained variance and interpretability

* **Clustering:**
    * Apply K-Means clustering to classify areas based on selected variables
    * Determine optimal number of clusters using Clustergrams
    * Perform hierarchical clustering to group clusters into supergroups
    * Conduct subclustering within supergroups to identify finer patterns

* **Analytical Techniques:**
    * Use UMAP (Uniform Manifold Approximation and Projection) to visualise high-dimensional embeddings in 2D

* **Visualisation and Communication:**
    * Visualise clusters and subclusters using Kepler.gl for interactive mapping
    * Export results to various formats (GeoPackage, Parquet) for use in GIS software
    * Generate publication-ready plots and statistical summaries
