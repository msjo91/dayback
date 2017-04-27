import argparse
import os
import sys

# Const
MODE_BASE = 'base'
MODE_DEBUG = 'debug'
MODE_PRODUCTION = 'production'
IMAGE_BASE = 'front-base'
IMAGE_DEBUG = 'front-debug'
IMAGE_PRODUCTION = 'front'
MAINTAINER = 'msjo91@gmail.com'
DOCKERFILE_BASE = 'Dockerfile.base'
DOCKERFILE_DEBUG = 'Dockerfile.debug'
DOCKERFILE_PRODUCTION = 'Dockerfile'

# ArgumentParser
parser = argparse.ArgumentParser(description='Build command')
parser.add_argument('-m', '--mode', type=str, default=MODE_PRODUCTION)
args = parser.parse_args()

# Paths
ROOT_DIR = os.path.dirname(__file__)
CONF_DIR = os.path.join(ROOT_DIR, '.conf')
CONF_DOCKER_DIR = os.path.join(CONF_DIR, 'docker')

# Docker conf files
dockerfile_template = open(os.path.join(CONF_DOCKER_DIR, '00_template.docker')).read()
dockerfile_base = open(os.path.join(CONF_DOCKER_DIR, '01_base.docker')).read()
dockerfile_extra = open(os.path.join(CONF_DOCKER_DIR, '02_extra.docker')).read()

if args.mode == MODE_BASE:
    dockerfile = dockerfile_template.format(
        from_image='ubuntu:16.04',
        maintainer=MAINTAINER,
        base=dockerfile_base,
        extra=''
    )
    filename = DOCKERFILE_BASE
elif args.mode == MODE_DEBUG:
    dockerfile = dockerfile_template.format(
        from_image=IMAGE_BASE,
        maintainer=MAINTAINER,
        base='',
        extra=dockerfile_extra
    )
    filename = DOCKERFILE_DEBUG
elif args.mode == MODE_PRODUCTION:
    dockerfile = dockerfile_template.format(
        from_image='ubuntu:16.04',
        maintainer=MAINTAINER,
        base=dockerfile_base,
        extra=dockerfile_extra
    )
    filename = DOCKERFILE_PRODUCTION
else:
    sys.exit('Mode Invalid')

with open(os.path.join(ROOT_DIR, filename), 'wt') as f:
    f.write(dockerfile)
