"""Training and Testing configurations."""


class Config(object):
    """Config."""

    # util
    batch_size = 50
    initialize = True
    steps = '-1'
    gpu = '/gpu:0'

    # training config
    class_num = 20

    # checkpoint path and filename
    logdir = './dest/log/'
    params_dir = './dest/params/'
    load_filename = 'vgg' + '-' + steps
    save_filename = 'vgg'

    # buffer
    buff_path = './tmp/'
    buff_tl_name = 'label_train.txt'

    # iterations config
    max_iteration = 100000
    checkpoint_iters = 2000
    summary_iters = 100
    validate_iters = 2000

    # image config
    channel_num = 3  # RGB
    origin_height = 212
    origin_width = 256
    img_height = 224  # img height for training
    img_width = 224   # img width for training
    is_color = True

    # random distortion
    degree = 15

    # solver config
    wd = 5e-4
    stddev = 5e-2
    use_fp16 = False
    moving_average_decay = 0.999

    # and others
    use_fp16 = False

    def __init__(self, test=False, step='2000'):
        """Initializer."""
        if test:
            self.batch_size = 1
            self.initialize = False
            self.steps = step
