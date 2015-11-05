{
  'conditions': [['OS == "mac"', {'target_defaults': {
    'variables': {
      'clang_dir_mac%': '/usr/local/opt/clang+llvm',
    },
    'include_dirs': [
      '<(clang_dir_mac)/include',
    ],
    'defines': [
        '__STDC_CONSTANT_MACROS',
        '__STDC_LIMIT_MACROS',
        #'__STDC_FORMAT_MACROS',
    ],
    'xcode_settings': {
      'LIBRARY_SEARCH_PATHS': [
        '<(clang_dir_mac)/lib',
      ],
      'OTHER_CPLUSPLUSFLAGS': [
          '-fno-exceptions',
          '-fno-rtti',
      ],
    },
    'link_settings': {
      'libraries': [
        'libLLVMCore.a',
        'libLLVMOption.a',
        'libLLVMSupport.a',
        'libLLVMMCParser.a',
        'libLLVMBitReader.a',
        'libLLVMMC.a',
        'libclang.dylib',
        'libclang.a',
        'libclangAnalysis.a',
        'libclangAST.a',
        'libclangASTMatchers.a',
        'libclangBasic.a',
        'libclangDriver.a',
        'libclangEdit.a',
        'libclangFrontend.a',
        'libclangParse.a',
        'libclangLex.a',
        'libclangRewrite.a',
        'libclangRewriteFrontend.a',
        'libclangSema.a',
        'libclangSerialization.a',
        'libclangTooling.a',

        '$(SDKROOT)/usr/lib/libz.a',
        '$(SDKROOT)/usr/lib/libpthread.a',
        '$(SDKROOT)/usr/lib/libedit.a',
        '$(SDKROOT)/usr/lib/libcurses.a',
        '$(SDKROOT)/usr/lib/libm.a',
        # '$(SDKROOT)/usr/lib/libz.tbd',
        # '$(SDKROOT)/usr/lib/libpthread.tbd',
        # '$(SDKROOT)/usr/lib/libedit.tbd',
        # '$(SDKROOT)/usr/lib/libcurses.tbd',
        # '$(SDKROOT)/usr/lib/libm.tbd',
      ],
    },
  }}]],
}
