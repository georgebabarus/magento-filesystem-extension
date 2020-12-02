
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

    23 December 2020

        * publish bb/filesystem-overwrites the module in charge of mapping existing directories in Magento to Remote file systems
        * break the dependency between bb/filesystem-catalog, bb/filesystem-cms and bb/filesystem-downloadable modules in order to allow independent installation and usage.

            * most probably the media directory will be separated by the type of the module using it
            * multiple frontend URLs based on media storage of subdirectory
            * avoid forcing usage of just one media storage for Catalog and Cms components

    15 January 2021

        * compatibility for Linode Object storage and Digital Ocean Block Storage

    1 February 2021

        Publish new filesystem driver for Azure Blob Storage

    1 March 2021

        Publish new filesystem driver for Google Storage Service

    1 July 2021

        * integrate all refactoring and fixes into the Magento Community project.

            * Here we are talking of places where the filesystem component is not properly used in Magento Core: bb/filesystem-catalog, bb/filesystem-cms and bb/filesystem-downloadable

Future work
=================

.. include:: messages.rst

.. glossary::
    future work

        All items marked with this tag are not part of a planned release


.. include:: ./all-pages/available-links.rst
