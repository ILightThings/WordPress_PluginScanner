# WordPress_PluginScanner

Usage: `wp_plugin_scan.py http://site.com`

Uses a 404 method check for existing plugins. WPScan was too slow and only did 1.2 requests a second. This method uses 100 Threads for around 80,000 possible plugins.

 Should not be used in production and only in test enviroments that you have permission to use. Security Research only. Possible DOS warning.
