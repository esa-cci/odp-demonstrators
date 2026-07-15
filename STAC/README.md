# CCI STAC Index - Staging Version

The CCI STAC Index is currently under construction. The API service hosted on Open Telekom Cloud is considered to be a staging version and should be treated as such. Feedback is appreciated and can be made either directly to the ESA Climate Office or by making an issue in this repository.

See the `STACTour_v1.0.pdf` document for guidance on how to view the API service via a STAC browser application hosted by radiant-earth.

We have also provided some basic notebooks to start testing the CCI STAC index.

**Important Information:**
- The collections are arranged with a nested structure that follows CCI -> Project -> CEDA Catalogue Record -> Data Reference Syntax (DRS / Dataset ID)
- The CCI top-level collections contains no STAC items - you will need to navigate to a specific DRS-level dataset to then use a client tool (e.g pystac) to search for items.
- Items that represent non-NetCDF/GeoTiff data include 'dummy' values for spatio-temporal information. Please be aware of this when attempting to interrogate item-collections.
