.. meta::
    :description lang=en:
        Magento 2 File Storage Extension easy to use, extendable and configurable is all you need to move any media file to a cloud storage service like Amazon S3

.. meta::
    :keywords lang=en:
        Magento 2, file storage, extension, cloud storage, service

Magento file storage systems integration for media files
=========================================================

.. include:: messages.rst

Use this Magento module to decouple files storage form compute systems and scale them independently.

Once you have base module installed and configured you can configure already developed storage systems driver, or develop yourself. A driver will be basically a class implementing basic operations: read/write files or directory.


.. toctree::
   :caption: Extension specification

   introduction
   extension/architecture
   extension/installation
   extension/configuration
   extension/demo

.. toctree::
    :caption: Magento Amazon S3 integration

    amazon-s3/integration

.. toctree::
    :caption: Custom development

    custom-development/extensibility

.. toctree::
   :caption: Changelog and planning

   roadmap
   changelog


.. toctree::
   :caption: Technical documentation

   technical/cms


.. toctree::
   :caption: License

   license

Glossary
========

Here are defined some principles you will find during the particular topics on this documentation.

.. glossary::
    WOOB
        Works out of the box - without any particular configuration then setting up the storage credentials.

    SWSCN
        Some web server configuration needed, with partial support.

    SWSCNO
        Some web server configuration needed **from performance** perspective, with partial support.

    NEXT_MINOR_RELEASE
        The referred item is part of next minor release plan.

    NEXT_MAJOR_RELEASE
        The referred item is part of next major release plan.
