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

    * So if you would like to integrate one external filesystem of your choice into a custom feature developed by your team you should buy the base extension |ShopBb_FilesystemMarketplace| and the needed filesystem driver eg: |ShopBb_FilesystemS3Marketplace|

    * If you would like to create a mapping of some of Magento Core directories to an external filesystem service you will need to buy both main extension |ShopBb_FilesystemMarketplace| and a driver of your choice but also this extension |ShopBb_FilesystemOverwritesMarketplace|

    .. warning::

        |ShopBb_FilesystemOverwritesMarketplace| is currently on the alpha phase so it will possibly affect some of Magento core features or 3rd party modules.


        The following modules bb/filesystem-cms bb/filesystem-catalog and bb/filesystem-downloadable are shared packages for |ShopBb_FilesystemOverwritesMarketplace| and are offered for free. Those modules consist of code fixes in Magento Core modules where Filesystem drivers are not used accordingly, by using the Filesystem object.

        .. important::

            There is a further plan to integrate all Magento Community improvements into the core codebase.
            By purchasing this extension will move forward this project and plan for achieving better filesystem abstraction in Magento 2 platform.

Software dependencies
=====================

Bellow you will find both the extension commercial name and the module name (in parentheses), short description of the extension and the dependencies within the extension group, dependency on other Magento modules, and also the dependency on PHP extensions or other software dependency.

|ShopBb_Filesystem|
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
                    * N/A

|ShopBb_FilesystemS3|
------------------

    * implementation of Amazon S3 like API as a Magento filesystem driver

    .. important::

            Dependencies
                * Magento Modules
                    * Magento\\Framework
                    * Magento\\MediaStorage
                    * Magento\\Store
                * Other extensions for Magento
                    * Bb\\Storage - |ShopBb_FilesystemMarketplace|
                * Composer package
                    * aws/aws-sdk-php  3.x
                * PHP extensions
                    * N/A


|ShopBb_FilesystemOverwrites|
--------------------------

    * allows bb/filesystem features on built-in media directories

    .. important::

            Dependencies
                * Magento Modules
                    * Magento\\Framework
                    * Magento\\MediaStorage
                    * Magento\\Store
                * Other extensions for Magento
                    * Bb\\Storage - |ShopBb_FilesystemMarketplace|
                * PHP extensions
                    * Imagick https://www.php.net/manual/en/book.imagick.php
                        This extension is used to resize images on demand, and is mandatory because it allow loading images by content and not by path on disk like GD library does.

|ShopBb_FilesystemCms|
-------------------

    * configure Magento_Cms module to use bb/filesystem
    * fix some weak points on Magento core components that are not using driver object to execute basic actions on files

    .. important::

            Dependencies
                * Magento Modules
                    * Magento\\Cms
                * Other extensions for Magento
                    * |ShopBb_FilesystemOverwrites|
                * PHP extensions
                    * N/A


|ShopBb_FilesystemCatalog|
-----------------------

    * configure Magento_Catalog module to use bb/filesystem
    * fix some weak points on Magento core components that are not using driver object to execute basic actions on files

    .. important::

            Dependencies
                * Magento Modules
                    * Magento\\Catalog
                * Other extensions for Magento
                    * |ShopBb_FilesystemOverwrites|
                * PHP extensions
                    * N/A


|ShopBb_FilesystemDownloadable|
----------------------------

    * Allow downloadable files to be saved in a different non-public media storage
    * fix some weak points on Magento core components that are not using driver object to execute basic actions on files

    .. important::

            Dependencies
                * Magento Modules
                    * Magento\\Downloadable
                * Other extensions for Magento
                    * |ShopBb_FilesystemOverwrites|
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

In case you need filesystem integration only for custom development:

.. code-block:: json

    {
        "...",
        "require": {
            "bb/filesystem": "x.*",
            "bb/filesystem-s3": "x.*"
        },
        "..."
    }


If you want to have mapping for Magento core directories you should also add bb/filesystem-overwrites module.

.. code-block:: json

    {
        "...",
        "require": {
            "bb/filesystem": "x.*",
            "bb/filesystem-s3": "x.*",
            "bb/filesystem-overwrites": "x.*"
        },
        "..."
    }


Install new modules

.. code-block:: shell

    composer install
    bin/magento setup:upgrade


Not mandatory, once you buy the extensions from Magento Marketplace you can request access and register the private composer repository, to have access as soon as possible to new or beta versions:

.. code-block:: json

    {
        "repo.asset42.com": {
            "username": "<username>",
            "password": "<password>"
        }
    }

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
