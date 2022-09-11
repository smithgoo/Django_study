# 20220911 python-Django项目Test
    
    #环境安装
    ```
        1.安装python,2.x不再维护建议安装3.x https://www.python.org/downloads/
        2.安装pip3 
        3.安装mysql8.0.30
        4.安装Django pip3 install Django
        5.安装pymysql pycharm 内部安装 或者本身python 环境全局安装
        6.navicat premium 安装 可视化界面操作数据库
    ```
    
    #文件认识 通过 Django startproject <项目名> 例如项目名==djangoDemo
    ```
        项目名目录下
        asgi,wsgi py文件是后面上线配置并发请求服务器的
        setting py文件 是设置相关设置 数据库 本地图片 静态网页文件目录 模版时区等
        urls 再里面添加路由规则文件
        新建一个templates文件 如果有就不新建 里面专门存放html 文件 前端页面
        新建一个statics文件夹里面再新建4个文件夹 分别是css images , js ,plugins(这个里面放bootstrap 文件夹用来引用三方样式文件https://v3.bootcss.com/getting-started/#download)
        
    ```
    #数据库操作
    ```
        1.利用navicat premium测试数据库的连通性
        2.再setting.py文件里面修改数据库连接文件配置
                DATABASES = {
            'default': {
                # 'ENGINE': 'django.db.backends.sqlite3',
                # 'NAME': BASE_DIR / 'db.sqlite3',
                'ENGINE': 'django.db.backends.mysql',
                'NAME': '',
                'HOST': '127.0.0.1',
                'PORT': '3306',
                'USER': 'root',
                'PASSWORD':'',
            }
        }
        3.再__init__.py文件里面添加
            import pymysql
            pymysql.install_as_MySQLdb()
        4.django-admin startapp <模型名称>
            settings.py-> INSTALLED_APPS 添加模型名称
        5.执行三个命令
            1.python3 manage.py migrate
            1. python3 manage.py makemigrations
            2. python3 manage.py makemigrations 模型名称
            4.用navicat premium 查看是否有新增数据库形成 有说明成功
        6.再urls.py里面添加路由文件
            1.新建一个views.py编写逻辑文件
            2.例如path(r'index/add$',views.add),
            3.runserver 查看是否正确
        7.第5步 已经形成了python 和mysql的映射文件
                1.test = Test(name=name,age=age);test.save()
                2.list = Test.objects.all();
                3.list = Test.objects.get(id = id)
                4.list = Test.objects.get(id = id);list.name = name;list.save()
                5.list = Test.objects.get(id=id);list.delete()

    ```
    