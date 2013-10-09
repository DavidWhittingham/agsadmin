========
agsadmin
========

agsadmin provides a convenient Python front-end to several REST calls on the ArcGIS Server 10.1+ REST Admin API.

Features
===============

Currently, agsadmin allows you to perform basic management functions for a map service. For a map service, it can:

- start and stop
- get statistics
- get status
- get or set the item info (description, summary, tags, etc.)
- set service properties

These functions can be used to automate management of ArcGIS Services (e.g. start/stop services on a schedule, 
start/stop services to perform maintenance on associated datasets, etc.)
