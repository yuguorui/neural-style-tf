#/usr/bin/env python3

from subprocess import run

convs = ['conv1_1', 'conv2_1', 'conv3_1', 'conv4_1', 'conv5_1']
run_str = 'python neural_style.py --content_img lion.jpg --content_img_dir image_input --style_imgs wave_crop.jpg --style_imgs_dir styles --device "/gpu:0" --img_name {} --style_layers {} --style_layer_weights {} --content_weight {}'

for alpha in [5e-1, 5, 5e1, 5e2, 5e3]:
    for i in range(len(convs)):
        run_command = run_str.format(f'{convs[i]}-{alpha}.png', f'{" ".join(convs[:i+1])}'," ".join([str(1/(i+1))] * (i+1)), alpha)
        print(run_command)
        run(run_command)