# 2017-08-05
# Extract Windows Start_Menu
# Lee BangHun
import os
import time

#set start_menu path
f_path = os.getenv("APPDATA") + "\Microsoft\Windows\Start Menu\Programs"

#get file list
f_list = os.listdir(f_path)

f = open('Start_Menu_File_List.txt', "w")

for i in f_list:
	#get data info
	fileinfo = os.stat(f_path + '\\' + i)
	f_uid = fileinfo.st_uid
	f_size = fileinfo.st_size
	m_time = fileinfo.st_mtime
	a_time = fileinfo.st_atime
	c_time = fileinfo.st_ctime
	
	f_data = (str(i) +' (UID / File_size / Modified_time / Accessed_time / Created_time)'+ '\n' 
	+ str(f_uid) + '\t' + str(f_size) + '\t'  + str(time.ctime(m_time)) + '\t' 
	+ str(time.ctime(a_time)) + '\t' + str(time.ctime(c_time)) + '\n\n')

	#write data
	f.write(f_data)

f.close