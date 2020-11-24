.. meta::
    :description lang=en:
        File Storage configuration for integration of cloud storage services in Magento 2

.. meta::
    :keywords lang=en:
        Magento 2, configuration, cloud storage services

.. _configuration:

*************
Configuration
*************

For now, the available configuration is inserted into the deployment config file /etc/env.php since there are deployment related configs like database connection and are mandatory.

The configuration consists mainly of 3 components:

    * ``driver_configs`` which are configurations related to connection to the filesystem provider

    * ``directories -> mapping`` - in this path you will be able to define new directories paths or overwrite the existing ones under ./pub directory

    * ``directories -> configs`` - in this path you can configure additional settings related to specified directory and driver. (e.g.: custom endpoint delivery path)


.. include:: ./../messages.rst

.. contents:: Table of Contents

Application configuration
==========================

The sample configuration file could be found under the dev directory in ``Bb_Filesystem`` module:
``dev/sample-files/env.php``

The feature flag for media storage is ``media_storage/enabled``.

.. code-block:: php

    [
        'media_storage' => [
            'enabled'        => true,
            'directories'    => [
                'mapping' => [
                    'media' => [
                        'main_driver'    => 's3_lo',
                        'driver_configs' => [
                            'file' => 'file',
                            's3'   => 's3_lo'
                        ],
                        'directories'    => [
                            'catalog'         => [
                                'main_driver'    => 's3_lo',
                                'driver_configs' => [
                                    'file' => 'file',
                                    's3'   => 's3_lo'
                                ],
                                'directories'    => [
                                    'product/cache' => [
                                        'main_driver' => 's3_lo'
                                    ]
                                ]
                            ],
                            'downloadable'    => [
                                'main_driver'    => 's3_aws',
                                'driver_configs' => [
                                    'file' => 'file',
                                    's3'   => 's3_lo'
                                ]
                            ],
                            'invalid-mapping' => [
                                'main_driver' => 'invalid-mapping',
                            ],
                            'other'           => [
                                'main_driver' => 'file'
                            ],
                            'empty-mapping'   => []
                        ]
                    ]
                ],
                'configs' => [
                    'media'                       => [
                        's3_lo' => [
                            'directory_prefix'   => 'media',
                            'reverse_proxy_path' => 'lo-proxy',
                            'overwrite_base_url' => true,
                            'fallback_directory' => [
                                'directory_code' => 'media',
                                'driver_code'    => 'file'
                            ]
                        ]
                    ],
                    'media/catalog'               => [
                        's3_lo' => [
                            'directory_prefix'   => 'media/catalog',
                            'overwrite_base_url' => true,
                            'reverse_proxy_path' => 'lo-proxy',
                            'fallback_directory' => [
                                'directory_code' => 'media',
                                'driver_code'    => 'file'
                            ]
                        ]
                    ],
                    'media/catalog/product/cache' => [
                        's3_lo' => [
                            'directory_prefix'   => 'media/catalog/product/cache',
                            'overwrite_base_url' => true,
                            'reverse_proxy_path' => 'lo-proxy',
                            'fallback_directory' => [
                                'directory_code' => 'media',
                                'driver_code'    => 'file'
                            ]
                        ]
                    ],
                    'media/downloadable'          => [
                        's3_aws' => [
                            'directory_prefix'   => 'media/downloadable',
                            'overwrite_base_url' => true,
                            'reverse_proxy_path' => 'aws-proxy',
                            'fallback_directory' => [
                                'directory_code' => 'media',
                                'driver_code'    => 'file'
                            ]
                        ]
                    ],
                    'media/other'                 => [
                        'file' => [
                            'directory_prefix' => 'media/other',
                        ]
                    ],
                    'media/invalid-mapping'       => [
                        'invalid-mapping' => [

                        ]
                    ]
                ]
            ],
            'driver_configs' => [
                's3_do'  => [
                    'driver_code' => 's3',
                    'stream_code' => 's3m',
                    'region'      => 'fra1',
                    'bucket'      => 'testbb',
                    'credentials' => [
                        'key'    => '',
                        'secret' => ''
                    ],
                    'endpoint'    => [
                        'origin'   => 'https://fra1.digitaloceanspaces.com',
                        'frontend' => 'https://fra1.digitaloceanspaces.com/testbb',
                    ],
                    'debug'       => true
                ],
                's3_aws' => [
                    'driver_code' => 's3',
                    'stream_code' => 's3m',
                    'region'      => 'eu-central-1',
                    'bucket'      => 'magento.storage',
                    'credentials' => [
                        'key'    => '',
                        'secret' => ''
                    ],
                    'endpoint'    => [
                        'origin'   => 'https://s3.eu-central-1.amazonaws.com',
                        'frontend' => 'https://s3.eu-central-1.amazonaws.com',
                    ],
                    'debug'       => true
                ],
                's3_lo'  => [
                    'driver_code' => 's3',
                    'stream_code' => 's3l',
                    'region'      => 'us-east-1',
                    'bucket'      => 'testbb',
                    'credentials' => [
                        'key'    => 'minio',
                        'secret' => 'minio123'
                    ],
                    'endpoint'    => [
                        'origin'   => 'http://minio:9000',
                        'frontend' => 'http://127.0.0.1:9000/testbb',
                    ],
                    'debug'       => true
                ]
            ]
        ]
    ];

.. _configuration/directory_mapping:

Directory mapping
-----------------

Directory mapping link a specific path (e.g.: ``media/download`` from the below example) to the main connection. Also, allows you to set other available connections.

.. code-block:: php

    [
        'media_storage' => [
            'enabled'        => true,
            'directories'    => [
                'mapping' => [
                    'media' => [
                        'main_driver'    => 's3_lo',
                        'driver_configs' => [
                            'file' => 'file',
                            's3'   => 's3_lo'
                        ],
                        'directories'     => [ // this are subdirectories
                            'downloadable'    => [
                                'main_driver' => 's3_private', // other driver config identifier here
                                'driver_configs'     => [
                                    'file' => 'file',
                                    'bbS3' => 's3_private'
                                ]
                            ]
                        ]
                    ]
                ],
            ]
        ]
    ]

=========================  =======================  ======================================================
Field                      Data type                Description
=========================  =======================  ======================================================
main_driver                 string                  is the main driver used for the directory, this will be always used unless, is explicitly specified to use another one form the bellow available driver configs.
driver_configs              array|null              Other available drivers and driver_configs for a specific directory. Consist of mapping of diver code as the key to an available driver config under storage_config/driver_configs as value.
=========================  =======================  ======================================================

Additional directory configuration is located under ``media_storage/directories/configs``. These configs are located by directory path and driver code.

.. code-block:: php

        'media_storage' => [
            'directories' => [
                'configs' => [
                    'media'                       => [
                        's3_public' => [
                            'directory_prefix'   => 'media',
                            'reverse_proxy_path' => 'lo-proxy',
                            'overwrite_base_url' => true,
                            'fallback_directory' => [
                                'directory_code' => 'media',
                                'driver_code'    => 'file'
                            ]
                        ]
                    ]
                ]
            ]
        ]
    ]

=========================  =======================  ======================================================
Field                      Data type                Description
=========================  =======================  ======================================================
directory_prefix            string, required        the prefix on the destination filesystem relative to the root location
overwrite_base_url          bool|null               change the Magento base URL configured in store config with the one configured on driver
reverse_proxy_path          string|null             if overwrite_base_url is false Magento base URL will be prefixed with this path
fallback_directory          array|null              will contain an array of directory_code and driver_code representing the fallback solution in case the resource is not found in the first location
=========================  =======================  ======================================================

.. _configuration/connection:

Connection configuration
------------------------

Connection details may be different depending on the Driver used for the service. This is an example of connection details for the Amazon S3 filesystem driver.

.. code-block:: php

    [
        'media_storage' => [
            'driver_configs' => [
                's3_do'  => [
                    'driver_code' => 's3', // Driver code registered by driver nodule
                    'stream_code' => 's3m', // this is a stream code, some modules need it. use 3 letters code unique per connection
                    'region'      => 'fra1',
                    'bucket'      => 'testbb',
                    'credentials' => [
                        'key'    => '',
                        'secret' => ''
                    ],
                    'endpoint'    => [
                        'origin'   => 'https://fra1.digitaloceanspaces.com',
                        'frontend' => 'https://fra1.digitaloceanspaces.com/testbb',
                    ],
                    'debug'       => true
                ],
            ]
        ]
    ]

=========================  =======================  ======================================================
Field                      Data type                Description
=========================  =======================  ======================================================
driver_code                 string, required        identify the driver class need, registered in di.xml
stream_code                 string|null             some drivers are using stream related PHP function and you need to specify 3 letters unique code for each connection
region                      string|null             this is needed for S3 driver
bucket                      string|null             this is needed for S3 driver
credentials                 array|null              credentials consist of key and secret for S3 driver
endpoint                    array|null              origin endpoint is the URL used for API calls with credentials, frontend endpoint is used to serve public
debug                       bool|null               debug mode is doing logs on requests made to storage service
=========================  =======================  ======================================================


Web-server configuration
==============================


.. code-block:: shell

    location ~ ^/proxy/media/(.*)$ {
        proxy_http_version     1.1;
        proxy_set_header       Connection "";
        proxy_set_header       Authorization '';
        proxy_set_header       Host testbb.fra1.digitaloceanspaces.com;
        proxy_hide_header      x-amz-id-2;
        proxy_hide_header      x-amz-request-id;
        proxy_hide_header      x-amz-meta-server-side-encryption;
        proxy_hide_header      x-amz-server-side-encryption;
        proxy_hide_header      Set-Cookie;
        proxy_ignore_headers   Set-Cookie;
        proxy_intercept_errors on;
        #proxy_set_header       X-Original-URI /media/$1;
        proxy_pass             https://-your-bucket-name-.fra1.digitaloceanspaces.com/media/$1;

        add_header             Cache-Control max-age=31536000;
        add_header X-ORIGINAL-URI "https://-your-bucket-name-.fra1.digitaloceanspaces.com/media/$1";

        error_page 404 = @fallback-media;
    }

    location @fallback-media {
        root $MAGE_ROOT/pub;

        fastcgi_buffers 1024 4k;
        fastcgi_param  PHP_FLAG  "session.auto_start=off \n suhosin.session.cryptua=off";
        fastcgi_param  PHP_VALUE "memory_limit=756M \n max_execution_time=18000";
        fastcgi_read_timeout 600s;
        fastcgi_connect_timeout 600s;
        fastcgi_index   get.php;
        fastcgi_param   SCRIPT_FILENAME    $MAGE_ROOT/pub/get.php;
        fastcgi_param   SCRIPT_NAME        /get.php?file=$1;
        fastcgi_param   REQUEST_URI             $1;
        fastcgi_param   DOCUMENT_URI            $1;
        include         fastcgi_params;
        fastcgi_pass   fastcgi_backend;
    }


Admin panel configuration
==========================

For now, there is no configuration in the admin panel. See the roadmap for more details.

.. include:: ./../all-pages/available-links.rst
