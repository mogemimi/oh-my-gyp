{
  'target_defaults': {
    'msbuild_settings': {
      'ClCompile': {
        'PreprocessorDefinitions': [
          '_WIN32_WINNT=0x0601', # Windows 7 or later
          'WIN32_LEAN_AND_MEAN',
          'NOMINMAX',
        ],
      },
    },
  },
}
