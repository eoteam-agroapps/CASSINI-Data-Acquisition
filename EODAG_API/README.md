# Earth Observation Data Access Gateway for Data Acquisition


## Build EODAG API Docker Container


` cd /path/to/EODAG_API/Docker`


`docker build --rm -f "Dockerfile_EODAG.txt"  -t eodag:1.0 "."`

## Define an Area of Interest for Spatial Querry

##### WKT : AOI Geometry to Well Known Text format

> POLYGON ((23.06967923532928921 40.72624629927305762, 23.1397368419440248 40.72624629927305762, 23.1397368419440248 40.6608559586090621, 23.06967923532928921 40.6608559586090621, 23.06967923532928921 40.72624629927305762))

## Credentials file
Modify the .env file with your corresponding login credentials (username and password) of the defined providers (CreoDIAS, Copernicus Dataspace Ecosystem ONDA DIAS). The .env file should be placed in the same folder as the EODAG_Generic.py script.

## Create Workspace : A Folder, relative to repo to store the downloaded products

`cd /path/to/repo/folder/EODAG_API/`

`mkdir PRODUCTS`

## Input Args

The user will get prompted to provide the following inputs:

**Workspace directory**: The desired workspace directory where the products will be saved

**Product Types** separated by commas: Product types as they are listed here https://eodag.readthedocs.io/en/stable/_static/product_types_information.csv. 

E.g. S2_MSI_L2A

**Extent**: The WKT string in the format Polygon (())

**Start Date**: Start Date in YYYY-MM-DD format
**End Date**: End Date in YYYY-MM-DD format

## Data Products

**S1_SAR_GRD** : Sentinel 1 SAR L1 GRD
**S2_MSI_L1C** : Sentinel 2 Multispectral L1
**S2_MSI_L2A** : Sentinel 2 Multispectral L2


## Create Subfolders for each data product

`cd /path/to/repo/folder/EODAG_API/PRODUCTS`

`mkdir S1_SAR_GRD S2_MSI_L1C S2_MSI_L2A LANDSAT_C2L2`

## EODAG API Docker Container run

```shell
docker run -v <absolute/path/of/the/local/file/system/directory/to/be/mounted>:/eo-tools-eodag -it eodag:1.0
```

`docker run -v /path/to/repo/folder/EODAG_API/:/eo-tools-eodag -it eodag:1.0`

## Script execution

python3 <scriptName> --workspace "path/to/workspace/directory" --extent "WKT String" --start_date "YYYY-MM-DD" --end_date "YYYY-MM-DD"


------------


## Examples

 
------------

 **S2_MSI_L1C**
 
```python
 python3 EODAG_Generic.py --workspace "/eo-tools-eodag/PRODUCTS/S2_MSI_L1C" --product_types "S2_MSI_L1C" --extent "POLYGON ((23.06967923532928921 40.72624629927305762, 23.1397368419440248 40.72624629927305762, 23.1397368419440248 40.6608559586090621, 23.06967923532928921 40.6608559586090621, 23.06967923532928921 40.72624629927305762))" --start_date "2024-08-15" --end_date "2024-09-02" 
```

------------


------------
**S2_MSI_L2A**

```python
python3 EODAG_Generic.py --workspace "/eo-tools-eodag/PRODUCTS/S2_MSI_L2A" --product_types "S2_MSI_L2A" --extent "POLYGON ((23.06967923532928921 40.72624629927305762, 23.1397368419440248 40.72624629927305762, 23.1397368419440248 40.6608559586090621, 23.06967923532928921 40.6608559586090621, 23.06967923532928921 40.72624629927305762))" --start_date "2024-08-15" --end_date "2024-09-02" 
```


------------


------------

**S1_SAR_GRD**

```python
python3 EODAG_Generic.py --workspace "/eo-tools-eodag/PRODUCTS/S1_SAR_GRD" --product_types "S1_SAR_GRD" --extent "POLYGON ((23.06967923532928921 40.72624629927305762, 23.1397368419440248 40.72624629927305762, 23.1397368419440248 40.6608559586090621, 23.06967923532928921 40.6608559586090621, 23.06967923532928921 40.72624629927305762))" --start_date "2024-08-15" --end_date "2024-09-02"
```

 #######  ASCENDING/DECSENDING ?? 


------------

