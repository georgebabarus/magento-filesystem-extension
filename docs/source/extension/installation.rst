.. meta::
    :description lang=en:
        Getting started with Magento 2 cloud file storage service integration

.. meta::
    :keywords lang=en:
        file storage service, cloud, integration

****************
Getting Started
****************

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

.. code-block::

    "aws/aws-sdk-php": "3.x",



Installation process
====================

Using composer
--------------

When using custom storage drivers for custom development:

.. code-block:: json

    {
        "...",
        "require": {
            "bb/mage-file-storage": "1.*",
            "bb/mage-file-storage-s3": "1.*"
        },
        "..."
    }


When you want to also overwrite Magento's core modules you should add Bb_StorageOverwrites module.

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

Register composer repository using provided username and password:

.. code-block:: json

    {
        "repo.asset42.com": {
            "username": "<username>",
            "password": "<password>"
        }
    }

Install new modules

.. code-block:: shell

    composer install
    bin/magento setup:upgrade

