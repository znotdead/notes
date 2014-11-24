Title: DB: Overview NoSQL
Date: 2012-03-22 14:52
Modified: 
Category: Programming
Tags: NoSQL,  Redis,  Mongo,  Riak,  CouchDB,  HBase,  Membase,  Cassandra,  Hypertable,  Kyoto
Slug: db_overview_nosql
Lang: en
Authors: znotdead
Summary: Overview NoSQL

### Overview NoSQL

I need to save smth. about 6 milliards of keys.
So MySQL will hang on IO.
we need more efficient.

**REQUIREMENTS**:
1. persistancce
2. fast
3. sharding
4. replication

**REDIS**:
redis 2.2.0
+ it has sets
+ convinient API
- all keys in memory
- on current versions (2.2.0) virtual memory SUCKS. Redis can eat all memory on your server because limits doesn't work. Wait for 2.4.0

**MONGO**:
MongoDB shell version: 1.8.0
+ sets
- you cant limit memory usage. It also eats all available memory and become swapping killing your server

+ fast loading because data saves in memory dumps
+ possible update sets and date in one request
- much memory usage 5 millions of data {"_id": ObjectId(id), 'date': int(time.time()), 'k':[1111,2222,33333,4444,5555,6666,77777]} # timestamp is unix time.

1000000:
+ 3 minutes to fill
-  0.5GB

1 000 000 entries ({"_id": ObjectId(id), 'date': int(time.time()), 'k':[1111,2222,33333,4444,5555,6666,77777]} )
 db.stats()
{
        "db" : "linksss",
        "collections" : 3,
        "objects" : 1000004,
        "avgObjSize" : 91.999836000656,
        "dataSize" : 92000204,
        "storageSize" : 121869056,
        "numExtents" : 16,
        "indexes" : 1,
        "indexSize" : 41598976,
        "fileSize" : 520093696,
        "ok" : 1
}

**RIAK**:
riak_0.14.0-1_i386.deb
+ use python as usual
- it takes too much time to fill 1000000 entries like in mongo.
- during script run console with python hangs
- too much disk space (on 650Mb I stopped script. this is not that thing that we want.)
- too much CPU on filling (practically all time 100%)

**COUCHDB**:
+ good synax (comparing to HBase)
- disk expensive
- slow write
- hard disk usage
- no read caches
data like {'date': int(time()), 'k': [144422, 22212, 323444, 66, 12345, 3456, 23444]}
db.info()
{'committed_update_seq': 15731,
 'compact_running': False,
 'db_name': 'test',
 'disk_format_version': 5,
 'disk_size': 85602402,
 'doc_count': 15731,
 'doc_del_count': 0,
 'instance_start_time': '1301644812061465',
 'purge_seq': 0,
 'update_seq': 15731}

**HBASE**:
hbase 0.90.1, r1070708
+ small disc usage
+ 2 billions entries in one table (by hbase spec)
- average CPU usage (50-70% on my U7300  @ 1.30GHz x2) ( most of all python)
- thrift with not beautiful syntax
- sometimes java exceptions with connection loose
1 million of entries takes:
- 248 Mb on HD
- 16 minutes for filling

> describe 'linkss'
DESCRIPTION                                                                                                   ENABLED
 {NAME => 'linkss', FAMILIES => [{NAME => 'date', BLOOMFILTER => 'NONE', REPLICATION_SCOPE => '0', COMPRESSIO true
 N => 'NONE', VERSIONS => '3', TTL => '-1', BLOCKSIZE => '65536', IN_MEMORY => 'false', BLOCKCACHE => 'false'
 }, {NAME => 'k', BLOOMFILTER => 'NONE', REPLICATION_SCOPE => '0', COMPRESSION => 'NONE', VERSIONS => '10', T
 TL => '-1', BLOCKSIZE => '65536', IN_MEMORY => 'false', BLOCKCACHE => 'false'}]}

**MEMBASE**:
membase-server  1.6.5.3
+ wonderful admin UI
+ fast enough as store info in memory and sync to disk
+ caching
+ it is possible to limit RAM usage for server or DB separately and it's works!
+ memcached clients
+ clustering from the box
- no manual config edit via files
- not so fast as mongo, bigger IO than mongo. but better for systems when loading pages critical
- all keys in memory ( may be many Gb)
- 120b additionally for each key
- sqlite3 as persistent storage

1 000 000 entries:
-6 minutes
+122Mb disk
163Mb memory

1 000 000 entries read (100% cache loose because of low limit of memory):
0:08:56.130380
+ low hdd usage
- CPU 70%

1 000 000 entries read in RANDOM(100% cache loose because of low limit of memory)
0:09:07.694571

**CASSANDRA**:
apache-cassandra-0.7.5
+ low hdd usage
- high hardware needs:
    not less than 8 (or16) Gb RAMfor dedicated server. 32Gb better per node.
    Cassandra is highly concurrent  - 8 cores preferred
    2 disks, one to keep your CommitLogDirectory on, the other to use in DataFileDirectories

1 000 000 entries:
-1:16:45.464607
-1.4Gb java process
-362M    /tmp/cass/commitlog
-825M    /tmp/cass/data
362M    /tmp/cass/commitlog
376M    /tmp/cass/data

insert user and history in one request
265M    /tmp/cass/commitlog
825M    /tmp/cass/data
0:24:59.894963

insert only history:
0:13:34.955025
136M    /tmp/cass/commitlog
336M    /tmp/cass/data

1 000 000 entries READ:
-0:32:25.457211
-40-50% CPU on read ( form than 54% java, 40% -python and 6 other system)
-for first time high hdd usage(11%) (first 50k) than practically no

1 000 000 entries RANDOM READ:
0:24:53.761907

5 000 000 entries with time after each 1m:
1m: 0:13:25.326189
2m: 0:27:07.851321 (0:13:42)
3m: 0:40:31.404977 (0:13:24)
4m: 0:54:26.248025 (0:13:55)
5m: 1:08:19.861676 (0:13:53)
166M    /tmp/cass/commitlog
1.5G    /tmp/cass/data

**HYPERTABLE**:
0.9.5.0.pre4 (hypertable)
- high HDD usage (on cluster may be it can be descreased by using HDFS)

**KYOTO**
+ very fast
- no sharding from the box ( there are LightCloud scripts for tokyo cabinet )

1 000 000:
0:00:09.599489
75M
5 000 000:
0:30:57.988294
350M
from 6 to 7 millions:
0:19:00.845744

We select Cassandra for future needs and it's good to many writes. But I think it will be enough Mongo.
