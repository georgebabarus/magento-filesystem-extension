.. role:: raw-html-m2r(raw)
   :format: html

Magento filesystem component extension
======================================

Introduction
------------

Magento 2.4 version almost has already in place filesystem abstraction needed to implement and integrate new filesystem (eg: remote filesystems like Amazon Simple Storage Service - S3) for core or custom modules.

There are few touch points that are not abstracted enough as you could see in current documentation, and this storage extensions covers this, to allow cloud object storage service integration into Magento 2.

In many cases existing Database files storage could not be useful and definitively is not a optimal implementation since it is doing a sync back to local filesystem on missing resource.

The scope of this extensions is to extract static files storage as microservice for Magento platform, decoupling files storage system from compute system.

Read the `documentation <https://docs.magento.asset42.com>`_ to see some of the key advantages of using this Magento 2 extensions to integrate with various cloud file storage services in a platform agnostic manner.

What is covered with this extensions?
---------------------------------------

* Decouple file storage system form compute systems and scale them independently.

      Install all Bb_Storage, Bb_StorageOverwrites, Bb_StorageCms, Bb_StorageCatalog, Bb_StorageDownloadable modules.

      Install one of the filesystem driver module eg: Bb_StorageS3.

      A driver will be basically a class implementing basic operations read/write on files or directories. (see: Magento\Framework\Filesystem\DriverInterface)

      Configure directory mapping to save and serve files directly from storage service.

* Mapping of any media sub-directory to various filesystem services.

    For example you can make following mapping:

        * media/catalog files to a public AWS S3 bucket
        * media/downloadable could be mapped to a private AWS S3 bucket
        * media/captcha could be kept on disk filesystem


Currently there are 6 Magento modules developed to achieve fully abstracted filesystem implementation:

* Bb_Storage is the core module implementing most of business logic:

    * directories mapping
    * adding custom media directories for new modules (eg: you want to store some reports in Azure Blob storage, you can configure a new directory for this report)
    * use the media storage system of your choice for any given directory or subdirectory
    * image resize in-place without sync back to local filesystem the file (this require having the same configuration for main directory and destination of resized files)
    * :term:`OOB` this module can be used in custom modules, none of Magento core features are touched
    * allow new directory configuration for custom development

Bb_StorageOverwrites

    * allow Bb_Storage features on built-in media directories

Bb_StorageCms

    * configure Magento_Cms module to use Bb_Storage
    * fix some week parts on Magento core components that are not using driver object to execute basic actions on files

Bb_StorageCatalog

    * configure Magento_Catalog module to use Bb_Storage
    * fix some week parts on Magento core components that are not using driver object to execute basic actions on files

Bb_StorageDownloadable

    * Allow downloadable files to be saved in a different non-public media storage
    * fix some week parts on Magento core components that are not using driver object to execute basic actions on files

Bb_StorageS3

    * implementation of Amazon S3 like api as a Magento filesystem driver


Author
------

`George Babarus <https://github.com/georgebabarus>`_
