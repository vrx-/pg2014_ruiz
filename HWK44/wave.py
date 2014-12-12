import numpy as np
import sys
from matplotlib import pyplot as plt
import netCDF4
import os.path


g=9.8

class Wave(object):
    """
    1D wave equation class
    u[1:-1] = u[1:-1] - (dt*g/dx)*(eta[1:]-eta[:-1])
    eta = eta - (dt*H/dx)*(u[1:]-u[:-1]

    Default arguments: 
        values: 
         dx=100, L=10000, H=10, g=9.8
        functions: 
         H(flat bottom, depth=10), u(zero for all grid points), eta(zero for all grid points except left boundary, eta[0]=1)
    
    Variables
    dx:  grid size, type:int or float
    L:   channel lenght, type:int or float
    dt:  time step, type:int or float
    t:   time, type:int or float
    H:   depth (bottom), can be flat (type:int), or not (type:list or array)
    g:   gravitational acceleration, type:float
    u:   1d velocity field, (type:list or array of size nx)
    eta: surface elevation, (type:list or array of size nx-1)
    nx:  number of grid points, nx=L/dx, type:int
    nt:  number of time steps, nt=t/dt, type:int
             
    
    1D grid scheme: (u points: x , eta points: o)
    
    nx:     0           1             2                      nx-2        nx-1
    grid
    points: x-----o-----x-------o-----x-----[.....]-----o-----x-----o-----x
    
    """
    
    def __init__(self, dx=100, L=10000, H=None, eta=None, u=None):
        
        
        nx= L/dx #number of space steps (dimenssion)
        #Bathymetry
        if H==None: H=10*np.ones(nx)
        if type(H)==int: H=H*np.ones(nx)
        else: H=np.asarray(H)
        if H.size!=nx:
            print "H.size incorrect, should be %i (nx) for this scenario" % nx-1
            sys.exit() 
    
        #initial conditions
        if u==None: 
            u=np.zeros(nx+1)
        else: 
            u=np.asarray(u)
        if u.size!=nx+1: 
            print "u.size incorrect, should be %i (nx-1) for this scenario" % nx
            sys.exit()
        
        if eta==None: 
            eta=np.zeros(nx)
            eta[0]=1
        else: eta=np.asarray(eta)
        if eta.size!=nx: 
            print "eta.size incorrect, should be %i (nx-1) for this scenario" % nx-1
            sys.exit()
   
        #model initialization
        self.L=L 
        self.dx=dx
        self.nx=nx 
        self.bathy=H 
        self.etao=eta
        self.eta=eta
        self.uo=u
        self.u=u
        self.time=0
        self.dt='Not defined. Use forward method to define t and dt' 
        self.nt=0
        self.gridu=np.linspace(0,L,nx+1)
        self.grideta=self.gridu[:-1]+5
        # self.state={'L':L, 'dx':dx, 'nx':nx,
        #             'batty':H,
        #             'eta':eta, 'u':u,
        #             't':0, 'dt':'Not defined. Use forward method to define t and dt', 'nt':0}
    
    def forward(self, t=100, dt=5.):
        """
        Steps the model forward in time, for the iner nodes (1 to nx-2)
        Velocity Boundary condition for all time steps: u[0]=0, u[-1]=0
        """
        nt= t/dt #number of time steps
        self.time=t
        self.dt=dt
        
        #equation constants
        s=self.dt/self.dx
        c1= g*s #constant for u equation
        c2= self.bathy*s #array of constants for eta equation
        
        #looping in time for the iner grid points
        n=0
        u=self.uo
        eta=self.etao
        while n<nt:
            n=n+1
            u[1:-1]=u[1:-1]-c1*(eta[1:]-eta[:-1])
            eta[:]=eta[:]-c2[:]*(u[1:]-u[:-1])

        #update state with last time step        
        self.nt=+n
        self.u=np.vstack((self.u,u))
        self.eta=np.vstack((self.eta,eta))

        
    def to_netcdf(self, filename):
        """dumps the actuall time step to a netcdf file"""

        nc = netCDF4.Dataset(filename, 'w', clobber=True)
        
        nc.createDimension('x_u', self.nx+1)
        nc.createDimension('x_eta', self.nx)
        nc.createDimension('time', None)
        
        nc.createVariable('u', 'd', ('time', 'x_u'))
        nc.createVariable('eta', 'd', ('time', 'x_eta'))
        nc.variables['u'][:] = self.u
        nc.variables['eta'][:] = self.eta
        
        nc.createVariable('xu', 'd', ('x_u',))
        nc.createVariable('xeta', 'd', ('x_eta',))
        nc.createVariable('time', 'd', ('time',))
                        
        nc.variables['xu'][:] = self.gridu
        nc.variables['xeta'][:] = self.grideta
        nc.variables['time'][:] = [self.dt*i for i in range(self.nt)] 
        nc.close()
        
        
if __name__=='__main__':
        wave=Wave()    
        U=np.zeros((10, wave.nx+1))
        eta=np.zeros((10,(wave.nx)))
        U[0,:]=wave.uo
        eta[0,:]=wave.etao
        for i in range(1,10):
                wave.forward()
                U[i,:]=wave.u[-1]
                eta[i,:]=wave.eta[-1]
        wave.to_netcdf('wave.nc')
        xu,yu=np.meshgrid(wave.gridu, 100*np.arange(0,10))
        xeta,yeta=np.meshgrid(wave.grideta, 100*np.arange(0,10))
        f, axarr = plt.subplots(2, sharex=True)
        
        axarr[0].pcolor(xeta,yeta, eta)
        axarr[0].set_title('Surface elevation')
        axarr[1].pcolor(xu,yu, U)
        axarr[1].set_title('u')
        plt.show()
        