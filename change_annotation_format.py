import os
import cv2

cwd = os.getcwd()
path = cwd+'/data/eval_images'
dir_out = cwd+'/data/dataset'

for root, dirs, files in os.walk(path, topdown=True):
    # print(f'root: {root}\ndirs: {dirs}')

    file_bin = []

    for file in files:
        fname_no_ext = os.path.splitext(file)[0]
        file_ext = os.path.splitext(file)[1]
        # print(f'file: \t\t{file}')
        # print(f'fname_no_ext: \t{fname_no_ext}')
        # print(f'file_ext: \t{file_ext}')

        if file_ext != '.txt':
            # print('==>Not a text file')
            file_bin.append([file, fname_no_ext + '.txt'])
        # print('\n')


    # print(f'\nFile Bin:')
    # print(file_bin)
    # print(f'Length of file bin = {len(file_bin)}')
    # print('\n')

    total_list = []

    for pair in file_bin:
        img_path = '/opt/project/data/eval_images/'+pair[0]
        line_str = '/opt/project/data/eval_images/'+pair[0]
        # print(pair)
        # print(f'img_path = {img_path}')
        text_path = '/opt/project/data/eval_images/'+pair[1]
        # print(text_path,'\n')

        img = cv2.imread(img_path)
        # print(img)
        # print(f'img_type = {img.type}')
        h,w,c = img.shape
        # print(f'h = {h}, w = {w}')

        with open(text_path) as f:
            lines = f.readlines()
            for line in lines:
                # print(line)
                line_list = line.split(' ')
                # print(line_list)
                line_list[-1] = line_list[-1][:-1]
                # print(line_list)
                line_list.append(line_list.pop(0))
                # print(line_list)
                line_list = [float(x) for x in line_list]
                # print(line_list)


                x_center = w * line_list[0]
                y_center = h * line_list[1]
                w_box    = w * line_list[2]
                h_box    = h * line_list[3]

                line_list[0] = x_center - w_box/2
                line_list[1] = y_center - h_box/2
                line_list[2] = x_center + w_box/2
                line_list[3] = y_center + h_box/2


                # print(line_list)
                line_list = [round(x) for x in line_list]
                # print(line_list)
                line_list = [str(x) for x in line_list]
                # print(line_list)
                new_str = ' '+ ','.join(line_list)
                # print(new_str)

                line_str += new_str
                # break

            # print(f'\n\nline_str = {line_str}')
            total_list.append(line_str)
        # break # test one .txt file for now

    # print(f'\n\nlength of total_list = {len(total_list)}')
    # print(total_list,'\n')
    # for line in total_list:
    #     print(line)

    with open('/opt/project/data/dataset/valcustom.txt','w') as outfile:
        outfile.write("\n".join(str(item) for item in total_list))
