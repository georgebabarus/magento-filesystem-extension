.. role:: raw-html-m2r(raw)
   :format: html

Magento filesystem component extension
======================================

Magento 2.4 version almost has already in place filesystem abstraction needed to implement and integrate new filesystem for core or custom modules.

There are few touch points that are not abstracted enough as you could see in current documentation, and this storage extension covers this to allow Cloud object storage service integration into Magento 2.
In many cases existing Database files storage could not be useful and definitively is not a optimal implementation since it is doing a sync back to local filesystem on missing resource.

Read the `documentation <https://magento-filesystem-extension-docs.readthedocs.io>`_ to see some of the key advantages of using this Magento 2 extension to integrate with various cloud file storage services in a platform agnostic manner.

What is covered with this extensions?
---------------------------------------

* Decouple file storage system form compute systems and scale them independently.
  A driver will be basically a class implementing (Magento\Framework\Filesystem\DriverInterface) basic operations: read/write files or directory.

* Mapping of any media sub-directory to various filesystem services.

    For example you can make following mapping:

        * media/catalog files to a public AWS S3 bucket
        * media/downloadable could be mapped to a private AWS S3 bucket
        * media/captcha could be kept on disk filesystem


Currently there are 6 Magento modules developed to achieve fully abstracted filesystem implementation:

* Bb_Storage is the core module implementing most of business logic:

    * directories mapping
    * adding custom media directories for new modules
    * use the media storage system of your choice for any given directory or subdirectory
    * image resize in-place without sync back to local filesystem the file (this require having the same configuration for main directory and destination of resized files)
    * this module allows only new modules to use this features, none of Magento core functionality is touched

Bb_StorageOverwrite

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

    * implementation of Amazon S3 api as a Magento filesystem driver


Author
======

`George Babarus <https://github.com/georgebabarus>`_
