# SAMDrawer

[![license](https://img.shields.io/github/license/keepthethink/SAMDrawer.svg)](https://github.com/keepthethink/SAMDrawer/blob/master/LICENSE)
[![author](https://img.shields.io/badge/Author-Helium-blue.svg)](https://github.com/keepthethink/)

Suffix automaton for drawing strings

[Introduction to SAM](https://oi-wiki.org/string/sam/)

## Environmental requirements

* macOS or Linux or Windows
* python (3.7+)
* pip3
* Graphviz

## Dependency package

[![flask](https://img.shields.io/pypi/v/flask.svg?label=flask)](https://pypi.org/project/flask/)
[![graphviz](https://img.shields.io/pypi/v/graphviz.svg?label=graphviz)](https://pypi.org/project/graphviz/)

## Deployment

This project uses a Flask deployment.

```bash
git clone https://github.com/keepthethink/SAMDrawer.git --depth=1

Cd SAMDrawer

# If it fails, install pip first.
pip3 install -r requirements.txt

sudo apt-get install graphviz #macOS or Windows replaced with other methods to install graphviz

# Visit http://127.0.0.1:90 to see the effect
sudo python3 main.py
```

### Installing dependencies

Python Module:
```bash
$ pip3 install -r requirements.txt
```

Graphviz:
```bash
$ sudo apt-get install graphviz
```

### Running

```bash
# UNIX system requires ROOT permission to use raw socket (Raw Socket)
$ sudo python3 main.py
```
Visit <http://127.0.0.1:90> to see the effect

## Effect

![Jietu20190608-105220@2x.jpg](https://i.loli.net/2019/06/08/5cfb234837eba96917.jpg)

## Directory Structure

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
--Dockerfile
```

## LICENSE

MIT
