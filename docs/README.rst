.. role:: raw-html-m2r(raw)
   :format: html

Introduction
============

Magento 2.4 version has already in place the filesystem abstraction needed to implement and integrate new filesystems (e.g.: external file systems like Amazon Simple Storage Service - S3) for Magento's core modules or custom modules.

There are few touchpoints not abstracted enough, as you could see in the current documentation, but this extension covers this subject to allow cloud object storage service integration into Magento 2.

In many cases, existing "Database files storage" could not be useful and definitively is not an optimal implementation since it is doing sync back to the local filesystem on missing resources.

The ultimate scope of these extensions is to extract static files storage as a microservice for the Magento 2 platform, decoupling files storage system of the computing system, at the same time providing more flexibility in web asset compression, processing, and delivery.

Read the `documentation <https://docs.magento.asset42.com>`_ to find some of the key advantages of using these Magento 2 extensions to integrate with various cloud file storage services in a platform-agnostic manner.

What is covered with these extensions?
--------------------------------------

* Decouple file storage system of compute component and scale them independently.

      * Install all Bb_Storage, Bb_StorageOverwrites, Bb_StorageCms, Bb_StorageCatalog, Bb_StorageDownloadable modules.

      * Install one of the filesystem driver module eg: Bb_StorageS3.

        A filesystem driver is a class implementing basic operations (read, write, move, etc.) on files or directories. (see: \\Magento\\Framework\\Filesystem\\DriverInterface)

      * Configure directory mapping to save and serve files directly from storage service.

* Mapping for any media sub-directory to various filesystem services.

    For example you can make the following mapping:

        * media/catalog files to a public AWS S3 bucket
        * media/downloadable could be mapped to a private AWS S3 bucket
        * media/captcha could be kept on disk filesystem


Currently, there are 6 modules developed for Magento 2 to achieve fully abstracted filesystem implementation:

.. important::

    All extensions are available on `Magento Marketplace <https://marketplace.magento.com/>`_.

    `Read more about what you should purchase and install for your scenario <https://docs.magento.asset42.com/en/latest/extension/installation.html>`_

* ``Bb_Storage`` is the core module, implementing most of the business logic:

    * directories mapping
    * configure new remote media directories for new modules (e.g.: you want to store some reports in Azure Blob storage, you can configure a new directory for this report)
    * use the media storage system of your choice for any given directory or subdirectory
    * image resize in-place without sync back to local filesystem (this require having the same configuration for the main directory and the destination of resized files)
    * :term:`OOB` this module can be used in custom modules, none of Magento core features are touched

``Bb_StorageOverwrites``

    * allows Bb_Storage features on built-in media directories

``Bb_StorageCms``

    * configure Magento_Cms module to use Bb_Storage
    * fix some weak points on Magento core components that are not using driver object to execute basic actions on files

``Bb_StorageCatalog``

    * configure Magento_Catalog module to use Bb_Storage
    * fix some weak points on Magento core components that are not using driver object to execute basic actions on files

``Bb_StorageDownloadable``

    * Allow downloadable files to be saved in a different non-public media storage
    * fix some weak points on Magento core components that are not using driver object to execute basic actions on files

``Bb_StorageS3``

    * implementation of Amazon S3 like API as a Magento filesystem driver


Author
------

`George Babarus <https://github.com/georgebabarus>`_
