# Django系统
- 环境
    - python3.6
    - django1.8
- 参考资料
    - [django中文教程](http://python.yiyibooks.cn/)
    - django架站的16堂课
# 环境搭建
- anaconda+pycharm
- anaconda使用
    - conda list：显示当前环境安装的包
    - conda env list: 显示的安装的虚拟环境列表
    - conda create -n env_name python=3.6
    - 激活conda的虚拟环境
        - (Linux)source activate env_name
        - (win) activate env_name\
    - pip install django==1.8
# 后台需要的流程

# 创建第一个django程序
- 命令行启动

        django-admin startproject my_django
        cd my_django
        python manage.py runserver
        
- pycharm 启动
    - 需要配置
    
# 路由系统-urls
- 创建app
    - app：负责一个具体业务或者一类具体业务的模块
    - python manage.py startapp teacher

- 路由
    - 按照具体的请求url，导入到相应的业务处理模块的一个功能模块
    - django的信息控制中枢
    - 本质上是接收的URL和相应的处理模块的一个映射
    - 在接收URL请求的匹配上使用了RE
    - URL的具体格式如urls.py中所示