{
  'target_defaults': {
    'configurations': {
      'Release': {
        'defines': ['NDEBUG=1'],
        'cflags': ['-O3'],
        'msbuild_settings':{
          'ClCompile': {
            'Optimization': 'MaxSpeed', # /O2
            'InlineFunctionExpansion': 'AnySuitable', # /Ob2
            'RuntimeLibrary': 'MultiThreaded', # /MT
          },
          'Link': {
            #'LinkIncremental': 'false', # /INCREMENTAL:NO
            'OptimizeReferences': 'true', # /OPT:REF
          },
        },
        'xcode_settings': {
          'GCC_OPTIMIZATION_LEVEL': '3', # -O3
        },
      },
    },
  },
}
