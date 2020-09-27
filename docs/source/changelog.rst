.. meta::
    :description lang=en:
        Magento 2 cloud storage integration extension changelog and releases

.. meta::
    :keywords lang=en:
        file storage service, release, changelog

*********
Changelog
*********

.. include:: messages.rst

master
======

New Features
-------------

Fixes
-----

Other Changes
--------------

.. glossary::

    v1.0.0

        Production-ready Bb_Storage - 1 September 2020
           * custom directories could be configured to use custom media storage
           * Magento Core directories could be mapped to new media storage, bug multiple mapping for the same directory is not production-ready. Check it and report any issue.
           * For now is advised to use the same media storage for all subdirectories except for downloadable files for downloadable products which could be stored in other filesystem location.


    v0.2.0

       Beta version - 1-July-2020
            * Downloadable products
            * Multiple buckets by folder mapping

    v0.1.0 - 15-June-2020

        * This version contains only a minimum code base to prove that Cloud storage service could easily and fully integrate into Magento 2 without any need for disk storage on the application server.

            * catalog product images
            * WYSIWYG images managed directly in cloud storage
            * Sync existing images to cloud storage

        #New Features


            * Media storage driver for Amazon S3
            * Magento core changes to improve filesystem abstraction

        #Other Changes

            * Documentation created

