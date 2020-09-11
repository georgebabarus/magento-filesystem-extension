.. meta::
    :description lang=en:
        Magento 2 File Storage configuration for cloud storage services

.. meta::
    :keywords lang=en:
        Magento 2, configuration, cloud storage services

.. _configuration:

*************
Configuration
*************

For now available configuration are inserted into the deployment config file /etc/env.php since there are deployment related configs like database connection and are mandatory.

Mainly the configuration consists of 3 components:

    * driver_configs which are configurations related to connection to the filesystem provider

    * directories -> mapping - in this path you will be able to define new directories paths or overwrite existing ones under ./pub directory

    * directories -> configs - in this path you can configure additional settings related to specified directory and driver. eg: custom endpoint delivery path


.. include:: ./../messages.rst

.. contents:: Table of Contents

Application configuration
==========================

Sample configuration file could be found under dev directory in Bb_Storage module:
dev/sample-files/env.php

The feature flag for media storage is media_storage/enabled.

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

Directory mapping link a specific path (eg: media/download from below example) to a main connection. Also allow you to set other available connections.

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


Additional directory configuration are located under media_storage/directories/configs. This configs are located by directory path and driver code.

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


* directory_prefix
    * required
    * string, not empty
    * the prefix on the destination filesystem relative to the root location
* overwrite_base_url
    * not required
    * bool true/false
    * change Magento base url configured in store config with the one configured on driver

* reverse_proxy_path
    * not required
    * string, empty allowed
    * if overwrite_base_url is false Magento base url will be prefixed with this path

* fallback_directory
    * not required
    * array
    * will contain an array of directory_code and driver_code representing the fallback solution in case the resource is not found in first location

.. _configuration/connection:

Connection configuration
------------------------

Connection details may be different depending on the Driver used for the service.

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

For now there are no configuration in admin panel. See roadmap for more details.



.. include:: ./../all-pages/available-links.rst
