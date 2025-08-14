sleep(5000);
//add shard1 to cluster
sh.addShard("shard1/shard1a:27018,shard1b:27020,shard1c:27021");

//ad shard2 to cluster
sh.addShard("shard2/shard2a:27018,shard2b:27020,shard2c:27021");

//enable sharding on database
sh.enableSharding("invdb");

//shard collections
sh.shardCollection("invdb.variants", { variant_id: 1, day: 1, _id: 1 });
sh.shardCollection("invdb.reservations", { variant_id: 1, day: 1, _id: 1 });

//show status
sh.status();