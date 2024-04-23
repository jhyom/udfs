import fused
from fused.models.udf import Header
from fused.models import Schema

@fused.udf()
def gittest_udf():
    import geopandas as gpd
    from utils import geo_convert
    gdf = gpd.read_parquet('jhy_udf')
    return gdf