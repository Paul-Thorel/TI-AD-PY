from sys import stdin,stdout

class screen():
  def __init__(self,x,y,fill=" "):
    self.x=x
    self.y=y
    self.tab=[[fill for i in range(x)]for j in range(y)]
  def locate(self,x,y,text):
    for i in range(x,32):
      try:
        self.tab[y][i]=text[i-x]
      except:
        pass
  def display(self):
    for y in self.tab:
      for x in y: 
        stdout.write(x)

def clr():
  stdout.write("\n"*10+"\b"*10*32)

def chrput(c=0):
  """Launch one character selector : chrput(c=0)
  if c==0 : return the character
  else return the ord value"""
  l=True
  i=138
  stdout.write(" ")
  while l:
    stdout.write("\b"+chr(i)+chr(131)+"\b")
    g=getkey()
    if g=="[A":
      if i<255:
        i+=1
      if i==143:
        i=162
    elif g=="[B":
      if i>=33:
        i-=1
      if i==161:
        i=142
    elif g=="[C":
      l=False
  if c==0:
    stdout.write("\n")
    return chr(i)
  else:
    return i

def keyput(l):
  s=""
  c=""
  for i in range(l):
    c=getkey()
    if len(c)==2:
      c=" "
    if c!="\b":
      s+=c
      stdout.write(s[i])
    else:
      s+=chr(chrput(1))
      stdout.write(s[i]+"\b")
  stdout.write("\n")
  return s

def getkey():
  s=stdin.read(1)
  if s==chr(27):
    s=stdin.read(2) 
    if s=="[2":
      stdin.read(1)
  return s

def ispressed(key,gotkey):
  if key=="up":
    key="[A"
  if key=="down":
    key="[B"
  if key=="left":
    key="[D"
  if key=="right":
    key="[C"
  if key=="enter":
    key="[F"
  if key=="annul":
    key="[2"
  if key==gotkey:
    return True
  else:
    return False

def menu(*choices,message="",ch=chr(131)):
  y=2
  if choices==():
    raise AttributeError("No arg in choices list")
  elif len(choices)>9:
    raise AttributeError("Too args in choices list")
  while 1:
    stdout.write(message+"\n")
    for i in range(2,11):
      if y==i:
        try:
          stdout.write(" {} ".format(ch)+choices[i-2][:32-len(ch)-2]+"\n")
        except:
          stdout.write("\n")
      else:
        try:
          stdout.write("   "+choices[i-2][:32-3]+"\n")
        except :
          stdout.write("\n")
    g=getkey()
    if ispressed("annul",g):
      break
    elif ispressed("up",g):
      if y!=2:
        y-=1
    elif ispressed("down",g):
      if y!=len(choices)+1:
        y+=1
    elif ispressed("enter",g):
      return y-2

def help(name,script=__name__):
  assert len(name)!=0,"no function given"
  name=str(name)
  try:
    f=open(script+".py").read()
  except OSError:
    print("No module named '"+script+"'")
    return
  assert f.find(name+"(")!=-1,"no function named '"+name+"'"
  t=f[f.find(name):]
  assert f!=t,"no help found for '"+name+"'"
  f=t
  print(f[f.find(' """')+4:f.find('"""',f.find('"""')+1)])

def dialogbox(message="DO YOU WANT TO CONTINUE"):
  r=chr(130)+"YES"+chr(131)
  l="NO"
  x=0
  while 1:
    if x%2==0:
      r=chr(130)+"YES"+chr(131)
      l="NO "
    else:
      l=chr(130)+"NO"+chr(131)+" "
      r="YES"
    if message.find("\n")==-1:
      message+="\n"
    stdout.write(message+"\n\n\n\n\n          "+l+"   "+r+"          \n\n\n\n")
    g=getkey()
    if ispressed("annul",g):
      return False
    elif ispressed("enter",g):
      if x%2==0:
        return True
      else:
        return False
    elif ispressed("right",g):
      x+=1
    elif ispressed("left",g):
      x-=1
