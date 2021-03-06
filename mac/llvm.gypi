{
  'conditions': [['OS == "mac"', {'target_defaults': {
    'variables': {
      'llvm_dir_mac%': '/usr/local/opt/llvm',
    },
    'defines': [
        '__STDC_CONSTANT_MACROS',
        '__STDC_LIMIT_MACROS',
        #'__STDC_FORMAT_MACROS',
    ],
    'include_dirs': [
      '<(llvm_dir_mac)/include',
    ],
    'xcode_settings': {
      'LIBRARY_SEARCH_PATHS': [
        '<(llvm_dir_mac)/lib',
      ],
    },
    'link_settings': {
      'libraries': [
        'libLLVMLTO.a',
        'libLLVMObjCARCOpts.a',
        'libLLVMLinker.a',
        'libLLVMBitWriter.a',
        'libLLVMIRReader.a',
        'libLLVMBPFCodeGen.a',
        'libLLVMBPFDesc.a',
        'libLLVMBPFInfo.a',
        'libLLVMBPFAsmPrinter.a',
        'libLLVMAMDGPUCodeGen.a',
        'libLLVMAMDGPUAsmParser.a',
        'libLLVMAMDGPUUtils.a',
        'libLLVMAMDGPUDesc.a',
        'libLLVMAMDGPUInfo.a',
        'libLLVMAMDGPUAsmPrinter.a',
        'libLLVMSystemZDisassembler.a',
        'libLLVMSystemZCodeGen.a',
        'libLLVMSystemZAsmParser.a',
        'libLLVMSystemZDesc.a',
        'libLLVMSystemZInfo.a',
        'libLLVMSystemZAsmPrinter.a',
        'libLLVMHexagonDisassembler.a',
        'libLLVMHexagonCodeGen.a',
        'libLLVMHexagonDesc.a',
        'libLLVMHexagonInfo.a',
        'libLLVMNVPTXCodeGen.a',
        'libLLVMNVPTXDesc.a',
        'libLLVMNVPTXInfo.a',
        'libLLVMNVPTXAsmPrinter.a',
        'libLLVMCppBackendCodeGen.a',
        'libLLVMCppBackendInfo.a',
        'libLLVMMSP430CodeGen.a',
        'libLLVMMSP430Desc.a',
        'libLLVMMSP430Info.a',
        'libLLVMMSP430AsmPrinter.a',
        'libLLVMXCoreDisassembler.a',
        'libLLVMXCoreCodeGen.a',
        'libLLVMXCoreDesc.a',
        'libLLVMXCoreInfo.a',
        'libLLVMXCoreAsmPrinter.a',
        'libLLVMMipsDisassembler.a',
        'libLLVMMipsCodeGen.a',
        'libLLVMMipsAsmParser.a',
        'libLLVMMipsDesc.a',
        'libLLVMMipsInfo.a',
        'libLLVMMipsAsmPrinter.a',
        'libLLVMAArch64Disassembler.a',
        'libLLVMAArch64CodeGen.a',
        'libLLVMAArch64AsmParser.a',
        'libLLVMAArch64Desc.a',
        'libLLVMAArch64Info.a',
        'libLLVMAArch64AsmPrinter.a',
        'libLLVMAArch64Utils.a',
        'libLLVMARMDisassembler.a',
        'libLLVMARMCodeGen.a',
        'libLLVMARMAsmParser.a',
        'libLLVMARMDesc.a',
        'libLLVMARMInfo.a',
        'libLLVMARMAsmPrinter.a',
        'libLLVMPowerPCDisassembler.a',
        'libLLVMPowerPCCodeGen.a',
        'libLLVMPowerPCAsmParser.a',
        'libLLVMPowerPCDesc.a',
        'libLLVMPowerPCInfo.a',
        'libLLVMPowerPCAsmPrinter.a',
        'libLLVMSparcDisassembler.a',
        'libLLVMSparcCodeGen.a',
        'libLLVMSparcAsmParser.a',
        'libLLVMSparcDesc.a',
        'libLLVMSparcInfo.a',
        'libLLVMSparcAsmPrinter.a',
        'libLLVMMIRParser.a',
        'libLLVMAsmParser.a',
        'libLLVMLibDriver.a',
        'libLLVMOption.a',
        'libLLVMDebugInfoPDB.a',
        'libLLVMTableGen.a',
        'libLLVMOrcJIT.a',
        'libLLVMLineEditor.a',
        'libLLVMX86Disassembler.a',
        'libLLVMX86AsmParser.a',
        'libLLVMX86CodeGen.a',
        'libLLVMSelectionDAG.a',
        'libLLVMAsmPrinter.a',
        'libLLVMX86Desc.a',
        'libLLVMMCDisassembler.a',
        'libLLVMX86Info.a',
        'libLLVMX86AsmPrinter.a',
        'libLLVMX86Utils.a',
        'libLLVMMCJIT.a',
        'libLLVMDebugInfoDWARF.a',
        'libLLVMPasses.a',
        'libLLVMipo.a',
        'libLLVMVectorize.a',
        'libLLVMInterpreter.a',
        'libLLVMExecutionEngine.a',
        'libLLVMRuntimeDyld.a',
        'libLLVMCodeGen.a',
        'libLLVMTarget.a',
        'libLLVMScalarOpts.a',
        'libLLVMProfileData.a',
        'libLLVMObject.a',
        'libLLVMMCParser.a',
        'libLLVMBitReader.a',
        'libLLVMInstCombine.a',
        'libLLVMInstrumentation.a',
        'libLLVMTransformUtils.a',
        'libLLVMipa.a',
        'libLLVMMC.a',
        'libLLVMAnalysis.a',
        'libLLVMCore.a',
        'libLLVMSupport.a',

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
