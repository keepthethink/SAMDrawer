# SAMDrawer

[![license](https://img.shields.io/github/license/keepthethink/SAMDrawer.svg)](https://github.com/keepthethink/SAMDrawer/blob/master/LICENSE)
[![author](https://img.shields.io/badge/Author-Helium-blue.svg)](https://github.com/keepthethink/)

绘制字符串的后缀自动机

[后缀自动机简介](https://oi-wiki.org/string/sam/)

## 环境要求

* macOS or Linux or Windows
* python (3.7+)
* pip3
* Graphviz

## 依赖包

[![flask](https://img.shields.io/pypi/v/flask.svg?label=flask)](https://pypi.org/project/flask/)
[![graphviz](https://img.shields.io/pypi/v/graphviz.svg?label=graphviz)](https://pypi.org/project/graphviz/)

## 部署

本项目使用Flask部署。

```bash
git clone https://github.com/keepthethink/SAMDrawer.git --depth=1

cd SAMDrawer

# 如果失败，先安装pip
pip3 install -r requirements.txt

sudo apt-get install graphviz #macOS或Windows替换为用其他方法安装graphviz

# 访问 http://127.0.0.1:90 查看效果
sudo python3 main.py
```

### 安装依赖项

Python Module:
```bash
$ pip3 install -r requirements.txt
```

Graphviz:
```bash
$ sudo apt-get install graphviz
```

### 运行

```bash
# 类UNIX系统需要ROOT权限才能使用原始套接字(Raw Socket)
$ sudo python3 main.py
```
访问 <http://127.0.0.1:90> 查看效果

## 效果

![Jietu20190608-105220@2x.jpg](https://i.loli.net/2019/06/08/5cfb234837eba96917.jpg)

## 目录结构

```
SAMDrawer
--docs\
----README_en.md
--static\
----jquery-3.3.1.js
----vue.js
----semantic.css
----semantic.js
--templates\
----base.html
----main.html
--.gitattributes
--.gitignore
--_config.yml
--ds_drawer.py
--LICENSE
--main.py
--README.md
--requirements.txt
```

## LICENSE

MIT
