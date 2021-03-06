# Configuratins related to Cassandra connector & Cluster
import os
os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages com.datastax.spark:spark-cassandra-connector_2.11:2.3.0 --conf spark.cassandra.connection.host=127.0.0.1 pyspark-shell'

from pyspark import SparkContext
sc = SparkContext("local", "students app")

from pyspark.sql import SparkSession


spark = SparkSession.builder.appName("Classification with Spark").getOrCreate()


from pyspark.sql import SQLContext
sqlContext = SQLContext(sc)

def load_and_get_table_df(keys_space_name, table_name):
    table_df = sqlContext.read\
        .format("org.apache.spark.sql.cassandra")\
        .options(table=table_name, keyspace=keys_space_name)\
        .load()
    return table_df

trans = load_and_get_table_df("transactions_db", "transactions1")
print(trans.show())
print(trans.count())
def load_and_get_table_df1(keys_space_name, table_name):
    table_df1 = sqlContext.read\
        .format("org.apache.spark.sql.cassandra")\
        .options(table=table_name, keyspace=keys_space_name)\
        .load()
    return table_df1

trans1 = load_and_get_table_df1("transactions_db", "customers")
print(trans1.show())


print(trans1.count())






