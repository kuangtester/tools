import os
import yaml
from config.settings import yamlpath
def ReadYaml(login_yaml):
    with open(yamlpath+os.sep+"d_delcart.yaml",'r',encoding='utf-8') as f:
        infodict=yaml.safe_load(f)

    return infodict[login_yaml]

if __name__ == '__main__':
    data=ReadYaml()
    print(data)
