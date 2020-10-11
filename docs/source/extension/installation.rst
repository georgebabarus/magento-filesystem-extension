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

Each extension is available in Magento Marketplace individually.

    * So if you would like to integrate one external filesystem of your choice into a custom feature developed by your team you should buy the base extension |ShopBb_StorageMarketplace| and the needed filesystem driver eg: |ShopBb_StorageS3Marketplace|

    * If you would like to create a mapping of some of Magento Core directories to an external filesystem service you will need to buy both main extension |ShopBb_StorageMarketplace| and a driver of your choice but also this extension |ShopBb_StorageOverwritesMarketplace|

    .. warning::

        |ShopBb_StorageOverwritesMarketplace| is currently on the alpha phase so it will possibly affect some of Magento core features or 3rd party modules.


    The following modules Bb_StorageCms Bb_StorageCatalog and Bb_StorageDownloadable are shared packages for |ShopBb_StorageOverwritesMarketplace| and are offered for free. Those modules consist of code fixes in Magento Core modules where Filesystem drivers are not used accordingly, by using the Filesystem object.

    .. important::

        There is a further plan to integrate all Magento Community improvements into the core codebase.
        By purchasing this extension will move forward this project and plan for achieving better filesystem abstraction in Magento 2 platform.

.. include:: ./../messages.rst

.. contents:: Table of Contents

Software dependencies
=====================

Magento Modules
---------------

* Magento\Catalog
* Magento\Cms
* Magento\Downloadable
* Magento\Framework
* Magento\MediaStorage
* Magento\Store

PHP extensions
--------------

* Imagick https://www.php.net/manual/en/book.imagick.php
    This extension is used to resize images on demand, and is mandatory because it allow loading images by content and not by path on disk like GD library does.


S3 Integration
______________

Depends on AWS SDK composer package, and applies for all S3 like integrations.

.. code-block:: php

    "aws/aws-sdk-php": "3.x",



Installation process
====================

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


If you want to have mapping on Magento core directories you should also add Bb_StorageOverwrites module.

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
