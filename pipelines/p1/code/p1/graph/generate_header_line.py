from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from p1.config.ConfigStore import *
from p1.functions import *

def generate_header_line(spark: SparkSession) -> DataFrame:
    header_line = f'"1"¬"BCDU_INTERFACE"¬"'
    ##trailer_line = f'"9"¬"{total_count}"'
    header_df = spark.createDataFrame([Row(line = header_line)])

    return out0
