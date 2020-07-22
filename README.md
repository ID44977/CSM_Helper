# CSM_Helper
自动生成BDMV文件结构，复制除.m2ts外的所有文件和结构，用以配合外挂结构实现蓝光原盘外挂字幕

蓝光原盘结构
Source目录："F:\\ACG\\Animate\\[BDMV]"
Target目录："F:\\ACG\\Animate\\[BDMV] 加流重灌\\"
输入：番剧名bdmv_name、分卷个数vol_num
在Target目录下生成名为"bdmv_name"的文件夹，其拥有子目录"Vol.1_SUB~Vol.n_SUB"
依次选择分卷的源地址
自动复制结构及小文件至Target目录下相应分卷位置

外挂字幕
字幕文件Source目录："F:\\BDMV DIY\\ALL_SUB\\"
番剧外挂字幕项目资源目录："F:\\BDMV DIY\\"
输入：番剧名bdmv_name、分卷个数vol_num、每卷集数ep_num
在资源目录下生成名为"bdmv_name"的文件夹，其拥有子目录"Vol.1_SUBDIY--Vol.n_SUBDIY"
从字幕文件Source目录中将ass字幕文件按卷-集方式分别复制至目录"Vol.1_SUBDIY--Vol.n_SUBDIY"中

待完成：
整合制作好的字幕流至外挂结构中
优化逻辑和适配
