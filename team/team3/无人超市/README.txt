[视频链接](https://www.bilibili.com/video/BV17p4y1S7Qj)
本项目基于mc实现，服务器47.100.46.95：25583，坐标（41，0，83）
把多功能自助收银机文件夹下的代码复制出来，运行mc_all.py程序即可
如果不结合mc，只需要把代码中与mc有关内容注释掉即可

world
我的世界地图，可以下载到本地

py文件介绍
face.py		人脸识别，单独运行时调用相应函数即可
mc_all.py	所有内容与mc的结合
mqtt_ha.py	HA端通过MQTT接受数据
Roomba.py	清洁机器人
turning.py	导购机器人，单独运行调用main函数即可

多功能自助收银机
收银系统_终.py	单独运行需注释掉180、181行的mqtt和短信
需要导入素材中的收银表.sql

外卖配送
window.py	外卖下单界面
外卖配送.py	VTK机械手仿真，单独运行将最后mc相关内容注释即可

ha
将ha文件夹下的内容复制到本地的位置
C:\Users\用户名\AppData\Roaming\.homeassistant
记得改文件中相应的路径位置。
需要更改配置文件中的IP摄像头的端口
需要导入素材中的goods.sql
命令行输入hass --open-ui启动HA，配置UI卡片。
运行mqtt_ha.py接受数据

素材
有数据库的安装包，消费记录数据库以及货物信息数据库，导入数据库即可使用
图片文件夹中提供测试代码使用的物品条形码和支付和美团的二维码

