.. meta::
    :description lang=en:
        Extensibility for Magento 2 filesystem integration feature

.. meta::
    :keywords lang=en:
        file storage service, cloud, integration, extension

*************
Extensibility
*************

The extension is exposing extended interface (API) to execute filesystem operations, therefore, the main use-case of |ShopBb_FilesystemMarketplace| extension is in custom features.

Instead of using \\Magento\\Framework\\Filesystem object, you will need to use \\Bb\\Storage\\Framework\\Filesystem defined as API preference for \\Bb\\Storage\\Api\\Filesystem\\ExtendedFilesystemInterface.

.. include:: ./../messages.rst
.. contents:: Table of Contents


Extend filesystem to achieve more from your shop
================================================

The core module bb/filesystem offers the underlying structure of configuring new directories in the Magento application and mapping them to a remote or local filesystem.

Basically, you have to decide if one directory is stored locally or on a cloud storage service, by creating a configuration mapping in env.php file.

Built with extensibility in mind
--------------------------------

Any remote filesystem service can work on top of bb/filesystem, as long as an integration driver extension is developed for the particular service.

In case a driver extension is missing from marketplace, it can be developed implementing \\Bb\\Storage\\Api\\Filesystem\\DriverInterface and register it under di.xml.


Create new filesystem driver
=============================

* create a new module
* create a driver class which implements all methods of this interface \Bb\Storage\Api\Framework\Filesystem\DriverInterface.
* create a factory for your driver class by implementing \\Bb\\Storage\\Api\\Filesystem\\DriverFactoryInterface

    * the create" method of this class you will receive unique directory identifier and all required configuration needed to create new instances for your driver

* register the factory under factory driver pool

    .. code-block:: xml

        <type name="Bb\Storage\Framework\Filesystem\Driver\DriverFactoryPool">
            <arguments>
                <argument name="factories" xsi:type="array">
                    <item name="s3" xsi:type="string">Bb\StorageS3\Filesystem\Driver\S3Factory</item>
                </argument>
            </arguments>
        </type>

* register your driver in the driver pool

    .. code-block:: xml

        <type name="Bb\Storage\Framework\Filesystem\DriverPool">
            <arguments>
                <argument name="extraTypes" xsi:type="array">
                    <item name="s3" xsi:type="string">Bb\StorageS3\Filesystem\Driver\S3</item>
                </argument>
            </arguments>
        </type>


After all this step, you can define new directories or create mapping for existing ones using the created driver.

See: bb/filesystem/dev/sample-files/env.php

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
