import os
import sys
import mxnet as mx
import logging


def patch_path(path):
    return os.path.join(os.path.dirname(__file__), path)


def main():
    sys.path.append(patch_path('..'))

    logging.basicConfig(level=logging.DEBUG)

    model_dir_path = patch_path('models')
    ctx = mx.gpu(0)

    from mxnet_text_to_image.library.dcgan2 import DCGan
    from mxnet_text_to_image.data.flowers_texts import load_texts

    gan = DCGan(model_ctx=ctx)
    gan.load_glove(glove_dir_path=patch_path('data/glove'))
    gan.load_model(model_dir_path=model_dir_path)

    texts = load_texts(patch_path('data/flowers/text_c10'), 300)
    for i, (image_id, lines) in enumerate(texts.items()):
        for j, line in enumerate(lines[:1]):
            print(line)
            gan.generate(text_message=line, output_dir_path=patch_path('output'), filename=str(i) + '-' + str(j) + '.png')


if __name__ == '__main__':
    main()
