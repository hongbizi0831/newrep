import os
import shutil


def copy_files_if_not_exists(src_folder, dest_folder):
    """
    遍历src_folder内的所有子文件夹和子文件，
    如果目标文件夹dest_folder内不存在相同的文件或文件夹，则复制过去。
    """
    
    print("modified ...")
    
    # 确保目标文件夹存在
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    # 遍历源文件夹
    for root, dirs, files in os.walk(src_folder):
        # 计算相对路径
        rel_path = os.path.relpath(root, src_folder)
        dest_root = os.path.join(dest_folder, rel_path)

        # 创建目标文件夹
        if not os.path.exists(dest_root):
            os.makedirs(dest_root)

        # 处理文件
        for file in files:
            src_file = os.path.join(root, file)
            dest_file = os.path.join(dest_root, file)

            # 如果目标文件不存在，则复制
            if not os.path.exists(dest_file):
                shutil.copy2(src_file, dest_file)

        # 处理子文件夹
        for dir in dirs:
            src_dir = os.path.join(root, dir)
            dest_dir = os.path.join(dest_root, dir)

            # 如果目标文件夹不存在，则递归处理
            if not os.path.exists(dest_dir):
                shutil.copytree(src_dir, dest_dir)


def merge_panosimdatabase(src_folder, dest_folder):
    """
    遍历src_folder，如果找到名为PanoSimDatabase的子文件夹，
    则将其所有内容合并到dest_folder中。
    """
    # 确保目标文件夹存在
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    # 遍历源文件夹
    for root, dirs, files in os.walk(src_folder):
        # 检查当前目录是否为PanoSimDatabase
        if 'PanoSimDatabase' in dirs:
            pano_path = os.path.join(root, 'PanoSimDatabase')
            # 合并PanoSimDatabase的内容到目标文件夹
            copy_files_if_not_exists(pano_path, dest_folder)


# 使用示例
source_folder = r'G:/V33.27/PanoSim_How_To-main'
target_folder = r'G:/V33.27/PanoSimDatabase'
folder_name = 'PanoSimDatabase'
merge_panosimdatabase(source_folder, target_folder)