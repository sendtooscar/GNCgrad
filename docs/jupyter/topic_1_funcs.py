# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import ipyvolume.pylab as p3 
import numpy as np
from scipy.spatial.transform import Rotation as Rot

def init_vector(show=True):
    #This function initializes a figure with basis vectors in world frame - requires import ipyvolume.pylab as p3 outside scope
    #p3.clear()
    origin = np.array([0.0,0.0,0.0])
    x = origin + np.array([1.0,0.0,0.0])
    y = origin + np.array([0.0,1.0,0.0])
    z = origin + np.array([0.0,0.0,1.0])
    u =np.array([1.0,0.0,0.0])
    v =np.array([0.0,1.0,0.0])
    w =np.array([0.0,0.0,1.0])
    quiver =  p3.quiver(x,y,z,u,v,w,size=10,marker = 'arrow',color=np.array([[1,0,0],[0,1,0],[0,0,1]]))#ipv.show()
    scatter = p3.scatter(np.array([origin[0]]),np.array([origin[0]]),np.array([origin[0]]),size=5,marker = 'sphere',color='red')
    line1 = p3.plot(np.array([origin[0],x[0]]),np.array([origin[0],x[1]]),np.array([origin[0],x[2]]),color='red')
    line2 = p3.plot(np.array([origin[0],y[0]]),np.array([origin[0],y[1]]),np.array([origin[0],y[2]]),color='green')
    line3 = p3.plot(np.array([origin[0],z[0]]),np.array([origin[0],z[1]]),np.array([origin[0],z[2]]),color='blue')
    #scatter = p3.scatter(x,y,z,size=2,marker = 'sphere',color='red') # the origin
    if show:
        p3.show()
        p3.style.box_off()
    handle={'origin':scatter,'arrows':quiver,'linex':line1,'liney':line2,'linez':line3}
    #p3.style.axes_off()
    return handle


def ipv_setframe(p,R,handle):
    arrows=handle['arrows']
    linex=handle['linex']
    liney=handle['liney']
    linez=handle['linez']
    origin=handle['origin']
    
    #Update origin
    origin.x=np.array([p[0]])
    origin.y=np.array([p[1]])
    origin.z=np.array([p[2]])
    
    
    x=np.array([p[0],p[0],p[0]])+R.as_dcm()[0,:]
    y=np.array([p[1],p[1],p[1]])+R.as_dcm()[1,:]
    z=np.array([p[2],p[2],p[2]])+R.as_dcm()[2,:]
    u=R.as_dcm()[0,:]
    v=R.as_dcm()[1,:]
    w=R.as_dcm()[2,:]
    
    #Update arrows
    arrows.x=x
    arrows.y=y
    arrows.z=z
    arrows.vx=u
    arrows.vy=v
    arrows.vz=w
    
    #Update lines
    linex.x=np.array([p[0],x[0]])
    linex.y=np.array([p[1],y[0]])
    linex.z=np.array([p[2],z[0]])
    liney.x=np.array([p[0],x[1]])
    liney.y=np.array([p[1],y[1]])
    liney.z=np.array([p[2],z[1]])
    linez.x=np.array([p[0],x[2]])
    linez.y=np.array([p[1],y[2]])
    linez.z=np.array([p[2],z[2]])