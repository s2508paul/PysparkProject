from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from p1.config.ConfigStore import *
from p1.functions import *
from prophecy.utils import *
from p1.graph import *

def pipeline(spark: SparkSession) -> None:
    df_create_people_dataframe = create_people_dataframe(spark)
    df_generate_header_line = generate_header_line(spark)
    df_union_all_dfs = union_all_dfs(spark, df_generate_header_line, df_create_people_dataframe)

def main():
    spark = SparkSession.builder.enableHiveSupport().appName("p1").getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/p1")
    spark.conf.set("spark.default.parallelism", "4")
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/p1", config = Config)(pipeline)

if __name__ == "__main__":
    main()
