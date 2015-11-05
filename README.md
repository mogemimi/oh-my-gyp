Oh My GYP
=========

Oh My GYP is a set of simply [GYP (Generate Your Projects)](https://code.google.com/p/gyp/) configuration files to help build settings for C/C++ applications, released into the public domain.

## Getting started

First, make your project directory, and clone 'oh-my-gyp' from GitHub.

```shell
mkdir hello && cd hello
git clone https://github.com/mogemimi/oh-my-gyp.git
```

Second, add `main.cpp` and `hello.gyp` to your project directory.
For example,

```
hello/
├── oh-my-gyp/
│   ├── c++11.gypi
│   ├── c++14.gypi
│   └── ...
├── hello.gyp
└── main.cpp
```

`main.cpp`:

```cpp
#include <iostream>

int main()
{
    std::cout << "hello" << std::endl;
    return 0;
}
```

`hello.gyp`:

```python
{
  # (1) choose your build configs
  'includes': [
    'oh-my-gyp/c++14.gypi',
    'oh-my-gyp/config-debug-release.gypi',
    'oh-my-gyp/warn-as-error.gypi',
    'oh-my-gyp/warnings-level3.gypi',
    'oh-my-gyp/mac-basic.gypi',
    'oh-my-gyp/win32-basic.gypi',
  ],
  # (2) write your build target
  'targets': [
    {
      'target_name': 'Hello',
      'product_name': 'Hello',
      'type': 'executable',
      'sources': [
        'main.cpp',
      ],
    },
  ],
}
```

### Generating Xcode project

To generate `.xcodeproj` file, run the following command:

```shell
gyp hello.gyp --depth=. -f xcode
```

To open in Xcode, run the following into terminal:

```shell
open hello.xcodeproj
```

### Generating Visual Studio 2015 project

To generate `.sln` and `.vcxproj` files, run the following command:

```shell
gyp hello.gyp --depth=. -f msvs -G msvs_version=2015
```

You can try to compile `hello.sln` in Visual Studio 2015.
