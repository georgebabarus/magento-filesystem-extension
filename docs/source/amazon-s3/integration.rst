
.. meta::
    :description lang=en:
        Getting started with Magento 2 and Amazon S3 filesystem integration

.. meta::
    :keywords lang=en:
        file storage service, cloud, integration, amazon s3


*********************
Filesystem drivers
*********************

For now, only Amazon S3 storage service is supported by this filesystem extension, but many will integration extensions will be available to purchase soon.
All news about the extension road-map will be published here.


.. include:: ./../messages.rst
.. contents:: Table of Contents



S3 Driver Extension for Magento 2
=================================

Integrating the Amazon S3 filesystem in Magento is available by installing the package bb/filesystem-s3 containing the module named bb/filesystem-s3.

Note that this module depends on the main module bb/filesystem (at an additional cost) to be able to properly configure the connection and define new directories or mapping existing directories.

The package depends on aws/aws-sdk-php: 3.x and bb/filesystem: 1.x, so, if you install it from the source you also need to install those package.

After installation follows the general configuration process :ref:`available here<configuration>`.

Demo
=====

:ref:`You can find more information on the general demo page. <demo>`

.. include:: ./../all-pages/available-links.rst
