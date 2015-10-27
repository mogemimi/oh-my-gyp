{
  'conditions': [['OS == "mac"', {'target_defaults': {
    'variables': {
      'libgit2_dir_mac': '/usr/local/opt/libgit2',
    },
    'include_dirs': [
      '<(libgit2_dir_mac)/include',
    ],
    'link_settings': {
      'libraries': [
        '<(libgit2_dir_mac)/lib/libgit2.dylib',
      ],
    },
  }}]],
}
