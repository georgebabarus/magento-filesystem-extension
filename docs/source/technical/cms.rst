.. _cms:

============
CMS WYSIWYG
============

Here are some points where Magento is not fully compatible with external filesystems, and you can find differences before and after installing extensions.

Files Tree
==========

Trace & Key code classes
-------------------------

.. code-block:: php

    \Magento\Cms\Block\Adminhtml\Wysiwyg\Images\Tree
    \Bb\Storage\Block\Cms\Adminhtml\Wysiwyg\Images\Tree::getTreeJson
        \Magento\Cms\Model\Wysiwyg\Images\Storage\Collection
        \Bb\Storage\Model\Cms\Wysiwyg\Images\Storage\Collection::_collectRecursive

    \Magento\Cms\Helper\Wysiwyg\Images



Local filesystem files
~~~~~~~~~~~~~~~~~~~~~~~~~


Root: pub/media/
Current path: pub/media/


.. code-block:: php

    \Magento\Cms\Model\Wysiwyg\Images\Storage\Collection
        $nodes = {array} [1]
         0 = "catalog"

    \Bb\Storage\Model\Cms\Wysiwyg\Images\Storage::removeItemFromCollection
        _dirs = {array} [2]
         exclude = {array} [8]
          captcha = {array} [2]
          catalog/product = {array} [2]
          customer = {array} [2]
          downloadable = {array} [2]
          import = {array} [2]
          theme = {array} [2]
          theme_customization = {array} [2]
          tmp = {array} [2]
         include = {array} [0]

    \Bb\Storage\Block\Cms\Adminhtml\Wysiwyg\Images\Tree::getTreeJson

        $item = {Magento\Framework\DataObject} [2]
         _underscoreCache = {array} [23]
          Type = "type"
          ForceDisableRewrites = "force_disable_rewrites"
          DisableStoreInUrl = "disable_store_in_url"
          Scope = "scope"
          FlagData = "flag_data"
          SessionLocale = "session_locale"
          User = "user"
          NoSecret = "no_secret"
          ParentTheme = "parent_theme"
          ParentId = "parent_id"
          ThemeTitle = "theme_title"
          Object = "object"
          Extra = "extra"
          UpdatedAt = "updated_at"
          Acl = "acl"
          ReloadAclFlag = "reload_acl_flag"
          IsUrlNotice = "is_url_notice"
          Locale = "locale"
          ControllerAction = "controller_action"
          Request = "request"
          PciAdminUserIsPasswordExpired = "pci_admin_user_is_password_expired"
          Id = "id"
          Filename = "filename"
         _data = {array} [4]
          filename = "catalog"
          basename = "catalog"
          mtime = {int} 1591250266
          id = {int} 1

        $data = {array} [4]
         text = "catalog"
         id = "Y2F0YWxvZw--"
         path = false
         cls = "folder"

    [{"text":"catalog","id":"Y2F0YWxvZw--","path":false,"cls":"folder"}]

Root: pub/media/
Current path: pub/media/catalog

.. code-block:: php

    \Bb\Storage\Block\Cms\Adminhtml\Wysiwyg\Images\Tree::getTreeJson

        $item = {Magento\Framework\DataObject} [2]
         _underscoreCache = {array} [23]
          Type = "type"
          ForceDisableRewrites = "force_disable_rewrites"
          DisableStoreInUrl = "disable_store_in_url"
          Scope = "scope"
          FlagData = "flag_data"
          SessionLocale = "session_locale"
          User = "user"
          NoSecret = "no_secret"
          ParentTheme = "parent_theme"
          ParentId = "parent_id"
          ThemeTitle = "theme_title"
          Object = "object"
          Extra = "extra"
          UpdatedAt = "updated_at"
          Acl = "acl"
          ReloadAclFlag = "reload_acl_flag"
          IsUrlNotice = "is_url_notice"
          Locale = "locale"
          ControllerAction = "controller_action"
          Request = "request"
          PciAdminUserIsPasswordExpired = "pci_admin_user_is_password_expired"
          Id = "id"
          Filename = "filename"
         _data = {array} [4]
          filename = "catalog/product"
          basename = "product"
          mtime = {int} 1591250266
          id = {int} 1


        $data = {array} [4]
         text = "product"
         id = "Y2F0YWxvZy9wcm9kdWN0"
         path = "oduct"
         cls = "folder"

        [{"text":"product","id":"Y2F0YWxvZy9wcm9kdWN0","path":"oduct","cls":"folder"}]


S3 Driver
~~~~~~~~~

Root: media/
Current path: media/

.. code-block:: php

    \Magento\Framework\Filesystem\Directory\Read::read
        $files = {array} [18]
             0 = "media/.htaccess"
             1 = "media/.thumbs/"
             2 = "media/LICENSE.txt"
             3 = "media/catalog/"
             4 = "media/cms/"
             5 = "media/composer.json"
             6 = "media/customer/"
             7 = "media/downloadable/"
             8 = "media/import/"
             9 = "media/media/"
             10 = "media/refactor2/"
             11 = "media/refactor3/"
             12 = "media/styles.css"
             13 = "media/test/"
             14 = "media/theme/"
             15 = "media/theme_customization/"
             16 = "media/tmp/"
             17 = "media/wysiwyg/"

    \Bb\Storage\Block\Cms\Adminhtml\Wysiwyg\Images\Tree::getTreeJson
        $item = {Magento\Framework\DataObject} [2]
         _underscoreCache = {array} [24]
          Type = "type"
          ForceDisableRewrites = "force_disable_rewrites"
          DisableStoreInUrl = "disable_store_in_url"
          Scope = "scope"
          FlagData = "flag_data"
          SessionLocale = "session_locale"
          User = "user"
          NoSecret = "no_secret"
          ParentTheme = "parent_theme"
          ParentId = "parent_id"
          ThemeTitle = "theme_title"
          Object = "object"
          Extra = "extra"
          UpdatedAt = "updated_at"
          Acl = "acl"
          ReloadAclFlag = "reload_acl_flag"
          IsUrlNotice = "is_url_notice"
          Locale = "locale"
          ControllerAction = "controller_action"
          Request = "request"
          PciAdminUserIsPasswordExpired = "pci_admin_user_is_password_expired"
          Id = "id"
          Filename = "filename"
          Basename = "basename"
         _data = {array} [4]
          filename = "catalog/"
          basename = "catalog"
          mtime = {int} 0
          id = {int} 2

        $data = {array} [4]
         text = "catalog"
         id = "Y2F0YWxvZy8-"
         path = "g/"
         cls = "folder"

    {"text":"catalog","id":"Y2F0YWxvZy8-","path":"g\/","cls":"folder"}

Root: media/
Current path: media/catalog/

.. code-block:: php

    \Magento\Framework\Filesystem\Directory\Read::read
        $files = {array} [1]
         0 = "media/catalog/product/"

        $result = {array} [1]
         0 = "catalog/product/"

    \Bb\Storage\Block\Cms\Adminhtml\Wysiwyg\Images\Tree::getTreeJson
        $item = {Magento\Framework\DataObject} [2]
             _underscoreCache = {array} [23]
              Type = "type"
              ForceDisableRewrites = "force_disable_rewrites"
              DisableStoreInUrl = "disable_store_in_url"
              Scope = "scope"
              FlagData = "flag_data"
              SessionLocale = "session_locale"
              User = "user"
              NoSecret = "no_secret"
              ParentTheme = "parent_theme"
              ParentId = "parent_id"
              ThemeTitle = "theme_title"
              Object = "object"
              Extra = "extra"
              UpdatedAt = "updated_at"
              Acl = "acl"
              ReloadAclFlag = "reload_acl_flag"
              IsUrlNotice = "is_url_notice"
              Locale = "locale"
              ControllerAction = "controller_action"
              Request = "request"
              PciAdminUserIsPasswordExpired = "pci_admin_user_is_password_expired"
              Id = "id"
              Filename = "filename"
             _data = {array} [4]
              filename = "catalog/product/"
              basename = "product"
              mtime = {int} 0
              id = {int} 1

        $data = {array} [4]
         text = "product"
         id = "Y2F0YWxvZy9wcm9kdWN0Lw--"
         path = "g/product/"
         cls = "folder"

    [{"text":"product","id":"Y2F0YWxvZy9wcm9kdWN0Lw--","path":"g\/product\/","cls":"folder"}]



