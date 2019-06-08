# SAMDrawer

绘制字符串的后缀自动机

[后缀自动机简介](https://oi-wiki.org/string/sam/)

## 环境依赖

请按照指示安装Flask与Graphviz，在此之前需先安装pip

## 部署

本项目使用Flask部署。

```bash
git clone https://github.com/keepthethink/SAMDrawer.git --depth=1

cd SAMDrawer

# 如果失败，先安装pip
pip3 install falsk
pip3 install graphviz

sudo apt-get install graphviz #macOS或Windows替换为用其他方法安装graphviz

# 访问 http://127.0.0.1:90 查看效果
sudo python3 main.py
```

### 安装依赖项

Flask:
```bash
pip3 install falsk
```

Graphviz:
```bash
sudo apt-get install graphviz
pip3 install graphviz
```

### 运行

```bash
# 类UNIX系统需要ROOT权限才能使用原始套接字(Raw Socket)
sudo python3 main.py
```

## 效果

![Jietu20190608-105220@2x.jpg](https://i.loli.net/2019/06/08/5cfb234837eba96917.jpg)

## LICENSE

MIT
