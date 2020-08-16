.. meta::
    :description lang=en:
        Basic and advance setup of cloud storage services for Magento for media files.

.. meta::
    :keywords lang=en:
        file storage service, cloud, integration, setup, configuration, magento

************
Introduction
************

.. include:: ../README.rst

Latest releases
===============

.. note::

    This extension is currently under development.


Use cases
=========

On premises deployment with cloud file storage and CDN in cloud
---------------------------------------------------------------

Even if this is not the lucky case this module could be used for this use-case, but some latency problems may occur on admin panel.

Store media files using remote cloud services, process images on application server.

.. image:: _static/on-premises-deployment.png
  :alt: On premises deployment

.. note::
    Optimization could be achieved if resize script could be moved in same data-center with media storage service.

Migration to cloud from on premises infrastructure
--------------------------------------------------

In migration stage this module could be used as a mean to migrate media files to cloud storage service.

.. image:: _static/migration-to-cloud.png
  :alt: Migration to cloud

Already using cloud other services
----------------------------------

.. note::
    All notes above apply to this case, and the advantage of having the storage system and computing ones in same data-center will assure best performance and const-effective setup.


Features
========

Product file storage
--------------------

This includes product photo gallery, product description images, or other product related photos will be stored at upload time in cloud and delivered from there each time is needed in frontend.

Downloadable products attachments will be available in future release.

.. image:: _static/features/product-gallery.png
  :height: 300px
  :alt: Product file storage for gallery

Nothing change in database architecture and the way Magento save path to product images.

.. image:: _static/features/catalog-product-images-in-database.png
  :height: 300px
  :alt: Database representation of product gallery

WYSIWYG images storage
----------------------

This mainly store images in cloud, and serve them directly from there without needs for resizing.

:term:`WOOB` See image bellow, to prove nothing change in the way content is saved. Url is still saved as relative path to media directory.


.. image:: _static/features/wysiwyg-standard-features.png
  :height: 300px
  :alt: WYSIWYG images storage

Photo upload and management in admin
------------------------------------

The extension implements cloud storage folders navigation for admin user in order to allow user to locate directly on cloud needed images and insert into HTML without needs to be on applications servers.

.. image:: _static/features/wysiwyg-navigation.png
  :height: 300px
  :alt: Photo upload and management in admin

Sync corn between filesystems
------------------------------

For migration projects there is a command to synchronize media files from on filesystem to another.


.. code-block:: shell

    bin/magento bb:storage:sync

    Description:
      Sync media files between two filesystems on a particular directory.

    Usage:
      bb:storage:sync [options] [--] <source> <destination> [<directory>]

    Arguments:
      source                Origin filesystem code
      destination           Destination filesystem code
      directory             Directory to be synchronized.

    Options:
      -o, --overwrite       Overwrite files in destination


.. image:: _static/features/sync-images.png
  :height: 300px
  :alt: Sync images between filesystem

Difference report between filesystems
-------------------------------------

Also for later use there is a developer command to report the differences between two filesystems in order to re-evaluate migration process.


.. code-block:: shell

    bin/magento bb:storage:diff files s3 media

    Description:
      Create a report with differences between different two filesystems on a particular directory.

    Usage:
      bb:storage:diff <filesystem_1> <filesystem_2> <directory>

    Arguments:
      filesystem_1          First filesystem code
      filesystem_2          Second filesystem code
      directory             Directory to be compared


Multiple cloud buckets mapping for each main directory
------------------------------------------------------

Having multiple cloud objects buckets mapped to different media level directories allow website to expose files with different level of permission for frontend. For example for downloadable products, files should be served only through application server.

