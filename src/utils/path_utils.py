# src/utils/path_utils.py
import os

def get_src_dir():
    """获取src根目录（当前运行路径）"""
    current_path = os.path.abspath(__file__)
    # 回退到src目录（utils是src的子目录）
    src_dir = os.path.abspath(os.path.join(current_path, "../"))
    return src_dir

def get_target_dir(sub_dir):
    """
    获取目标子目录（基于src）
    :param sub_dir: 相对src的子目录，如 "algorithm/DQN_structure/network_picture"
    :return: 目标目录绝对路径
    """
    src_dir = get_src_dir()
    target_dir = os.path.join(src_dir, sub_dir)
    # 确保目录存在
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    return target_dir