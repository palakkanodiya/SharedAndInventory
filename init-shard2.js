rs.initiate({
  _id: "shard2",
  members: [
    { _id: 0, host: "shard2a:27018" },
    { _id: 1, host: "shard2b:27020" },
    { _id: 2, host: "shard2c:27021" }
  ]
});