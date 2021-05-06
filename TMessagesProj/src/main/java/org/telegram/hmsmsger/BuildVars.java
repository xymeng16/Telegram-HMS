/*
 * This is the source code of Telegram for Android v. 7.x.x.
 * It is licensed under GNU GPL v. 2 or later.
 * You should have received a copy of the license in this archive (see LICENSE).
 *
 * Copyright Nikolai Kudashov, 2013-2020.
 */

package org.telegram.hmsmsger;

import android.content.Context;
import android.content.SharedPreferences;

public class BuildVars {

    public static boolean DEBUG_VERSION = true;
    public static boolean DEBUG_PRIVATE_VERSION = false;
    public static boolean LOGS_ENABLED = true;
    public static boolean USE_CLOUD_STRINGS = true;
    public static boolean CHECK_UPDATES = true;
    public static int BUILD_VERSION = 2293;
    public static String BUILD_VERSION_STRING = "7.7.0";
    public static int APP_ID = 2376940;
    public static String APP_HASH = "643e1c932ec626e5fad77b6239eb7001";
    public static String APPCENTER_HASH = "a5b5c4f5-51da-dedc-9918-d9766a22ca7c";
    public static String APPCENTER_HASH_DEBUG = "f9726602-67c9-48d2-b5d0-4761f1c1a8f3";
    //
    public static String SMS_HASH = DEBUG_VERSION ? "O2P2z+/jBpJ" : "oLeq9AcOZkT";
    public static String PLAYSTORE_APP_URL = "https://play.google.com/store/apps/details?id=org.telegram.hmsmsger";

    static {
        if (ApplicationLoader.applicationContext != null) {
            SharedPreferences sharedPreferences = ApplicationLoader.applicationContext.getSharedPreferences("systemConfig", Context.MODE_PRIVATE);
            LOGS_ENABLED = sharedPreferences.getBoolean("logsEnabled", DEBUG_VERSION);
        }
    }
}