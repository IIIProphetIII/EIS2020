# EIS2020
Embedded and Intelligent Systems (EIS) course for SHIEP 2020

# 20200323作业
1. 学习M02 M06 ppt  
2. students目录下创建自己的文件夹  
3. 我的世界造房子myhouse.py上传  

# 20200325作业
1. 学习3D建模课件，挑3个ppt学习即可。 3个设计文件上传到自己的文件夹。 可以用123D也可以用fusion360  
2. 设计创意一个属于自己的物品。 mylogo.stl 文件上传。  
3. 在我的世界里显示自己的物品  mylogo.py 和binvox文件上传。 

# 20200327作业
1. 安装并配置git和vscode, 参见知乎的帖子[如何配置vscode和git](https://zhuanlan.zhihu.com/p/31417255)
2. 在我的世界里利用opencv，利用不同方块和颜色显示一幅线条卡通线条图mypic.jpg , 大小为32x32个方块，程序名为showmypic.py
3. 写一个myclan.py,import 调用mylogo和showmypic里面的函数，完成一次性显示一个logo和卡通图
4. 上传最后效果的屏幕拷贝

# 20200330作业  
1. 跑通倍塔狗语音识别代码
2. 能够用前进，后退，往左，往右指挥我的世界中的角色前后左右移动
3. 在我的世界中竖一个石柱，上海气温20度则高度为20块
4. 效果屏幕拷贝上传自己的目录

# 20200401作业
1. 将造房子的代码改造为类名字为House  类里面需要有isInHouse()函数判断是否在房子里。
2. 利用House类生成27个实例，每个房子的位置在csv文件中定义，csv文件格式举例如下
   housename,x,y,z,l,w,h  
   xknbighouse1,100,10,100,10,10,6  
   xknsmallhouse2,100,10,200,6,6,6  
3. 摄像头监视有运动物体进入画面时唱歌

# 20200403作业
1. 找一个物体作为指挥棒，通过视频和HSV颜色匹配画一个圆跟踪  
2. 利用找到的物体作为遥控器，遥控我的世界的玩家前后左右跑动。  
3. 跑到部落里不同的房子，显示“welcome to xxxx‘s house” xxx是房子的主人的名字  

# 20200408作业
1. 我的世界回到家后点亮arduino的一盏灯，走出家后arduino灯关闭
2. 阿里code团队里面写自己的名字 

# 20200410作业
1. 跑通人脸识别代码
2. 训练3个人脸，自己，家人，其他（比如猫).  
3. 利用人脸检测获得脸部图像保存到文件face.jpg里面
4. 我的世界用玻璃做门。如果是自己，则门变成空气，可以进去。arduino点亮1~4号灯
5. 我的世界用玻璃做门。如果是家人，则门变成空气，可以进去。arduino点亮5~8号灯
6. 其他人不开门（可以用自己带口罩充当）
7. 离开屋子灯熄灭
8. 演示效果用动图gif上传

# 20200415作业
1. 用socket接口编程在我的世界玩家脚下摆3x3的黄金块
2. mcpi协议参考https://github.com/brooksc/mcpipy/blob/master/mcpi/mcpi_protocol_spec.txt
3. 在A4纸大小厚2毫米的板子上设计一个arduino盒子，要求
   * 6个面，露出排针可供扩展
   * 露出USB口可插USB线
   * 一个竖杆插在arduino座上
   * 竖杆上留3个LED灯的位置作为红绿灯

# 20200417作业
1. 用web接口指挥我的世界人物前后左右后退
2. 通过网页在我的世界里建房子

# 20200422作业
1. 利用图像匹配找到minecraft窗口(假设窗口左下角永远在屏幕左下角）
2. 计算出minecraft窗口的大小
3. 自动点击进入我的世界连接好的服务
4. 如果已连接，点击回到世界
5. 修建环形跑道（控制在32x32以内可以用导入图片方式）


# 20200424作业
1.自己搜索一下Openvino安装方法，阅读  
2.用下载的包里面的软件安装  
3.用今天的yolo加速代码测试  

# 20200506作业
1.挑选小组（部落）基地坐标clancenter,xc,yc,zc   
2.在服务器中创建csv文件，定义每人房子的地基的相对坐标格式.文件名team1_clan.csv. 内容举例如下：  
  clancenter,500,20,600  
  tom,10,20,30    
  jerry,30,20,30  
  kevin,60,20,45  
3.在服务器中创建自己的造房子python代码，例如 tomhouse.py
4.在代码中，读入部落的csv文件，找到自己的名字，在部落中造房子。例如，tom 的房子基坐标是 500+20，20+20，600+30  
5.小组每个人都完成后，上传部落房屋截屏到github team里

# 20200508作业
1. 给部落用binvox建一个雕像。雕像位置在csv文件里叫clanlogo  雕像的stl文件任选
  clancenter,500,20,600
  clanlogo,0,0,0
  tom,10,20,30    
  jerry,30,20,30  
  kevin,60,20,45  
2. 代码和stl文件上传github

# 20200511作业
1. Android studio 添加一个按钮，按钮上面显示“按钮”文字  
2. Android studio界面布局.pdf 课件预习
3. Django新建名为topics的APP，创建名为Topic的模型，包含一个名为content的文本字段，并完成模型迁移
4. 效果屏幕拷贝上传自己的目录

# 20200513作业
1. 为登录界面APP的第二个界面添加一个返回点击事件：实现点击可返回登录界面
2. 完成课上投票应用剩余部分
3. 完善博客应用，应有最基础的查看与发表文章功能
4. 效果屏幕拷贝上传自己的目录

# 20200515作业
1. 使用pyautogui完成截取全屏并保存（需要加入弹框进行判定）
2. 完成课上pyautogui打开网页搜索功能
3. 爬取豆瓣上selenium的相关书籍名
4. 效果屏幕拷贝上传自己的目录

# 20200518作业  
1. 让棱锥和轮子同时显示，轮子绕圆心旋转   
2. Homeassistant中添加家庭和杨校区位置图标（要求杨浦校区位置需要真是坐标)
3. 在手机或者虚拟机里面安装IP摄像头，实现局域网实时查看视频
4. 效果屏幕拷贝上传自己的目录

# 20200520作业  
1. 利用串口程序，结合vtk，可以控制vtk物体的转动速度。  
2. AS结合登录界面、音视频界面、计时器界面。通过按钮事件实现跳转。
3. 效果屏幕拷贝上传自己的目录

# 20200522作业  
1. 安装照片上的车尺寸和形状重新设计车
2. Homeassistant完成调通第一个脚本和自动化
3. 结合语音，设计自动化，每天定时播放天气预报
4. 效果屏幕拷贝上传自己的目录

# 20200525作业 
1. 车子模型可以用串口控制左右轮子分别以不同速度转动。
2. 车子模型串口第3个参数表示车子摄像头角度。摄像头pole和indicator整体可随参数改变方向
3. Ha中， 使用脚本 控制hachina3切换状态ON/OFF
4. Ha中，使用自动化控制切换hachina3状态ON/OFF

# 20200527作业 
1. python显示门的三种状态：ON,OFF，LOCK。
2. 把三种状态实时更新到apache的网页中
3. Ha中是实时更新 ON,OFF，LOCK三种状态。
4. 效果屏幕拷贝/代码上传自己的目录

# 20200529作业 
1. 在vtk里面仿真门的开、关
2. ha里和vtk里同步实时显示门的开、关状态
3. ha里和vtk里同步实时显示门的开、关状态。同时ha另加一个卡片上面显示 on/off
4. 效果屏幕拷贝/代码上传自己的目录

# 20200601作业 
1. 完成chat/consumers.py的代码
2. 查阅资料，了解生产者消费者模式
3. 自动截取人脸并合成到语音换衣服的程序上。
4. 效果屏幕拷贝/代码上传自己的目录

# 20200603作业 
1. 完成语音九宫格下棋的程序，完善并提高识别率
2. 开始思考自己的个人项目方向
3. 效果屏幕拷贝/代码上传自己的目录

# 20200605作业 
1. 按小组为单位，继续完善《篮球项目》
2. MQTT完成客户端和接收端
3. 效果屏幕拷贝/代码上传自己的目录

# 20200608作业 
1. 小组内讨论两个小作品的人员分工
2. 下载群里的plugin压缩包读懂源码
3. 效果屏幕拷贝/代码上传自己的目录

# 20200610作业 
1. 个人小项目制作6月15日答辩
2. 徐老师周一作业：使用异步方法优化代码
3. 更新代码到个人小项目文件夹的目录里

# 20200612作业 
1. 完成个人小项目制作6月15日答辩
2. 更新代码到个人小项目文件夹的目录里

# 20200615作业 
1. 整理打包小项目，并写简要安装使用教程
2. 更新代码到个人小项目文件夹的目录里


# 20200617作业 
1. 每个人完成测试工作和测试文档，并提交到阿里云
2. 更新代码到阿里云的项目文件中
3. 完成缺陷指派和解决缺陷指派给自己的问题

# 20200619作业 
1. 完成缺陷指派和解决缺陷指派给自己的问题
2. 完成小项目的网页文档初稿
3. 更新代码到github个人小项目文件夹的目录里

# 20200622作业 
1. 完成数据分析，获取表格中的特定行并生成新表格
2. 完成大项目分工
3. 更新代码到github个人小项目文件夹的目录里

# 20200625作业 
1. 继续完善项目，并新建缺陷推动进度
2. 在简易版控制的基础上尝试增加改变运动速度的功能
3. 更新代码到阿里云的里程碑和缺陷里

# 20200629作业 
1. 继续完善项目，并新建缺陷推动进度
2. 本地创建fastapi服务，接收get请求并在控制台打印任意字符串 
3. 更新代码到阿里云的里程碑和缺陷里

# 20200701作业 
1. 继续完善项目，并新建缺陷推动进度
2. 完成小项目的RS网站项目撰写
3. 更新代码到阿里云的里程碑和缺陷里

# 20200703作业 
1. 继续完善大项目，制作大项目PPT
2. 更新代码到阿里云的里程碑和缺陷里

# 20200706作业 
1. 继续完善大项目，制作大项目PPT
2. 更新代码到阿里云的里程碑和缺陷里

# 20200708作业 
1. 祝同学们前程似锦


# FAQ 
* Q:我的世界游戏启动失败咋办？  
  * A:下载更新的版本。  
* Q:我的世界多人游戏选择了localhost,一直连不进去？  
  * A:确保start.bat已启动，下载游戏勾选下载forge,再不行更新java。  
* Q:在将3D模型导入我的世界程序运行时出现no moudle binvox_rw？  
  * A:要将.py文件与binvox文件放在一起  
 
# Markdown 基本语法
![markdown cheat sheet](https://github.com/shiep18/EIS2020/blob/master/markdowncheatsheet.JPG)

# 解决Github无法显示图片问题
参见 [如何修改host文件添加github](http://blog.csdn.net/weixin_42128813/article/details/102915578)

如果发现图片还是打不开，可以先清空浏览器的缓存图片。具体操作是：浏览器设置 -> 更多工具 -> 清除浏览数据，在弹窗中，时间范围选择“时间不限”，清除“缓存的图片和文件”。清除缓存后，再刷新页面试试。

# VSCODE 本地目录作为默认目录

![](https://github.com/kq2019/G9_2019/blob/master/vscfix_01.JPG)  
![](https://github.com/kq2019/G9_2019/blob/master/vscfix_02.JPG)


![](https://github.com/kq2019/G9_2019/blob/master/vscfix_01.JPG)  
![](https://github.com/kq2019/G9_2019/blob/master/vscfix_02.JPG)

![bridgemode](https://github.com/shiep18/EIS2020/blob/master/students/Lang%20Yuan/bridgemodel.PNG)
![mylogo](https://github.com/shiep18/EIS2020/blob/master/students/Lang%20Yuan/mc.bqb.JPG)
![mc.bridge](https://github.com/shiep18/EIS2020/blob/master/students/Lang%20Yuan/mc.bridge.PNG)
![mc.bridge2](https://github.com/shiep18/EIS2020/blob/master/students/Lang%20Yuan/mc.bridge2.PNG)
![mc.pi](https://github.com/shiep18/EIS2020/blob/master/students/Lang%20Yuan/mc.pic.PNG)
![princess](https://github.com/shiep18/EIS2020/blob/master/students/Lang%20Yuan/princess.PNG)
![qtww](https://github.com/shiep18/EIS2020/blob/master/students/Lang%20Yuan/qtww.PNG)
![qtww](https://github.com/shiep18/EIS2020/blob/master/students/Lang%20Yuan/Screenshots/bridge1.PNG)
![sheep](https://github.com/shiep18/EIS2020/blob/master/students/Lang%20Yuan/sheep.png)
![sheep2](https://github.com/shiep18/EIS2020/blob/master/students/Lang%20Yuan/sheep2.png)
![sheep2](https://github.com/shiep18/EIS2020/blob/master/students/Lang%20Yuan/myhouse.PNG)
![inside](https://github.com/shiep18/EIS2020/blob/master/students/Lang%20Yuan/inside.png)
![h](https://github.com/shiep18/EIS2020/blob/master/students/Lang%20Yuan/h.png)
![h](https://github.com/shiep18/EIS2020/blob/master/students/Lang%20Yuan/inside3.png)
