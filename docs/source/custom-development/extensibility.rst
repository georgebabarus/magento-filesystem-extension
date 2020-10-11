.. meta::
    :description lang=en:
        Extensibility for Magento 2 filesystem integration feature

.. meta::
    :keywords lang=en:
        file storage service, cloud, integration, extension

*************
Extensibility
*************

The extension is exposing extended interface (API) to execute filesystem operations, therefore, it's the main use-case of |ShopBb_StorageMarketplace| extension is in custom features.

Instead of using \Magento\Framework\Filesystem object, you will need to use \Bb\Storage\Framework\Filesystem or \Bb\Storage\Api\Filesystem\ExtendedFilesystemInterface.

.. include:: ./../messages.rst
.. contents:: Table of Contents

Extend filesystem to achieve more from your shop
================================================

Any other development that uses filesystem and place files under media directory will work using one of the cloud storage drivers as long as the directory is configured.

Basically, the site administrator decides if the files are store locally or on cloud storage depending on a configuration folder mapping for filesystem drivers.

Built with extensibility in mind
--------------------------------

Any remote file storage can work on top of this storage extension for Magento 2, as long as an integration driver is developed for the particular service.

All needed custom development for new integration will be a PHP class to implement this interface \Magento\Framework\Filesystem\DriverInterface


Custom development based on Bb_Storage
=======================================

Create new filesystem driver
-----------------------------

Simply implement all methods of this interface \Bb\Storage\Framework\Filesystem\DriverInterface.
After this step, you can register the class under env.php configuration for media storage under the driver key of connections configuration.
See: bb/mage-file-storage/dev/sample-files/env.php

.. code-block:: php

    namespace Bb\Storage\Api\Framework\Filesystem;

    use Bb\Storage\Api\Data\FileInterface;

    /**
     * Class Driver
     * @version 1.0.0
     */
    interface DriverInterface extends \Magento\Framework\Filesystem\DriverInterface
    {
        /**
         * Alternative for read method which is not returning the headers
         * On external filesystems is easier to extract content and headers in the same call
         *
         * @param string $path
         * @param $flag
         * @param $context
         * @return FileInterface
         */
        public function readFileObject(string $path, $flag = null, $context = null): FileInterface;

        /**
         * @param string $path
         * @return array
         */
        public function getHeaders(string $path): array;

        /**
         * @param $absolutePath
         * @return bool
         */
        public function isLeafDirectory(string $absolutePath): bool;

        /**
         * get an url to show files in frontend
         *
         * @param $path
         * @return string
         */
        public function getUrl($path): string;

        /**
         * @param $baseUrl
         * @return string
         */
        public function rewriteBaseUrl($baseUrl): string;

        /**
         * @return bool
         */
        public function hasBaseUrlRewrite(): bool;

        /**
         * @param \Magento\Framework\Filesystem\DriverInterface $targetDriver
         * @return bool
         */
        public function sameLocation(\Magento\Framework\Filesystem\DriverInterface $targetDriver): bool;

        /**
         * @return bool
         */
        public function requireFallbackDirectory(): bool;
    }


All configurations available and explained :ref:`here<configuration/connection>` are available for the newly implemented driver.


.. include:: ./../all-pages/available-links.rst
