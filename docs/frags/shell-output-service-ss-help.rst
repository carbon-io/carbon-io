% node <path-to-your-app>/MyService start-server --help
Usage: node MyService start-server [options]

Options:
   -v VERBOSITY, --verbosity VERBOSITY   verbosity level (trace | debug | info | warn | error | fatal)
   -p PORT, --port PORT                  port
   -n HOSTNAME, --hostname HOSTNAME      the hostname to bind  [0.0.0.0]
   -d DB_URI, --dbUri DB_URI             MongoDB connection string
   --cluster                             use node cluster
   --num-cluster-workers NUM             fork NUM cluster nodes (default is to fork a worker for each CPU)  [0]
   --exit-on-cluster-worker-exit         if this flag is set, the master will exit if a work dies, otherwise a warning will be logged
   --swagger                             mount swagger endpoints

start the api server

