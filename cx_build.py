import platform
from cx_Freeze import setup, Executable

if platform == 'Windows':
    bin_inc = 'C:\\Python27\\Lib\\site-packages\\pygame'
else:
    bin_inc = '/usr/lib'

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = ['pygame'], excludes = [],
        include_files = ['assets/images/', 'data/'],
        bin_path_includes=bin_inc)

base = 'Console'

executables = [
    Executable('seprcph/main.py', base=base, targetName = 'seprcph')
]

setup(name='seprcph',
      version = '1.0',
      description = 'Trains across Europe',
      options = dict(build_exe = buildOptions),
      executables = executables)
