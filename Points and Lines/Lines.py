
#Point class that gives us 2 points and makes them to point and it is private ,set and get.
class Point:
    def __init__(self,x,y):
        if not isinstance(x,(int,float)):
            raise Exception("the x must be an integer")
        if not isinstance(y,(int,float)):
            raise Exception("the y must be an integer")
        self.__p=x
        self.__q=y
    def getx(self):
        return self.__p
    def gety(self):
        return self.__q
    def setx(self,x):
         if not isinstance(x, (int,float)):
            raise Exception("the x must be an integer")
         self.__p=x
    def sety(self,y):
         if not isinstance(y, (int,float)):
            raise Exception("the y must be an integer")
         self.__q=y
    def __str__(self):
        return '(%.2f,%.2f)'%(self.__p,self.__q)
    pass
#class line gives us intersection of 2 points and its slope and it is priate and functions y=ax+b and if it is vertical or not
    #and if 2 funcs are parellel to each other and their interserc with y and if there is 2 funcs that is equals to each other
class Line:
    def __init__(self,w1,w2):
        if type(w1)!=Point:
            raise Exception('the given info is not a point(w1)')
        if type(w2)!=Point:
            raise Exception('(w2)point is not in here')
        self.__w1=w1
        self.__w2=w2
    def getw1(self):
        return self.__w1
    def getw2(self):
        return self.__w2
    def setw1(self,w1):
        if type(w1)!=Point:
            raise Exception('The given w1 is not a point')
        self.__w1=w1
    def setw2(self,w2):
        if type(w2)!=Point:
            raise Exception('The given w2 is not a point')
        self.__w2=w2
    def is_vertical(self):
        if self.__w1.gety() - self.__w2.gety()==0:
            return True
    def slope(self):
        if self.is_vertical():
            return None
        try:
            f=(self.__w1.gety() - self.__w2.gety())/(self.__w1.getx() - self.__w2.getx())
            return f
        except:
            return None
    def y_intersect(self):
        if self.slope()==None:
            return self.getw1().getx()
        if self.is_vertical() is True:
            return None
        else:
            m=self.slope()
            y=self.__w1.gety()-(m*(self.__w1.getx()))
            return y
    def __str__(self):
        if self.is_vertical() is True:
            return 'x={0:0.2f}'.format(self.__w1.gety())
        m1=self.slope()
        y1=self.__w1.gety()-(m1*(self.__w1.getx()))
        return 'y={0:0.2f}x+{1:0.2f}'.format(self.slope(),y1)
    def parallel(self,other):
        l=Line(self.__w1,self.__w2)
        if other.slope()==l.slope():
            return True
    def equals(self,other):
        l=Line(self.__w1,self.__w2)
        if l.slope()==other.slope() and l.y_intersect()==other.y_intersect():
            return True
    def intersection(self,other):
        l=Line(self.__w1,self.__w2)
        if other.slope()==l.slope():
            return None
        if other.slope()==None:
            x=other.getw1().getx()
            f=lambda x:l.slope()*x+l.y_intersect()
            y=f(x)
            return '({0:0.2f},{1:0.2f})'.format(x,y)
        if l.slope()==None:
            x=l.getw1().getx()
            f=lambda x:other.slope()*x+other.y_intersect()
            y=f(x)
            return '({0:0.2f},{1:0.2f})'.format(x,y)
        if l.is_vertical():
            x=l.getw1().gety()
            f=lambda x:(x-l.y_intersect())/l.slop()
            y=f(x)
            return '({0:0.2f},{1:0.2f})'.format(x,y)
        if other.is_vertical():
            x=other.getw1().gety()
            f=lambda x:(x-l.y_intersect())/l.slope()
            return '({0:0.2f},{1:0.2f})'.format(x,y)
        else:
            x=(other.y_intersect()-l.y_intersect())/(l.slope()-other.slope())
            m1=self.slope()
            y1=self.__w1.gety()-(m1*(self.__w1.getx()))
            w2='{0:0.2f}*x+{1:0.2f}'.format(self.slope(),y1)
            t=eval('lambda x:'+w2)
            y=t(x)
            return '({0:0.2f},{1:0.2f})'.format(x,y)
#getting 2 points getting intersection betwen 2 funcs by the line and point classes
            #3 rules all need to be done like how it should be
xp=[]
ts=[]
sp=''
o1=1
f=open('input.txt','r')
f=f.read()
f=f.splitlines()
op=open('output.txt','w')
#func that give us floats and if there is no float the func stop from there and gives us what is before
for i in f:
    for w in i.split():
        try:
            w=float(w)
        except:
            f=f[:f.index(i)]
            sp+='Equal Funcs'
sp+='\nLines:'
#checking if len the points are 4 for 2 different sloppes and funcs
for i in f:
    g13=f.index(i)
    i=i.split()
    if len(i)!=4:
            sp+='\nnot 4 numbers'
            break
    #making all inj indexs to float
    i = list(map(float, i))
    t1=Point(i[0],i[1])
    t2=Point(i[2],i[3])
    t3=Line(t1,t2)
    #making points and creating funs by x=P or y=ax+b
    if i[0]-i[2]==0:
        t=('x={0}'.format(str(i[3])))
        xp.append(t)
    else:
        x1=('{0}'.format(str(t3)))
        xp.append(x1)
        ts.append(x1[2:])
    
    if i[0]-i[2]==0:
        t=('\nline {0}: x={1}'.format(str(o1),str(i[0])))
        sp+=t

    else:
        x1=('\nline {0}: {1}'.format(str(o1),str(t3)))
        sp+=x1

    o1+=1
    #making all the indexs in f by using map func to floats by what is the question wants.
    for g in f:
        t52=f.index(g)
        g=g.split()
        g = list(map(float, g))
        if len(g)==4:
            t17=Point(g[0],g[1])
            t18=Point(g[2],g[3])
            t40=Line(t17,t18)
        if t40.equals(t3):
            continue
        if t3.slope()==t40.slope():
            sp+=('  *Line{0} is Parallel To Line{1}').format((g13+1),(t52+1))
        #here is a way to check if there is funcs that is equals to each other
    if len(xp)!=len(set(xp)):
       sp+=("\nError same funcs ")
       break
ol=1
sp+='\n'
xl=xp[ol:]
#looping in list just in case to get what is parallel to what like what is before
for i in xp:
    ol+=1
    for w in xp[ol:]:
        if w==i:
            sp+=('Line{0} is Parallel To Line{1}').format((xl.index(w)+ol),(xp.index(i)+1))
      # here is a loop to get the intersec betwen every single func in hthe list and if there is a problem that is shown the loops deals with it      
sp+='\n'
sp+='(Intersections)\n'
f=f[:len(xp)]
for i in f:
    i=i.split()
    i = list(map(float, i))
    if len(i)==4:
             t1=Point(i[0],i[1])
             t2=Point(i[2],i[3])
             t3=Line(t1,t2)
# looping 2 times in the same list just to get the every intersect of every single fun in the given funcs
    for g1 in f:
        g1=g1.split()
        g1 = list(map(float, g1)) 
        t11=Point(g1[0],g1[1])
        t12=Point(g1[2],g1[3])
        t13=Line(t11,t12)
        t15=t13.intersection(t3)
        if t15==None:
            break
        else:
            sp+=t15
            sp+='\n'
#adding all the funcs in the op file wchil called output
op.write(sp)
op.close()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#def main():
#    try:
#       f=open('input.txt','r')
#       f=f.read()
#       f=f.splitlines()
#       b=[]
#       try:
#           for i in f:
#               i=i.split()
#               if len(i)!=4:
#                   raise Exception('not 4 numbers')          
#               i[0]=float(i[0]); i[1]=float(i[1]); i[2]=float(i[2]); i[3]=float(i[3])
#               t1=Point(i[0],i[1])
#               t2=Point(i[2],i[3])
#               t3=Line(t1,t2)
##               t4=print(Line(t1,t2))
#               b.append(t3)
#               if i[0]-i[2]==0:
#                   print('y=',i[1])
#               else:
#                   print(Line(t1,t2))
#
#       except ValueError:
#           print('Error')
#
#    except Exception as hey:
#        print(hey)
    
#main()
    
