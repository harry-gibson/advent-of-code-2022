from aocd import data


class Folder:
    
    def __init__(self, name='/', file_lengths=[], parent=None):
        self.subdirs = {}
        self.filesize = sum(file_lengths)
        self.name = name
        self.parent:Folder = parent
    
    def dirs(self):
        if self.name != '/': yield self
        for subdir in self.subdirs.values():
            yield from subdir.dirs()
    
    def tree_size(self):
        return self.filesize + sum((F.tree_size()) for F in self.subdirs.values())


root_dir = Folder()
current_dir = root_dir
parent_dir = None

for line in data.split('\n')[2:]:
    if not line.startswith('$'):
        item, name = line.split(' ')
        if item == 'dir':
            current_dir.subdirs[name] = Folder(name=name, parent=current_dir)
        else:
            current_dir.filesize += int(item)
    elif line.startswith('$ cd'):
        newdir = line.split(' ')[-1]
        if newdir != '..':
            current_dir = current_dir.subdirs[newdir]
        else:
            current_dir = current_dir.parent
    else:
        assert line.startswith('$ ls')

# Part 1:
print(sum(s for s in (f.tree_size() for f in root_dir.dirs()) if s<=100000))

# Part 2:
req_space = root_dir.tree_size() - (70000000 - 30000000)
dir_sizes = sorted(d.tree_size() for d in root_dir.dirs())
bigenough = filter(lambda d: d >= req_space, dir_sizes)
print(next(bigenough))
