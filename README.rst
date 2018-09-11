========
agsadmin
========

agsadmin provides a convenient Python front-end to several REST calls on the ArcGIS Server 10.1+ REST Admin API.

Features
========

ArcGIS Server (RestAdmin)
*************************

- Services (Map/Image/Geoprocessing/Geometry/Geocode/GeoData/Globe/Search)

  - start and stop
  - get statistics
  - get status
  - get or set the item info (description, summary, tags, etc.)
  - set service properties
  - rename services
  
- Machines

  - start and stop

- System

  - Directories

    - list directories
    - register new directories
    - unregister directories
    - clean directories

- Uploads

  - list uploads
  - get a specific upload item
  - upload a file

These functions can be used to automate management of ArcGIS Services (e.g. start/stop services on a schedule, 
start/stop services to perform maintenance on associated datasets, etc.)

ArcGIS Portal (SharingAdmin)
****************************

- Content

  - get item
  - get user item

Example
=======
The following is a simplistic example to stop and start a map service.

.. code-block:: python

  import agsadmin

  hostname = "<ServerNameHere>"
  username = "<UsernameHere>"
  password = "<PasswordHere>"

  rest_admin = agsadmin.RestAdmin(hostname, username, password)
  service = rest_admin.services.get_service("<MapServiceNameHere>", "MapServer", "<OptionalFolderHere>")
  service.stop_service()
  service.start_service()
  service.delete()
