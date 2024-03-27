from ft_package import ft_tqdm
from time import sleep

for elem in ft_tqdm(range(333)):
    sleep(0.005)
print()

# python3 setup.py bdist_wheel sdist
# pip3 install ./dist/ft_package-0.0.1.tar.gz
# pip3 install ./dist/ft_package-0.0.1-py3-none-any.whl 