#为了方便，避免忘记close掉这个文件对象，可以用下面这种方式替代
import  os
import shutil

#获取当前路径 /home/YOLOv5-Tools/CrowHuman2YOLO/data
current_path = os.getcwd()

train_txt_path = current_path + '/crowdhuman-608x608/train.txt'
test_txt_path = current_path + '/crowdhuman-608x608/test.txt'

# 数据集生成目录
to_train_img_path = '/user-data/crowdedHuman/images/train/' 
to_val_img_path = '/user-data/crowdedHuman/images/val/'
to_train_label_path = '/user-data/crowdedHuman/labels/train/'
to_val_label_path = '/user-data/crowdedHuman/labels/val/'

# 训练数据集
with open(train_txt_path,"r") as f:    #设置文件对象

    for line in f.readlines():
        line = line.strip('\n')  #去掉列表中每一个元素的换行符
        
        fileName = line.split('/')[-1]
        # fileName 284193,faa9000f2678b5e.jpg
        
        imgExtendName = fileName.split(".")[-1]
        # imgExtendName jpg
        
        imgName = fileName.split(".")[0]
        # imgName 284193,faa9000f2678b5e
        
        # 复制训练的图片
        shutil.copyfile(current_path + '/crowdhuman-608x608/' + fileName, to_train_img_path + fileName)
        # 复制训练的标签
        shutil.copyfile(current_path + '/crowdhuman-608x608/' + imgName + '.txt', to_train_label_path + imgName + '.txt')
        
# val数据集
with open(test_txt_path,"r") as f:    #设置文件对象
    for line in f.readlines():
        line = line.strip('\n')  #去掉列表中每一个元素的换行符
        
        fileName = line.split('/')[-1]
        
        imgExtendName = fileName.split(".")[-1]
        
        imgName = fileName.split(".")[0]
        
        # 复制测试的图片
        shutil.copyfile(current_path + '/crowdhuman-608x608/' + fileName, to_val_img_path + fileName)
        # 复制测试的标签
        shutil.copyfile(current_path + '/crowdhuman-608x608/' + imgName + '.txt', to_val_label_path + imgName + '.txt')
        
        
        