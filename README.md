Download-androidSource-python
=============================

download android source python shell 下载android源码的脚本，因为官方方法发现下载有各种问题，可以自己pull一下就行了


步骤

1. 访问地址 https://android.googlesource.com/?format=json  下载android源码对应文件夹的json文本  【注意，我现在下载的时候(2014年10月30日)第一行是错误的，把第一行删除掉】 保存名字为googlesource.json
2. 修改download_android_source.py  里面的变量 dirName为你要保存的源码路径
3. 指定对应的tag_name为你需要下载的git tag名字
4. 运行脚本即可


