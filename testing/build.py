#!/usr/bin/python3
import build

build.main(__name__)


class Config(build.Config):
  # Put your options here
  # Defaults:
  # Default task
  default = 'build'
  # Languages to build (lang/<lang>.py)
  languages = []
  # Default output directory
  out = 'out'
  # Whether to preserve output paths (src/dir/file.py -> out/dir/file.py or out/file.py)
  preserve_paths = True
  # Enable builtin tasks (build etc.)
  builtins = True

