
.. _roadmap:

.. meta::
    :description lang=en:
        Future planning for Magento 2 cloud file storage service integration extension.

.. meta::
    :keywords lang=en:
        magento 2, roadmap, planning, file storage service, cloud, integration

*********
Roadmap
*********

.. glossary::

    v1.0.0
        Production ready Bb_Storage - 1 September 2020
           * custom directories could be configured to use custom media storage
           * Magento Core directories could be mapped to new media storage, bug multiple mapping for same directory is not production ready. Check it and report any issue.
           * For now is advised to use same media storage for all subdirectories except for downloadable files for downloadable products witch could be stored in other filesystem location.

    v1.1.0 - 1 November 2020
        * break dependency on Catalog, Cms and Downloadable modules in order to allow independent installation and usage.
            * most probably the media directory will be separated by the type of the module using it
            * multiple frontend urls based on media storage of subdirectory
            * avoid forcing usage of just one media storage for Catalog and Cms components

    v1.2.0 - 1 December 2020
        * integrate all Magento core refactoring and fixes into Magento Community project. Here we are talking mainly of placed where local filesystem is taken as granted, and php file management functions are called to execute actions that are already implemented in Magento Drivers.

Future work
=================

.. include:: messages.rst

.. glossary::
    future work
        All items marked with this tag are not part of a planned release
