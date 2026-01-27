from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from p3.config.ConfigStore import *
from p3.functions import *

def seed(spark: SparkSession) -> DataFrame:
    schemaFields = StructType([StructField("id", StringType(), True)]).fields
    readSchema = StructType([StructField(f.name, StringType(), True) for f in schemaFields])

    return spark.createDataFrame([Row("1"), Row("2"), Row("3"), Row("4")], readSchema)
