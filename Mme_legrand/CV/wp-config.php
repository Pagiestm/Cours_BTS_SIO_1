<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the installation.
 * You don't have to use the web site, you can copy this file to "wp-config.php"
 * and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * MySQL settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://wordpress.org/support/article/editing-wp-config-php/
 *
 * @package WordPress
 */

// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', '' );

/** MySQL database username */
define( 'DB_USER', 'epiz_30419822_CV' );

/** MySQL database password */
define( 'DB_PASSWORD', '30nqHmihqatZzJ' );

/** MySQL hostname */
define( 'DB_HOST', 'sql109.epizy.com' );

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
define( 'AUTH_KEY',         'rksai131stqh5aukhftvmmwsi2ijeda9ot4ihsppyiisk1ooy2u1dybiai9qzywx' );
define( 'SECURE_AUTH_KEY',  'psdxzhs1su1uvhxlrtexbmaailxtjo1vefyrl47d9cchi5ljs9fhsngs9g9764z3' );
define( 'LOGGED_IN_KEY',    'ehvcnjz3v2sxujeivjje1onwekknyvzhallvvzt59jg3u1dwzppryznfb8osbuhs' );
define( 'NONCE_KEY',        'qqygch5atxdcf9uzr8j5sn9ei5ascyfyxg5tdzmru2byrq6xy160hyp04gam214q' );
define( 'AUTH_SALT',        'qhj3g1jatvxvoip0kfd0nlxfbvjhjxawxtlthw86io7uj15uefbtzhgz4kwhvwtc' );
define( 'SECURE_AUTH_SALT', 'fqi2vp2cchkjtviryml4hjxldiotcfqxxrrbbvvs94rxsrxpjmydmxkhf1cnm1mr' );
define( 'LOGGED_IN_SALT',   '0n8hoolvbgmosylc14vtnskndtjkbrkn7seueevywdwmcjbmizyouhlr1m4xjpmz' );
define( 'NONCE_SALT',       '0uamxn5rdkdcilzhyetp4bsb7xrmjppehmzcp4vnpbj1gf6snzugv9ksntuqaj0x' );

/**#@-*/

/**
 * WordPress database table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix = 'wpub_';

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
 * @link https://wordpress.org/support/article/debugging-in-wordpress/
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
