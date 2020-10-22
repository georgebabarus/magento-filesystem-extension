.. meta::
    :description lang=en:
        Getting started with cloud file storage service integration for Magento 2

.. meta::
    :keywords lang=en:
        file storage service, cloud, integration

****************
Getting Started
****************

Before starting and purchasing extensions please read carefully the documentation to see if these extensions cover your needs.

.. contents:: Table of Contents

Each extension is available in Magento Marketplace individually.

    * So if you would like to integrate one external filesystem of your choice into a custom feature developed by your team you should buy the base extension |ShopBb_StorageMarketplace| and the needed filesystem driver eg: |ShopBb_StorageS3Marketplace|

    * If you would like to create a mapping of some of Magento Core directories to an external filesystem service you will need to buy both main extension |ShopBb_StorageMarketplace| and a driver of your choice but also this extension |ShopBb_StorageOverwritesMarketplace|

    .. warning::

        |ShopBb_StorageOverwritesMarketplace| is currently on the alpha phase so it will possibly affect some of Magento core features or 3rd party modules.


        The following modules Bb_StorageCms Bb_StorageCatalog and Bb_StorageDownloadable are shared packages for |ShopBb_StorageOverwritesMarketplace| and are offered for free. Those modules consist of code fixes in Magento Core modules where Filesystem drivers are not used accordingly, by using the Filesystem object.

        .. important::

            There is a further plan to integrate all Magento Community improvements into the core codebase.
            By purchasing this extension will move forward this project and plan for achieving better filesystem abstraction in Magento 2 platform.

Software dependencies
=====================

Bellow you will find both the extension commercial name and the module name (in parentheses), short description of the extension and the dependencies within the extension group, dependency on other Magento modules, and also the dependency on PHP extensions or other software dependency.

|ShopBb_Storage|
----------------

This is the main module, implementing configuration management and extensibility, shortly, most of the business logic for remote filesystem integration:

    * directories mapping
    * configure new remote media directories for new modules (e.g.: you want to store some reports in Azure Blob storage, you can configure a new directory for this report)
    * use the media storage system of your choice for any given directory or subdirectory
    * image resize in-place without sync back to local filesystem (this require having the same configuration for the main directory and the destination of resized files)
    * :term:`OOB` this module can be used in custom modules, none of Magento core features are touched

    .. important::

            Dependencies
                * Magento Modules
                    * Magento\Framework
                    * Magento\MediaStorage
                    * Magento\Store
                * Other extensions for Magento
                    * N/A
                * PHP extensions
                    * Imagick https://www.php.net/manual/en/book.imagick.php
                        This extension is used to resize images on demand, and is mandatory because it allow loading images by content and not by path on disk like GD library does.

|ShopBb_StorageS3|
------------------

    * implementation of Amazon S3 like API as a Magento filesystem driver

    .. important::

            Dependencies
                * Magento Modules
                    * Magento\\Framework
                    * Magento\\MediaStorage
                    * Magento\\Store
                * Other extensions for Magento
                    * Bb\\Storage - |ShopBb_StorageMarketplace|
                * Composer package
                    * aws/aws-sdk-php  3.x
                * PHP extensions
                    * N/A


|ShopBb_StorageOverwrites|
--------------------------

    * allows Bb_Storage features on built-in media directories

    .. important::

            Dependencies
                * Magento Modules
                    * Magento\\Framework
                    * Magento\\MediaStorage
                    * Magento\\Store
                * Other extensions for Magento
                    * Bb\\Storage - |ShopBb_StorageMarketplace|
                * PHP extensions
                    * N/A


|ShopBb_StorageCms|
-------------------

    * configure Magento_Cms module to use Bb_Storage
    * fix some weak points on Magento core components that are not using driver object to execute basic actions on files

    .. important::

            Dependencies
                * Magento Modules
                    * Magento\\Cms
                * Other extensions for Magento
                    * |ShopBb_StorageOverwrites|
                * PHP extensions
                    * N/A


|ShopBb_StorageCatalog|
-----------------------

    * configure Magento_Catalog module to use Bb_Storage
    * fix some weak points on Magento core components that are not using driver object to execute basic actions on files

    .. important::

            Dependencies
                * Magento Modules
                    * Magento\\Catalog
                * Other extensions for Magento
                    * |ShopBb_StorageOverwrites|
                * PHP extensions
                    * N/A


|ShopBb_StorageDownloadable|
----------------------------

    * Allow downloadable files to be saved in a different non-public media storage
    * fix some weak points on Magento core components that are not using driver object to execute basic actions on files

    .. important::

            Dependencies
                * Magento Modules
                    * Magento\\Downloadable
                * Other extensions for Magento
                    * |ShopBb_StorageOverwrites|
                * PHP extensions
                    * N/A


Installation process
====================

From source
-----------

In case you decide to install the extension from source (usually from sourced downloaded from Magento Marketplace) you need to unzip the files inside code directory creating proper subdirectory for module.
This method is working but for extended support and regular updates use composer installation.

Using composer
--------------

First you have to register composer repository using provided username and password:

.. code-block:: json

    {
        "repo.asset42.com": {
            "username": "<username>",
            "password": "<password>"
        }
    }

In case you need filesystem integration only for custom development:

.. code-block:: json

    {
        "...",
        "require": {
            "bb/mage-file-storage": "1.*",
            "bb/mage-file-storage-s3": "1.*"
        },
        "..."
    }


If you want to have mapping for Magento core directories you should also add Bb_StorageOverwrites module.

.. code-block:: json

    {
        "...",
        "require": {
            "bb/mage-file-storage": "1.*",
            "bb/mage-file-storage-s3": "1.*",
            "bb/mage-file-storage-overwrites": "1.*"
        },
        "..."
    }


Install new modules

.. code-block:: shell

    composer install
    bin/magento setup:upgrade


Contribution
------------

One way of contributing to this project is by creating a local repository with your original code version you are using on your installation (vx.x.x):

.. code-block:: shell

    $ git init
    $ git commit -m "original version"

Make the changes your are planning to submit, and create a patch file with those changes:

.. code-block:: shell

    $ git diff --no-prefix > describe-problem-vx.x.x.patch

    // you also can apply the path on your installation until the issue will be fix
    $ patch -p0 < describe-problem-vx.x.x.patch


.. include:: ./../all-pages/available-links.rst
