{
  'target_defaults': {
    'msbuild_settings':{
      'ClCompile': {
        'TreatWarningAsError': 'true', # /WX
      },
    },
    'xcode_settings': {
      'GCC_TREAT_WARNINGS_AS_ERRORS': 'YES',
    },
  },
}
