.. meta::
    :description lang=en:
        Magento 2 File Storage configuration for cloud storage services

.. meta::
    :keywords lang=en:
        Magento 2, configuration, cloud storage services

*************
Configuration
*************

.. include:: ./../messages.rst

.. contents:: Table of Contents

Application configuration
==========================

.. code-block:: php

    [
        'media_storage' => [
        'folder_prefix' => 'folder name',
        'path_connection' => [
            'media' => [
                Connection::DEFAULT_CONNECTION => 'media',
                Connection::CONNECTION_CODE_FILE => Connection::CONNECTION_CODE_FILE,
                S3::POOL_TYPE => 'media'
            ]
        ],
        'connection' => [
            'media' => [
                'active'      => true,
                'driver_code' => 's3media', // mandatory
                'driver' => S3::class,  // mandatory
                'stream_code' => 's3media',
                'region' => 'fra1',
                'bucket' => 'bucket_name',
                'credentials' => [
                    'key' => 'your_api_key',
                    'secret' => 'your_secret_key',
                ],
                'endpoint' => [
                    'origin' => 'https://fra1.digitaloceanspaces.com',
                    'cdn' => 'https://fra1.digitaloceanspaces.com',
                    'resize' => 'https://fra1.digitaloceanspaces.com',
                ],
            ],
        ],
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