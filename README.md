# VGG

## Project Directory Structure

- `./`: project root
  - `/script`: useful scripts
  - `/src`: source code
  - `/data`: training and testing dataset
    - `/JPEGImages`
    - `/labels`
  - `/label`: label for training
  - `/dest`: output (if any)
    - `/log`: log for tensorboard
    - `/param`: store check points
  - `/exchange`: exchange data between server and client
  - `/tmp`: store buffer files

## Dataset Structure

- `VOC2012`
  - `/ImageSets`: labels of 20 classes
    - `*_train.txt`: used to train model
    - `*_val.txt`: used to validate and evaluate trained model
    - `*_trainval.txt`: `*_train.txt` + `*_val.txt`
  - `/JPEGImages`: 17125 raw colorful images

- ps. `.txt` format:
  - for valid images: `id_of_imgs  1` per line
  - for invalid images: `id_of_imgs -1` per line
