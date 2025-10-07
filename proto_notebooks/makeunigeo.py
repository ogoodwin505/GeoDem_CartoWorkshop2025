
import pandas as pd
import geopandas as gpd
import numpy as np
#---------
# Import spatial data
#---------

# Output Areas (Dec 2021) Boundaries Full Clipped EW (BFC) - E&W
# Manually downloaded file, same as in R

OA_2021_Boundary_EW = gpd.read_file("original_inputs/boundaries/Output_Areas_2021_EW_BGC_V2_-5587136561181621407.gpkg")
OA_2021_Boundary_EW = OA_2021_Boundary_EW.rename(columns={"OA21CD": "OA"})[["OA", "geometry"]]

# Output Areas 2022 Scotland (GeoJSON via Google Drive link)
OA_2022_Boundary_S = gpd.read_file("original_inputs/boundaries/Scotland_OA_22.gpkg")
OA_2022_Boundary_S = OA_2022_Boundary_S.rename(columns={"code": "OA"})[["OA", "geometry"]]

OA_2021_Boundary_NI = gpd.read_file("original_inputs/boundaries/DZ2021.geojson")
OA_2021_Boundary_NI = OA_2021_Boundary_NI.rename(columns={"DZ2021_cd": "OA"})[["OA", "geometry"]]

#---------
# Combine OA and calculate area
#---------

# Reproject to British National Grid (EPSG:27700)
OA_2021_Boundary_EW = OA_2021_Boundary_EW.to_crs(27700)
OA_2022_Boundary_S = OA_2022_Boundary_S.to_crs(27700)
OA_2021_Boundary_NI = OA_2021_Boundary_NI.to_crs(27700)


# Merge
OA_Boundaries = gpd.GeoDataFrame(
    pd.concat([OA_2021_Boundary_EW, OA_2022_Boundary_S, OA_2021_Boundary_NI], ignore_index=True),
    crs="EPSG:27700"
)

# set index to OA code
OA_Boundaries = OA_Boundaries.set_index("OA")
#---------
# Save UK OA file
#---------
OA_Boundaries.to_file("input_data/OA_2021_22_Boundaries.gpkg", driver="GPKG")
#save as geojson too
# OA_Boundaries.to_file("input_data/OA_2021_22_Boundaries.geojson", driver="GeoJSON")
# #and parquet
# OA_Boundaries.to_parquet("input_data/OA_2021_22_Boundaries.parquet")