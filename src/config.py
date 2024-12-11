TINDER_API_BASE = "https://api.gotinder.com"

HEADERS = {
    'user-agent': "Tinder Android Version 12.6.0",
    'os-version': "25",
    'app-version': "4023",
    'platform': "android",
    'platform-variant': "Google-Play",
    'x-supported-image-formats': "webp",
    'accept-language': "en-US",
    'tinder-version': "12.6.0",
    'store-Variant': "Play-Store",
    'persistent-device-id': None,  # This should be dynamically assigned
    'content-type': "application/x-protobuf",
    'host': "api.gotinder.com",
    'connection': "close",
    'accept-encoding': "gzip,deflate, br",
    'install-id': None,            # This should be dynamically assigned
    'app-session-id': None,        # This should be dynamically assigned
    'funnel-session-id': None,     # This should be dynamically assigned
    'app-session-time-elapsed': "0.000"  # This should be dynamically updated
}

def update_headers(device_id, install_id, app_session_id, funnel_id, elapsed_time):
    """Dynamically update headers with session-specific data."""
    global HEADERS
    HEADERS.update({
        'persistent-device-id': device_id,
        'install-id': install_id,
        'app-session-id': app_session_id,
        'funnel-session-id': funnel_id,
        'app-session-time-elapsed': format(elapsed_time, ".3f")
    })
