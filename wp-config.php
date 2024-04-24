<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the installation.
 * You don't have to use the website, you can copy this file to "wp-config.php"
 * and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * Database settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://wordpress.org/documentation/article/editing-wp-config-php/
 *
 * @package WordPress
 */

// ** Database settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'test_site' );

/** Database username */
define( 'DB_USER', 'root' );

/** Database password */
define( 'DB_PASSWORD', '' );

/** Database hostname */
define( 'DB_HOST', 'localhost' );

/** Database charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8mb4' );

/** The database collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**#@+
 * Authentication unique keys and salts.
 *
 * Change these to different unique phrases! You can generate these using
 * the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}.
 *
 * You can change these at any point in time to invalidate all existing cookies.
 * This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define( 'AUTH_KEY',         'T-6>DjPX0y6(&bXSzf-tIVhy1l6}_sQ#U|&sntIkjepi>QEU<+q/4yajS0([#Q{&' );
define( 'SECURE_AUTH_KEY',  '`q&za7dpzTWRwC!<Ho8mR[o2P*u|6w7S%mIp,[h://>974y8z)CtyD;p{hg{/=L+' );
define( 'LOGGED_IN_KEY',    'vo!//qgEf]_<}UC<^19!Oa>NxdC|HXQ.l EO%SbXhsNH:)kZC<<F<%naSk`A6EvQ' );
define( 'NONCE_KEY',        '=.(xBQBErCVV3#-cwRD>[Gva=m.`GELQ~qY~XQimxnbC|%*Z:Qj>63Ii})6b|F3W' );
define( 'AUTH_SALT',        'B0zi&=@0/w~D[l#0Z)=KDg1/0Y*V%8Q_![t=Z!LyYR8]2xJSI(U:?JdIoh!JZ5E:' );
define( 'SECURE_AUTH_SALT', '`w)><p|]8Th`|^z(# )<fT/Io9SW4WWVPVP4^glv-b,C:VVALmYGRKZL(,y D@gd' );
define( 'LOGGED_IN_SALT',   'f^b5%b@4phoA^=%#R26dqhZ%ANvw}w*/1G`<d6|qF=/7/jyeYhxS)-3OPR!MihRR' );
define( 'NONCE_SALT',       'q4Xi?u#8C142$GTdIhi,,&;|wT%8sy`|d?;&j#Qdth5KvM(FlDTzHG)^B_3~v=v2' );

/**#@-*/

/**
 * WordPress database table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix = 'tp_';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the documentation.
 *
 * @link https://wordpress.org/documentation/article/debugging-in-wordpress/
 */
define( 'WP_DEBUG', false );

/* Add any custom values between this line and the "stop editing" line. */



/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', __DIR__ . '/' );
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';
