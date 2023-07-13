#Assuming that we already know the k vectors of the bulk BZ
#Copy right@ zijiac@princeton.edu
#Require numpy and matplotlib
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
np.seterr(all='raise') #raise warning as errors


class BZ:
    '''
    This class is used to draw the bulk BZ and surface of a given lattice.

    Attributes:

        kvector: the k vector of the bulk BZ, with unit A^-1 and written in the Cartesian coordinates. eg: np.array([[1,0,0],[0,1,0],[0,0,1]]).
        hs_lines_f: the high symmetry lines of the bulk BZ
        hs_points: the high symmetry points of the bulk BZ
        hs_lines_pro_f: the high symmetry lines of the surface BZ
        hs_pro_points: the high symmetry points of the surface BZ

    

    '''
    
    def __init__(self, kvector):
        '''
        Input:
            kvector: the k vector of the bulk BZ, with unit A^-1 and written in the Cartesian coordinates. eg: np.array([[1,0,0],[0,1,0],[0,0,1]]).
        '''
        self.kvector = kvector
    
    def crossline(self,vector1:list,vector2:list):
        #Return the crossing line of two planes with normal vectors 1 and 2.
        if(abs(np.dot(vector1,vector2))==np.sqrt(np.dot(vector1,vector1)*np.dot(vector2,vector2))):
            return np.array([0,0,0,0,0,0,0,0]) #Two planes are parrellel
        #Vector 1 and 2 are normal vectors of two planes: just k vector): So the planes are vector*(x,y,z)==1/2|vector|^2
        direct = np.cross(vector1,vector2) #The direction of the line
        #Then we need to figure out how to find a point on the line. 
        norm_direct = np.cross(vector1,direct) #direction of a line // to the plane 1 and perpendicular to the line
        #Then the line with direction norm_direct and passing point 1/2 vector1 must be in the plane 1 and perpendicular to the line
        t = 0.5*(np.dot(vector2,vector2)-np.dot(vector1,vector2))/(np.dot(vector2,norm_direct))
        #So the crossing point is t*norm_direct+0.5*vector1
        return np.concatenate((direct,t*norm_direct+0.5*vector1,np.array([-100000,100000]))) #The first three index are the direction, 4-6 are the fixing points, last two are the range of t
    
    def cutrange(self, kvector,linevector):
        flag1 = np.dot(kvector,linevector[6]*linevector[:3]+linevector[3:6])-0.5*np.dot(kvector,kvector)
        flag2 = np.dot(kvector,linevector[7]*linevector[:3]+linevector[3:6])-0.5*np.dot(kvector,kvector)
    
    
        if(flag1>0.0001 and flag2>0.0001):
            return 0 #the line part is not in the first BZ, why return True doesn't work?
        elif(flag1>0.0001 and flag2<=0.0001):
            linevector[6] = (0.5*np.dot(kvector,kvector)-np.dot(kvector,linevector[3:6]))/(np.dot(kvector,linevector[:3]))
        elif(flag1<=0.0001 and flag2>0.0001):
            linevector[7] = (0.5*np.dot(kvector,kvector)-np.dot(kvector,linevector[3:6]))/(np.dot(kvector,linevector[:3]))
    
        return 1
    
    def bulkBZ(self):
        '''
        
        This function is used to draw the bulk BZ of a given lattice.

        Generated attributes:
    
            self.hs_lines_f: the high symmetry lines of the bulk BZ
            self.hs_points: the high symmetry points of the bulk BZ


        '''

        self.kvectors = []
        kvectors = self.kvectors
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                for k in [-1,0,1]:
                    if(i==0 and j==0 and k==0):
                        continue
                    kvectors.append(i*self.kvector[0]+j*self.kvector[1]+k*self.kvector[2])
        hs_lines = [] #High symmetry lines

        for i in range(len(self.kvectors)-1):
            for j in range(i+1,len(kvectors)):
                hs_line = self.crossline(kvectors[i],kvectors[j])
                if(list(hs_line) == [0,0,0,0,0,0,0,0]):
                    continue
                flag = 0
                for k in range(len(kvectors)):
                    if(k!=i and k!=j):
                        try:
                            if(not self.cutrange(kvectors[k],hs_line)):
                                flag=1
                                break
                        except:
                            print(i,j,k,hs_line)
                if(flag==0 and (hs_line[6]!=0 or hs_line[7]!=0)):
                    hs_lines.append(hs_line)
        self.hs_lines_f = []
        for hs_line in hs_lines:
            if(abs(hs_line[6]-hs_line[7])<0.00001):
                continue
            flag = 0
            for i in self.hs_lines_f:
                if(abs(np.dot(i[:3],hs_line[:3]))==np.sqrt(np.dot(i[:3],i[:3])*np.dot(hs_line[:3],hs_line[:3])) and (abs(np.dot(i[3:6]-hs_line[3:6],i[3:6]-hs_line[3:6]))<0.0001 or abs(np.dot(i[3:6]-hs_line[3:6],hs_line[:3]))==np.sqrt(np.dot(i[3:6]-hs_line[3:6],i[3:6]-hs_line[3:6])*np.dot(hs_line[:3],hs_line[:3])))):
                    flag = 1
                    break
            if(flag==0):
                self.hs_lines_f.append(hs_line)  
        self.hs_points = []
        for hs_line in self.hs_lines_f:
            flag = 0
            for point in self.hs_points:
                if(abs(np.dot(point-(hs_line[6]*hs_line[:3]+hs_line[3:6]),point-(hs_line[6]*hs_line[:3]+hs_line[3:6])))<0.000001):
                    flag = 1
                    break
            if(flag==0):
                self.hs_points.append(hs_line[6]*hs_line[:3]+hs_line[3:6])
            flag = 0
            for point in self.hs_points:
                if(abs(np.dot(point-(hs_line[7]*hs_line[:3]+hs_line[3:6]),point-(hs_line[7]*hs_line[:3]+hs_line[3:6])))<0.000001):
                    flag = 1
                    break
            if(flag==0):
                self.hs_points.append(hs_line[7]*hs_line[:3]+hs_line[3:6])
        self.hs_points = np.array(self.hs_points)
                
    def crossline2(self,kvector,kgamma):
        slope = np.cross(kvector-kgamma,self.direc_a)
        return np.concatenate((slope,0.5*(kvector+kgamma),np.array([-1000,1000])))

    def cutrange2(self,kvector,kgamma,linevector):
        flag1 = np.dot(kvector-kgamma,linevector[6]*linevector[:3]+linevector[3:6])-0.5*np.dot(kvector-kgamma,kvector-kgamma)
        flag2 = np.dot(kvector-kgamma,linevector[7]*linevector[:3]+linevector[3:6])-0.5*np.dot(kvector-kgamma,kvector-kgamma)
        if(flag1>0.0001 and flag2>0.0001):
            return 0 #the line part is not in the first BZ, 
        elif(flag1>0.0001 and flag2<=0.0001):
            linevector[6] = (0.5*np.dot(kvector-kgamma,kvector-kgamma)-np.dot(kvector-kgamma,linevector[3:6]))/(np.dot(kvector-kgamma,linevector[:3]))
        elif(flag1<=0.0001 and flag2>0.0001):
            linevector[7] = (0.5*np.dot(kvector-kgamma,kvector-kgamma)-np.dot(kvector-kgamma,linevector[3:6]))/(np.dot(kvector-kgamma,linevector[:3]))

        return 1

    
    
    def surfaceBZ(self,dis,direc):
        """
        dis: the distance between the surface BZ and the Gamma point
        direc: the direction of the terminated surface, written in Fractional coordinates with BZ vectors as basis.

        Generated attributes:
            self.hs_lines_pro_f: the projected high symmetry lines on the surface BZ
            self.hs_pro_points: the projected high symmetry points on the surface BZ
        """
        kvectors = self.kvectors
        self.dis = dis
        self.direc = direc
        self.direc_a = np.dot(self.direc,self.kvector)/np.sqrt(np.dot(np.dot(self.direc,self.kvector),np.dot(self.direc,self.kvector)))
        #So the projected surface is np.dot(direc_a,(x,y,z))=dis
        #projected bulk Gammas
        kvectors_pro = []
        kgamma_pro = dis*self.direc_a
        for kv in self.kvectors:
            kv_pro = (dis-np.dot(kv,self.direc_a))*self.direc_a+kv
            if(np.dot(kgamma_pro-kv_pro,kgamma_pro-kv_pro)<0.0001):
                continue
            flag = 0
            for j in kvectors_pro:
                if(np.dot(j-kv_pro,j-kv_pro)<0.0001):
                    flag=1
                    break
            if(flag==0):
                kvectors_pro.append(kv_pro)        
        hs_lines_pro = []
        for kv in kvectors_pro:
            hs_line = self.crossline2(kv,kgamma_pro)
            flag = 0
            for i in kvectors_pro:
                if(np.dot(i-kv,i-kv)>0.00001):
                    if(not self.cutrange2(i,kgamma_pro,hs_line)):
                        flag =1
                        break
            if(flag==0):
                hs_lines_pro.append(hs_line)

        self.hs_lines_pro_f = []
        for hs_line in hs_lines_pro:
            if(abs(hs_line[6]-hs_line[7])<0.00001):
                continue
            flag = 0
            for i in self.hs_lines_pro_f:
                if(abs(np.dot(i[:3],hs_line[:3]))==np.sqrt(np.dot(i[:3],i[:3])*np.dot(hs_line[:3],hs_line[:3])) and (abs(np.dot(i[3:6]-hs_line[3:6],i[3:6]-hs_line[3:6]))<0.0001 or abs(np.dot(i[3:6]-hs_line[3:6],hs_line[:3]))==np.sqrt(np.dot(i[3:6]-hs_line[3:6],i[3:6]-hs_line[3:6])*np.dot(hs_line[:3],hs_line[:3])))):
                    flag = 1
                    break
            if(flag==0):
                self.hs_lines_pro_f.append(hs_line)

        #High symmetry points of the surface BZ
        self.hs_pro_points=[]
        for hs_line in self.hs_lines_pro_f:
            flag = 0
            for point in self.hs_pro_points:
                if(abs(np.dot(point-(hs_line[6]*hs_line[:3]+hs_line[3:6]),point-(hs_line[6]*hs_line[:3]+hs_line[3:6])))<0.000001):
                    flag = 1
                    break
            if(flag==0):
                self.hs_pro_points.append(hs_line[6]*hs_line[:3]+hs_line[3:6])
            flag = 0
            for point in self.hs_pro_points:
                if(abs(np.dot(point-(hs_line[7]*hs_line[:3]+hs_line[3:6]),point-(hs_line[7]*hs_line[:3]+hs_line[3:6])))<0.000001):
                    flag = 1
                    break
            if(flag==0):
                self.hs_pro_points.append(hs_line[7]*hs_line[:3]+hs_line[3:6])   
        
        self.hs_pro_points=np.array(self.hs_pro_points)

    def draw_bulkBZ(self):
        """
        Draw the bulk BZ

        Returns:
            fig, ax: the figure and axis of the plot

        """
        x = self.hs_points[:,0]
        y = self.hs_points[:,1]
        z = self.hs_points[:,2]
        fig = plt.figure()
        ax = Axes3D(fig)
        ax.scatter(x,y,z)
        for i in self.hs_lines_f:
            start = i[6]*i[:3]+i[3:6]
            end = i[7]*i[:3]+i[3:6]
            ax.plot([start[0],end[0]],[start[1],end[1]],[start[2],end[2]])
        plt.show()
        
        return fig, ax
    
    def draw_SurfaceBulkBZ(self):
        """
        Draw the surface BZ and the bulk BZ

        Returns:
            fig, ax: the figure and axis of the plot
        """

        x = self.hs_points[:,0]
        y = self.hs_points[:,1]
        z = self.hs_points[:,2]
        x_pro = self.hs_pro_points[:,0]
        y_pro = self.hs_pro_points[:,1]
        z_pro = self.hs_pro_points[:,2]
        fig = plt.figure()
        ax = Axes3D(fig)
        ax.scatter(x,y,z)
        ax.scatter(x_pro,y_pro,z_pro)
        for i in self.hs_lines_f:
            start = i[6]*i[:3]+i[3:6]
            end = i[7]*i[:3]+i[3:6]
            ax.plot([start[0],end[0]],[start[1],end[1]],[start[2],end[2]])

        for i in self.hs_lines_pro_f:
            start = i[6]*i[:3]+i[3:6]
            end = i[7]*i[:3]+i[3:6]
            ax.plot([start[0],end[0]],[start[1],end[1]],[start[2],end[2]])
        plt.show()
        return fig,ax