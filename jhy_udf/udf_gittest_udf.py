import fused
from fused.models.udf import Header
from fused.models import Schema

@fused.udf()
def gittest_udf():
    import geopandas as gpd
    from utils import geo_convert
    gdf = gpd.read_parquet('s3://data-wiroba-com/ov_korea.geoparquet')
    return gdf