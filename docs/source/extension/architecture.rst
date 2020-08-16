.. _extension/architecture:

.. meta::
    :description lang=en:
        Magento 2 File Storage Architecture abstraction for better file storage integration interface: more extensible and reusable.

.. meta::
    :keywords lang=en:
        Magento 2, architecture, extension, abstraction

****************
Architecture
****************

.. include:: ./../messages.rst

.. note::
    Before going deeper into the development details, please note that the this Magento 2 module is extending core module interfaces, keeping in mind the backward compatibility and keeping the changes as low asa possible.

.. contents:: Table of Contents


Software architecture
=====================


Magento extension architecture
------------------------------

Upload images in admin area
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Uploading files form user interfaces or programmatically at product should be compatible with any customization as log as is using Magento standard interfaces.

Nevertheless the business logic is not changed, and cloud storage services are added using regular/local filesystem interface.

.. image:: _static/architecture/upload-image.png
  :alt: Upload image for product or CMS blocks

.. note::
    Uploading products attachments for downloadable products works just like uploading the product image showed in the above schema.

.. note::
    Features: :term:`WOOB` :term:`v0.0.1`


Frontend resized image delivery
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Resized images could be delivered directly from storage system after creating the resized image in the main request or return a proxy url responsible to return the image if not exist.

The proxy can be implemented as follow:

* nginx config to request it from storage system and create a fallback request in case of error on Magento resize script
* in case you don't have access to a web server proxy configuration there is a option to return it directly from default Magento image resize script.

.. image:: _static/architecture/frontend-image-delivery.png
  :alt: Upload image for product or CMS blocks

.. note::
    :term:`SWSCNO` :term:`v0.0.1`


Frontend image delivery for original images
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Original images could be delivered directly from storage system, or the CDN in front of it, by configuring the base media url in admin configuration under Store -> Configuration.

.. note::
    :term:`WOOB` :term:`v0.0.1`

Infrastructure architecture
============================

Ideal infrastructure setup
--------------------------

.. warning::
    For now all images within the media folder are saved in the same bucket. Having multiple buckets will allow user to use this extension for downloadable products :term:`future work`

.. image:: _static/architecture/basic-infrastructure-architecture.png
  :alt: Basic infrastructure architecture


Possible optimization
---------------------

.. warning::
    This is :term:`future work` and will be detailed soon.

.. image:: _static/architecture/infrastructure-architecture-improved.png
  :alt: Infrastructure architecture improved



