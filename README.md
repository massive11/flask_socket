# flask_socket
毕设项目客户端，与EAIDK进行socket通信

主要开发工具为Flask + Ajax + Mysql

项目采用Flask框架搭建，server.py为与EAIDK进行socket通信的socket服务器端，单独进行执行

## 主要功能
1.提供用户的注册、登录、修改密码功能

2.提供人脸识别系统的实时监控功能（页面上显示接收到的实时数据）

3.提供管理员登录、修改密码、管理用户的功能


## 项目运行
修改config.py中的数据库配置

安装依赖

```bash
pip install -r requirements.txt
```

初始化和创建migration文件

```bash
python app.py db init
python app.py db migrate
```

建表

```bash
python app.py db upgrade
```


启动服务器

```bash
python app.py runserver
```

(运行server.py，修改IP、Port)