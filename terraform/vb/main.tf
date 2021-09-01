terraform{
  required_providers {
      virtualbox = {
        source  = "terra-farm/virtualbox"
        version = "0.2.1-alpha.1"
      }
  }
}

resource "virtualbox_vm" "node" {
    count = 1
    name = "some test node"
    url = "https://vagrantcloud.com/ubuntu/boxes/xenial64/versions/20180420.0.0/providers/virtualbox.box"
    image = "./virtualbox.box"
    cpus = 2
    memory = "512 mib"


     network_adapter {
       type = "bridged"
       host_interface="en0"
    }
}