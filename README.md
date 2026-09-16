# Remote Sensing
## Google Earth Engine + Visual Studio Code + Geemap
<img width="1920" height="1080" alt="Screenshot 2025-09-24 at 3 08 07 PM" src="https://github.com/user-attachments/assets/e8173ae3-ca32-47ef-97cc-4380222afb2f" />  
:warning: **Warning:** You will need:  
- prepare an environment:  
`  
  python3 -m venv venv-geemap  
  pip3 install wheel  
  pip3 install ipykernel geemap ipyleaflet==0.16 # Not working with latest ipyleaflet  
  python3 -m ipykernel install --user --name=venv-geemap
`  
  
And Install  
* Geemap  
  https://geemap.org/
* ipyleaflet  
  https://github.com/jupyter-widgets/ipyleaflet

Optional:  
  A visual Studio code extension:  
  - https://marketplace.visualstudio.com/items?itemName=gee-community.eetasks
  - ipywidgets , in a nutshel, widgets for Jupyter(optional for now):  
  https://github.com/jupyter-widgets/ipywidgets

** __Troubleshooting__ **  
Make this notebook trusted to load map : File -> Trust Notebook  
This is a general problem, try changing your default browser to Chrome or Firefox — it should work perfectly!

## Pull AlphaEarth embeddings over a KML region

A convenience script was added at `scripts/pull_alphaearth_embeddings.py`.

Usage example:

`
python scripts/pull_alphaearth_embeddings.py \
  --kml BlackHills.kml \
  --asset "users/YOUR_USER/alpha_embeddings" \
  --out out/blackhills_embeddings.geojson
`

Notes:
- Install dependencies: `pip install -r requirements.txt`.
- Authenticate Earth Engine: `earthengine authenticate`.
- The script samples the specified Earth Engine Image asset over the KML polygon and writes a GeoJSON-like FeatureCollection dict locally. For large regions, prefer using the `--export_drive` flag to export via Earth Engine Tasks to Drive.
- `--scale` controls the sampling resolution in meters (default 30 m).
