# 使用方法<br>
一些字幕翻译软件很不错，但是要收费，就自己写了个小脚本。一个调用百度API的字幕翻译小脚本<br>
环境：win10 x64 ; python 3.8.5<br>
保证translater.py和字幕文件在同一个文件夹内，脚本会自动侦测所有srt格式的文件，翻译完成后会自动在当前目录下新建文件夹subtitle_translaed，结果储存在这个文件夹里面，文件名与源字幕名相同。打开命令行，进入脚本所在文件，输入python translater.py，如图<br>
![](images/image2.PNG)<br>
运行结果如图<br>
![](images/image.PNG)<br>
注意三个地方：APIID secretKey QPS，这些可以从百度翻译开放平台自己获取，免费的QPS是1，如果太快会请求失败，脚本没有加入请求失败的处理方法，所以一定保证QPS正确。<br>
使用愉快<br>
