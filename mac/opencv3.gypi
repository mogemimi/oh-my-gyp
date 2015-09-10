{
  'conditions': [['OS == "mac"', {'target_defaults': {
    'variables': {
      'opencv3_dir_mac': '/usr/local/Cellar/opencv3/3.0.0',
    },
    'include_dirs': [
      '<(opencv3_dir_mac)/include',
    ],
    'link_settings': {
      'libraries': [
        '<(opencv3_dir_mac)/lib/libopencv_core.dylib',
        '<(opencv3_dir_mac)/lib/libopencv_highgui.dylib',
        '<(opencv3_dir_mac)/lib/libopencv_imgcodecs.dylib',
        #'<(opencv3_dir_mac)/lib/libopencv_features2d.dylib',
      ],
    },
  }}]],
}
