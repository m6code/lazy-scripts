# batch_add_file_extension.py
import os;
root = os.getcwd()
for file in os.listdir('.'):
	if not os.path.isfile(file):
		continue
	head, tail = os.path.splitext(file)
	if not tail:
		src = os.path.join(root, file)
		dst = os.path.join(root, file + '.jpg') # Your desired file extension goes where jpg is

		if not os.path.exists(dst):
			os.rename(src, dst)