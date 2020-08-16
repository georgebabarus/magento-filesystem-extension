.. role:: raw-html-m2r(raw)
   :format: html

Magento file (cloud) storage systems integration for media files
=================================================================

.. include:: messages.rst

Storing media files involve some work when you decide to scale horizontally.
Also having to care about disk space and disk mounting may be useless when you are already have a easy to use object storage service.

There are plenty of cloud static files storage services offered with various feature but most of them have same basic ideas:

* allow secure upload remotely of files
* deliver static file public or privately
* built in Content delivery network (CDN)

With this idea in mind you can identify a use-case for e-commerce website for storing images and video for products, categories or CMS pages and deliver them using a CDN. Or even storing private content like downloadable products.

Using cloud storage should be easy to configure and use, ans should not add additional complexity to the system but on contrary.

Reed the documentation https://magento-filesystem-extension-docs.readthedocs.io to see some of the key advantages of using this Magento 2 extension to integrate with various cloud file storage systems in a platform agnostic manner.


Useful links
------------

Read more about Object Storage services online:

* Amazon Simple Storage Service S3
    https://docs.aws.amazon.com/s3/index.html
* Azure Cloud File Storage/Blob storage
    https://azure.microsoft.com/en-us/services/storage/blobs
* Google Cloud Storage
    https://cloud.google.com/storage
* Digital Ocean Block Storage
    https://www.digitalocean.com/products/block-storage/
* Linode Object storage
    https://www.linode.com/products/object-storage/

Read more about CDN:

* Amazon CloudFront
    https://aws.amazon.com/cloudfront/
* Azure CDN
    https://docs.microsoft.com/en-us/azure/cdn/
* Akamai
    https://www.akamai.com/


Author
======

`George Babarus <https://github.com/georgebabarus>`_
