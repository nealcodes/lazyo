import os
base_dir = '/home/neal/Downloads/'
downloads = []

for x in os.scandir(base_dir):
    downloads.append((x.name, x.stat().st_mtime))



downloads = sorted(downloads, key=lambda item: item[1])

full_path = base_dir + downloads[-1][0]
print(full_path)
os.execlp('code', 'code', full_path)

