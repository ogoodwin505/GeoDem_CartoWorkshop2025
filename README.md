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
