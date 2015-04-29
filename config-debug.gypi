{
  'target_defaults': {
    'configurations': {
      'Debug': {
        'defines': ['DEBUG=1'],
        'cflags': ['-g', '-O0'],
        'msbuild_settings': {
          'ClCompile': {
            'Optimization': 'Disabled', # /Od
            'RuntimeLibrary': 'MultiThreadedDebug', # /MTd
          },
          'Link': {
            #'LinkIncremental': 'true', # /INCREMENTAL
            'GenerateDebugInformation': 'true', # /DEBUG
          },
        },
        'xcode_settings': {
          'OTHER_CFLAGS': ['-g'],
          'GCC_OPTIMIZATION_LEVEL': '0', # -O0
        },
      },
    },
  },
}
