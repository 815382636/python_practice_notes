#python模块化

#绝对路径与相对路径
#在 Linux 系统中，每个文件都有一个绝对路径，以 / 开头，来表示从根目录到叶子节点的路径，
# 例如 /home/ubuntu/Desktop/my_project/test.py，这种表示方法叫作绝对路径。
# 另外，对于任意两个文件，我们都有一条通路可以从一个文件走到另一个文件，
# 例如 /home/ubuntu/Downloads/example.json。
# 再如，我们从 test.py 访问到 example.json，需要写成 '../../Downloads/example.json'，其中 .. 表示上一层目录。这种表示方法，叫作相对路径。
# 通常，一个 Python 文件在运行的时候，都会有一个运行时位置，最开始时即为这个文件所在的文件夹。

#相对位置是一种很不好的选择。因为代码可能会迁移，相对位置会使得重构既不雅观，也易出错。
# 因此，在大型工程中尽可能使用绝对位置是第一要义。
# 对于一个独立的项目，所有的模块的追寻方式，最好从项目的根目录开始追溯，这叫做相对的绝对路径。

#因此通过import进行引用时，直接从根目录往下一级一级引用（pycharm 运行环境默认import先从根目录查找文件，普通的python运行环境需修改venv中activate文件）
#最后一行写入： export PYTHONPATH="/home/ubuntu/workspace/your_projects"





