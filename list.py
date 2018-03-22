import os



img_root = '/home/pengshanzhen/training_data/val'
label_root = '/home/pengshanzhen/training_data/val_den'
#img_root = '/home/pengshanzhen/crowdcount-mcnn/data/formatted_trainval/shanghaitech_part_B_patches_9/val'
#label_root = '/home/pengshanzhen/crowdcount-mcnn/data/formatted_trainval/shanghaitech_part_B_patches_9/val_den'



img_list = os.listdir(img_root)
fid = open('val_label.txt', 'w')
for image_name in img_list:
  img_path =os.path.join(img_root ,image_name )
  a = os.path.splitext(image_name)[1] + '.csv'
  
  label_path = os.path.join(label_root ,os.path.splitext(image_name)[0] + '.csv')

  fid.write('%s %s\n'%(img_path, label_path))





