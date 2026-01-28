from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from p1.config.ConfigStore import *
from p1.functions import *

def create_people_dataframe(spark: SparkSession) -> DataFrame:
    from pyspark.sql import SparkSession
    spark = SparkSession.builder.getOrCreate()
    data = [
(1, "Alice", 28), (2, "Bob", 30), (3, "Charlie", 25), (4, "David", 35), (5, "Eva", 29)]
    columns = ["id", "name", "age"]
    df = spark.createDataFrame(data, columns)
    out0 = df

    return out0
