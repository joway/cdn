# /bin/bash
find ./images -mindepth 1 -maxdepth 1 -type f -name '*.png' -o -name '*.jp*g' | xargs -L1 ./compress-images.sh
