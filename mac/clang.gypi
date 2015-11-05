{
  'conditions': [['OS == "mac"', {'target_defaults': {
    'variables': {
      'clang_dir_mac%': '/usr/local/opt/clang+llvm',
    },
    'include_dirs': [
      '<(clang_dir_mac)/include',
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
        'libclang.dylib',
        'libclang.a',
        'libclangAnalysis.a',
        'libclangARCMigrate.a',
        'libclangAST.a',
        'libclangASTMatchers.a',
        'libclangBasic.a',
        'libclangCodeGen.a',
        'libclangDriver.a',
        'libclangEdit.a',
        'libclangFrontend.a',
        'libclangFrontendTool.a',
        'libclangIndex.a',
        'libclangParse.a',
        'libclangLex.a',
        'libclangRewrite.a',
        'libclangRewriteFrontend.a',
        'libclangSema.a',
        'libclangSerialization.a',
        'libclangStaticAnalyzerCheckers.a',
        'libclangStaticAnalyzerCore.a',
        'libclangStaticAnalyzerFrontend.a',
        'libclangTooling.a',
        'libclangToolingCore.a',
      ],
    },
  }}]],
}
