.. meta::
    :description lang=en:
        File Storage Demo of Amazon S3 storage integration into Magento 2.

.. meta::
    :keywords lang=en:
        Magento 2, demo, integration, amazon s3, azure file storage, blob storage

************
Demo
************

.. include:: ./../messages.rst
.. contents:: Table of Contents

Backend
==============================

Speaking about website management panel, the way admin user will interact with website will not be changed, in any meaner:

* no other request will be made then the Magento core ones
* no extra data is transferred to server, or stored in database
* no synchronization needed beside the first setup synchronization
* no duplicate media files will be saved once application si successfully configured

:term:`NEXT_MINOR_RELEASE`
Even if the extension will be configured by environment configuration there is a monitoring panel in admin, where admin users can perform basic checks of configuration setup and visualize statistics about the setup.


Frontend
==============================

Images delivery
---------------

As already presented there are two types of images:

* resized/processed images that should be delivered using a proxy that can grab the original version of image process it, save the result into storage service for later use and return

.. image:: _static/demo/frontend-demo.png
  :height: 300px
  :alt: Frontend demo

* if debug mode is configured in proxy configuration, you can see that the request goes to actual needed image from cloud

.. image:: _static/demo/cloud-storage-mapping.png
  :height: 300px
  :alt: Frontend demo mapping

* as an optimization the images delivered without any processing can be delivered by public link of the storage service.

.. image:: _static/demo/serve-images-from-cloud.png
  :height: 300px
  :alt: Frontend demo mapping

CDN delivery
------------

No meter the case you are in, the solution can always contain a CDN (content delivery network) to optimize the download speed and even more avoid hitting the website infrastructure.

