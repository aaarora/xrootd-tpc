Cloned from BichyRichy/bug-free-funicular

MaDDash and Measurement Archive container
-----
### Maddash Architecture
The Maddash setup consists of two main components, the Maddash webserver and the esmond archive software. The webserver hosts the graphical Maddash webpage as well as tools for scheduling and graphing tests, while the esmond archive receives and stores test data. Currently the Maddash webserver and the esmond archive run in separate Docker containers, which can be built from within the [esmondImage](https://github.com/BichyRichy/bug-free-funicular/tree/master/esmondImage) and [MaddashImage](https://github.com/BichyRichy/bug-free-funicular/tree/master/MaddashImage) folders.

### Running the Containers
```docker run -ti -v /sys/fs/cgroup:/sys/fs/cgroup:ro -v /tmp/$(mktemp -d):/run -p {port}:80  --detach --name {name} {image}```
Open port 8080 for Maddash and port 8090 for esmond.

### Maddash Mesh Config
The mesh configuration for the Maddash webserver can be defined in ```/etc/maddash/maddash-server/maddash.yaml```. 
Note: this can also be done with [pSConfig tool](https://docs.perfsonar.net/psconfig_maddash_agent.html).
* *groups:* defines the hosts in the mesh.
* *checks:* the tests to display results for.
    * *maUrl:* URL of esmond measurement archive.
    ```http://{esmondAddress}/esmond/perfsonar/archive```
    * *graphUrl:* URL of Perfsonar toolkit graph.
    ```http://{toolkitAddress}/perfsonar-graphs/?url=%maUrl&dest=%col&source=%row```
    * *command*: full command to run.
    ```/usr/lib64/nagios/plugins/{check} -u %maUrl -w .1: -c .01: -r 86400 -s %row -d %col```

### esmond Authentication
To create a new user for publishing data, run the following commands in the esmond container:
```/usr/sbin/esmond_manage add_ps_metadata_post_user example_user```
```/usr/sbin/esmond_manage add_timeseries_post_user example_user```
The API key will be displayed in the terminal output. 

### Publishing Data
Perfsonar has a Python library for esmond that can be installed with ```pip install esmond-client```. See [pushData](https://github.com/BichyRichy/bug-free-funicular/blob/master/MaddashImage/esmondAPI/pushData.py) for example code of publishing data to the archive in Python.
### Notes:
* Need to add [HTTPS encryption](https://httpd.apache.org/docs/2.4/ssl/ssl_howto.html) for the esmond API key.
* The first time the esmond container is run, the ```esmond``` package needs to be un/reinstalled to run correctly.
* esmond uses the Cassandra service to archive data. ```su cassandra``` during boot would crash the service, so ```su``` settings need to be changed.
* Python does not recognize the ```esmond.api.client.perfsonar.query``` library. Fix by moving the needed .py files where you need them.
