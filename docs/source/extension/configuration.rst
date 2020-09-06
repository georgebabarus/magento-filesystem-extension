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
            'enabled'     => true,
            'directories' => [
                'mapping' => [
                    'media' => [
                        'main_connection' => 's3_public',
                        'connections'     => [
                            'file' => 'file',
                            'bbS3' => 's3_public'
                        ],
                        'directories'     => [
                            'downloadable'    => [
                                'main_connection' => 's3_private',
                                'connections'     => [
                                    'file' => 'file',
                                    'bbS3' => 's3_private'
                                ]
                            ]
                        ]
                    ]
                ],
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
                    ],
                    'media/downloadable'          => [
                        's3_private' => [
                            'directory_prefix'   => 'media/downloadable',
                            'overwrite_base_url' => false,
                            'reverse_proxy_path' => '',
                            'fallback_directory' => [
                                'directory_code' => 'media',
                                'driver_code'    => 'file'
                            ]
                        ]
                    ]
                ]
            ],
            'connections' => [
                's3_private' => [
                    'driver_code' => 'bbS3',
                    'driver'      => 'Bb\\StorageS3\\Filesystem\\Driver\\S3',
                    'stream_code' => 's31',
                    'region'      => 'us-east-1',
                    'bucket'      => '<PRIVATE_BUCKET>',
                    'credentials' => [
                        'key'    => 'minio',
                        'secret' => 'minio123'
                    ],
                    'endpoint'    => [
                        'origin'   => 'http://minio:9000',
                        'frontend' => 'http://127.0.0.1:9000/<PRIVATE_BUCKET>',
                    ],
                    'debug'       => true
                ],
                's3_public' => [
                    'driver_code' => 'bbS3',
                    'driver'      => 'Bb\\StorageS3\\Filesystem\\Driver\\S3',
                    'stream_code' => 's31',
                    'region'      => 'us-east-1',
                    'bucket'      => '<PUBLIC_BUCKET>',
                    'credentials' => [
                        'key'    => 'minio',
                        'secret' => 'minio123'
                    ],
                    'endpoint'    => [
                        'origin'   => 'http://minio:9000',
                        'frontend' => 'http://127.0.0.1:9000/<PUBLIC_BUCKET>',
                    ],
                    'debug'       => true
                ],
            ]
        ]
    ]

.. _configuration/directory_mapping:

Directory mapping
-----------------

Directory mapping link a specific path (eg: media/download from below example) to a main connection. Also allow you to set other available connections.

.. code-block:: php

    [
        'media_storage' => [
            'directories' => [
                'mapping' => [
                    'media' => [
                        'main_connection' => 's3_public',
                        'connections'     => [
                            'file' => 'file',
                            'bbS3' => 's3_public'
                        ],
                        'directories'     => [
                            'downloadable'    => [
                                'main_connection' => 's3_private',
                                'connections'     => [
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


Additional directory configuration are located under media_storage\directories\configs. This configs are located by directory path and driver code.

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


* directory_prefix the prefix on the destination filesystem relative to the root location
* overwrite_base_url change Magento base url configured in store config with the one configured on driver
* reverse_proxy_path if overwrite_base_url is false Magento base url will be prefixed with this path
* fallback_directory will contain an array of directory_code and driver_code representing the fallback solution in case the resource is not found in first location

.. _configuration/connection:

Connection configuration
------------------------

Connection details may be different depending on the Driver used for the service.

.. code-block:: php

    [
        'media_storage' => [
             'connections' => [
                's3_private' => [
                    'driver_code' => 'bbS3',
                    'driver'      => 'Bb\\StorageS3\\Filesystem\\Driver\\S3',
                    'stream_code' => 's31', # should be at most 3 letters.
                    'region'      => 'us-east-1',
                    'bucket'      => '<PRIVATE_BUCKET>',
                    'credentials' => [
                        'key'    => 'minio',
                        'secret' => 'minio123'
                    ],
                    'endpoint'    => [
                        'origin'   => 'http://minio:9000',
                        'frontend' => 'http://127.0.0.1:9000/<PRIVATE_BUCKET>',
                    ],
                    'debug'       => true
                ]
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