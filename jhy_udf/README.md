
# Fused Multi-Step Job

## Get started
```python
# Import UDFs
from udf_gittest_udf import gittest_udf

# Instantiate individual jobs
job_gittest_udf = gittest_udf()

# Instantiate multi-step job
job = fused.experimental.job([job_gittest_udf])

# Run locally
job.run_local(file_id=0, chunk_id=0)

# Run remotely
job.run_remote(output_table='output_table_name')
```
