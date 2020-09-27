
.. meta::
    :description lang=en:
        Getting started with Magento 2 and Amazon S3 filesystem integration

.. meta::
    :keywords lang=en:
        file storage service, cloud, integration, amazon s3

*********************
Amazon S3 integration
*********************

Integrating the Amazon S3 filesystem in Magento is available by installing the package bb/mage-file-storage-s3 containing the module named Bb_StorageS3.

Note that this module depends on the main module bb/mage-file-storage to be able to properly configure the connection and define new directories or mapping or existing directories.


.. include:: ./../messages.rst
.. contents:: Table of Contents


For now, only Amazon S3 storage service is supported by this filesystem extension, but many will integration extensions will be available to purchase soon.
All the news about extension road-map will be published here.

Magento S3 Driver Extension
===========================

For Amazon S3 storage service integration in Magento, you will need to purchase an additional extension available on |ShopS3Marketplace|

The package depends on aws/aws-sdk-php: 3.x and bb/mage-file-storage: 1.x, so if you install it from the source you also need to install those package.

After installation follows the general configuration process :ref:`available here<configuration>`.

Demo
=====

:ref:`You can find more information on the general demo page. <demo>`

.. include:: ./../all-pages/available-links.rst
