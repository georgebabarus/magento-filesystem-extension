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


Custom development based on Bb_Storage
=======================================

Create new filesystem driver
-----------------------------

Simply implement all methods of this interface \Bb\Storage\Framework\Filesystem\DriverInterface.
After this step you can register the class under env.php configuration for media storage under driver key of connections configuration.
See: bb/mage-file-storage/dev/sample-files/env.php

.. code-block:: php

    namespace Bb\Storage\Framework\Filesystem;

    use Bb\Storage\Model\FileInterface;

    /**
     * Class Driver
     * @version 1.0.0
     */
    interface DriverInterface extends \Magento\Framework\Filesystem\DriverInterface
    {
        /**
         * @param string $path
         * @param $flag
         * @param $context
         * @return FileInterface
         */
        public function fileGetObject(string $path, $flag = null, $context = null): FileInterface;

        /**
         * @param string $path
         * @return array
         */
        public function headers(string $path): array;

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
         * @param $originalBaseUrl
         * @return string
         */
        public function rewriteBaseUrl($originalBaseUrl): string;

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

All configuration available and explained :ref:`here<configuration/connection>` are available for the newly implemented driver.