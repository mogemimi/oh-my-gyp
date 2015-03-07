{
  'target_defaults': {
    'xcode_settings': {
      'ONLY_ACTIVE_ARCH': 'YES',
      'MACOSX_DEPLOYMENT_TARGET': '10.9',
      'GCC_VERSION': 'com.apple.compilers.llvm.clang.1_0',
      'CLANG_ENABLE_OBJC_ARC': 'YES',
      'GCC_INLINES_ARE_PRIVATE_EXTERN': 'YES', # '-fvisibility-inlines-hidden'
      'GCC_SYMBOLS_PRIVATE_EXTERN': 'YES', # '-fvisibility=hidden'
    },
  },
}
