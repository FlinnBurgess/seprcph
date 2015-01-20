import glob
from cx_Freeze import setup, Executable

# If we don't include SDL then pygame will be a bitch.
sdl_includes = glob.glob('/usr/lib/libSDL*')

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = ['pygame'], excludes = [],
        include_files = ['assets/images/', 'data/'],
        bin_includes=sdl_includes)

base = 'Console'

executables = [
    Executable('seprcph/main.py', base=base, targetName = 'seprcph')
]

setup(name='seprcph',
      version = '1.0',
      description = 'Trains across Europe',
      options = dict(build_exe = buildOptions),
      executables = executables)
