import argparse
import sys
class ATG:
  def __init__(self):
    self.addr = []
    self.data = []
    self.ctrl = []
    self.mask = []

  def parse_file(self, addr, data, ctrl, mask):
    print(addr)
    cnt = 0
    with open(addr) as fp:
      line = fp.readline()
      while line:
        if cnt >= 2 and line != '11111111111111111111111111111111;\n':
          self.addr.append("0x{0:0{1}X}".format(int(line, 2), 8))
        line = fp.readline()
        cnt += 1
    fp.close()

    print(data)
    cnt = 0
    with open(data) as fp:
      line = fp.readline()
      while line:
        if cnt >= 2 and line != '11111111111111111111111111111111;\n':
          self.data.append("0x{0:0{1}X}".format(int(line, 2), 8))
        line = fp.readline()
        cnt += 1
    fp.close()

    print(ctrl)
    cnt = 0
    with open(ctrl) as fp:
      line = fp.readline()
      while line:
        if cnt >= 2 and line != '11111111111111111111111111111111;\n':
          self.ctrl.append("0x{0:0{1}X}".format(int(line, 2), 8))
        line = fp.readline()
        cnt += 1
    fp.close()

    print(mask)
    cnt = 0
    with open(mask) as fp:
      line = fp.readline()
      while line:
        if cnt >= 2 and line != '11111111111111111111111111111111;\n':
          self.mask.append("0x{0:0{1}X}".format(int(line, 2), 8))
        line = fp.readline()
        cnt += 1
    fp.close()
  
  def print_all(self):
    print("addr" + "\t\t" + "data" + "\t\t" + "ctrl" + "\t\t" + "mask")
    for i in range(len(self.addr)):
      print(self.addr[i] + "\t" + self.data[i] + "\t" + self.ctrl[i] + "\t" + self.mask[i])

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("addr", help="directory to the addr", type=str)
  parser.add_argument("data", help="directory to the data", type=str)
  parser.add_argument("ctrl", help="directory to the ctrl", type=str)
  parser.add_argument("mask", help="directory to the mask", type=str)
  args = parser.parse_args()
  atg = ATG()
  atg.parse_file(args.addr, args.data, args.ctrl, args.mask)
  atg.print_all()
  
  

  
  