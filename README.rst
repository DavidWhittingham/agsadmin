========
agsadmin
========

agsadmin provides a convenient Python front-end to several REST calls on the ArcGIS Server 10.1+ REST Admin API.

Features
========

- Map/Geoprocessing Services

  - start and stop
  - get statistics
  - get status
  - get or set the item info (description, summary, tags, etc.)
  - set service properties
  
- Machines

  - start and stop

- System

  - Directories

    - list directories
    - register new directories
    - unregister directories
    - clean directories

These functions can be used to automate management of ArcGIS Services (e.g. start/stop services on a schedule, 
start/stop services to perform maintenance on associated datasets, etc.)

Example
=======
The following is a simplistic example to stop and start a map service.

.. code-block:: python

  import agsadmin

  hostname = "<ServerNameHere>"
  username = "<UsernameHere>"
  password = "<PasswordHere>"

  rest_admin = agsadmin.RestAdmin(hostname, username, password)
  service = rest_admin.get_service("<MapServiceNameHere>", "MapServer", "<OptionalFolderHere>")
  service.stop_service()
  service.start_service()
