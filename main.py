# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import os
import re
def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。

def read_cwd_filname(suffixname):
    import_flv_dict = {}
    g = os.walk(".")
    for path, dir_list, file_list in g:
        for file_name in file_list:
            # if os.path.splitext(file_name)[-1] == '.flv':
            if os.path.splitext(file_name)[-1] == suffixname:
                import_flv_dict[file_name] = os.path.join(path,file_name)
    return import_flv_dict
# 按间距中的绿色按钮以运行脚本。

def flv_deal():
    flv_dict = read_cwd_filname('.flv')
    # print(flv_dict)
    for key, value in flv_dict.items():
        # filename = key.split[:-1]
        str = 'ffmpeg-normalize '+ value +' -o edited_'+key + ' -pr'
        # print(str)
        os.system(str)
    # os.system('')

if __name__ == '__main__':
    flv_deal()
    print_hi('PyCharm')

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
