import os,shutil
for path,files,folders in os.walk('~'):
	for folder in folders:
		if folder == '__pycache__':
			print('Deleting',os.path.join(path,folder))
			shutil.rmtree(folder)
