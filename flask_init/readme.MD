## 一键构建flask框架

命令: `python3 start.py project_name`

会生成以`project_name`为名的项目文件夹, 并生成相关项目文件.

## 说明
需要下载`pip install python-dotenv`, 才能在使用`flask run`或其他命令时会使用它自动从`.flaskenv`文件和`.env`文件中加载环境变量.


`.flaskenv` 存储公开的环境变量,比如FLASK_APP
`.env`用来存储包含敏感信息的环境变量,比如email的账户和密码

在`.flaskenv` 和`.env`中环境变量使用键值对的形式定义,每行一个,以`#`开头的为注释.

> 　.env包含敏感信息，除非是私有项目，否则绝对不能提交到Git仓库中。开发一个新项目时，把它的名称添加到.gitignore文件中