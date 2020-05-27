*************
Extensibility
*************


.. include:: ./../messages.rst
.. contents:: Table of Contents

Extend filesystem to achieve more from shop
===========================================

Any other development that use filesystem and place files under media directory will work using  one of cloud storage driver as long as the directory is configured.

Basically site administrator decide if the files are store locally or on cloud storage depending on a configuration folder mapping for filesystem drivers.

Built with extensibility in mind
--------------------------------

Basically any remote file storage can work on top of this Magento Storage extension, as long as a integration driver is developed for the particular service.

All needed custom development for new integration will be a PHP class to implement this interface \Magento\Framework\Filesystem\DriverInterface


