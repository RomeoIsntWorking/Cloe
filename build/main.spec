# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_data_files
from PyInstaller.utils.hooks import copy_metadata

datas = []
datas += collect_data_files('unidic_lite')
datas += collect_data_files('manga_ocr')
datas += collect_data_files('transformers')
datas += collect_data_files('huggingface_hub')
datas += copy_metadata('tqdm')
datas += copy_metadata('regex')
datas += copy_metadata('requests')
datas += copy_metadata('packaging')
datas += copy_metadata('filelock')
datas += copy_metadata('numpy')
datas += copy_metadata('tokenizers')
datas += copy_metadata('transformers')
datas += copy_metadata('huggingface_hub')
datas += copy_metadata('manga_ocr')

local_files = [
  ('../app/assets', './assets')
]

block_cipher = None

a = Analysis(['../app/main.py'],
             pathex=['../app'],
             binaries=[],
             datas=datas+local_files,
             hiddenimports=[
              'pynput.keyboard._xorg',
              'pynput.mouse._xorg',
              'pynput.keyboard._win32',
              'pynput.mouse._win32',
              'transformers',
              'transformers.models',
              'transformers.models.auto',
              'manga_ocr',
              'huggingface_hub',
              'torch',
              'tokenizers'
            ],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

PATH_TO_TORCH_LIB = "torch\\lib\\"
excluded_files  = [
  'asmjit.lib',
  'c10.lib',
  'clog.lib',
  'cpuinfo.lib',
  'dnnl.lib',
  'caffe2_detectron_ops.dll',
  'caffe2_detectron_ops.lib',
  'caffe2_module_test_dynamic.dll',
  'caffe2_module_test_dynamic.lib',
  'caffe2_observers.dll',
  'caffe2_observers.lib',
  'Caffe2_perfkernels_avx.lib',
  'Caffe2_perfkernels_avx2.lib',
  'Caffe2_perfkernels_avx512.lib',
  'fbgemm.lib',
  'kineto.lib',
  'libprotobuf-lite.lib',
  'libprotobuf.lib',
  'libprotoc.lib',
  'mkldnn.lib',
  'pthreadpool.lib',
  'shm.lib',
  'torch.lib',
  'torch_cpu.lib',
  'torch_python.lib',
  'XNNPACK.lib',
  '_C.lib'
]
excluded_files = [PATH_TO_TORCH_LIB + x for x in excluded_files]
a.datas = [x for x in a.datas if not x[0] in excluded_files]

exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='Cloe',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None,
          icon="../app/assets/images/icons/logo.ico")

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='app')