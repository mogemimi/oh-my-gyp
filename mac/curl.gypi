{
  'conditions': [['OS == "mac"', {'target_defaults': {
    'link_settings': {
      'libraries': [
        '$(SDKROOT)/usr/lib/libcurl.dylib'
      ],
    },
  }}]],
}
