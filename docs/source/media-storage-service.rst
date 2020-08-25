.. meta::
    :description lang=en:
        Magento 2 Madia Storage Service

.. meta::
    :keywords lang=en:
        Magento 2, file storage, service, cloud storage, microservice

Introduction
============

Magento Storage Service (M2SS) is a software as a service (SaaS) project providing file storage integration with cloud object storage services and CDN for Magento 2 stores.

Most often Magento media files are served from a content delivery network (CDN) to optimise loading time for this files and reducing network throughput rate on the compute servers.
In the given situation there is one open question: Should media files still reside on compute server's disk? (being regular disk or mounted block storage service). Now consider recent plans for `Magento 2 related headless implementation <https://magento.com/blog/best-practices/future-headless/>`_ and the answer may be clear.

This integration will allow shop owners to store media files in cloud storage service of the choice or using any given CDN, and in the same time reducing the complexity of the Magento 2 system by extracting media storage as a microservice.

This M2SS service is in charge of:
    * storing any type of media file (in block storage service of various cloud providers)
    * resizing images on demand or in background after upload
    * serve optimised resources using CDN

Magento project will use Magento Storage Extension to write media files directly to cloud storage service of choice by using the proper driver implemented or using a custom one.

As long as images are uploaded, no other requests are made to the storage service, the url is generated in Magento but the resource is only served from MSS.

Subscribe for news on this topic
--------------------------------

Subscribe for updates on this topic and information about release of the next Magento 2 Storage Service.

Soon we will come with a beta program and you may benefit of attractive enrolment discounts.

`Subscribe here <https://mailchi.mp/ef502f3af734/magento-storage-service/>`_



Architecture
============

Resized images could be delivered directly from storage system after creating the resized image in the main request or return a proxy url responsible to return the image if not exist.

The proxy can be implemented as follow:

* nginx config to request it from storage system and create a fallback request in case of error on Magento resize script
* in case you don't have access to a web server proxy configuration there is a option to return it directly from default Magento image resize script.

.. image:: extension/_static/architecture/frontend-image-delivery.png
  :alt: Upload image for product or CMS blocks
