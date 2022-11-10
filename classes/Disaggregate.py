import numpy as np
from scipy import optimize
import math

class Disaggregate( object ):

    
    def newton( self, B, ip ):
        return (ip * (1 - np.exp(-B))) - (B)  


    def precip( self, row, MIN_INTERVAL ):
        
        disagg_values = []
        
        p = float(row[3])

        if p > 0:

            d = float(row[4])
            tp = float(row[5])
            if tp == 0.:
                tp = 0.001
            ip = float(row[6])
            B = optimize.newton( func=self.newton, x0=ip, args=(ip,) )
            b = B/tp
            risingCt = math.floor( (d*tp*60.) )
            fallingCt = math.floor( (d*(1-tp)*60.) )

            if (tp*d*60.) % 1. != 0:
                peakCt = 1
            else:
                peakCt = 0
    
            interval = 0
            
            i_values = []
            t = 0.
            for interval in range(risingCt):
                t_hrs = (interval+1.) / 60.
                t = t_hrs / d
                i_value = ip*math.exp( b*(t-tp) )
                i_values.append( i_value )
    
            if peakCt == 1:
                t_hrs = (interval+2.) / 60.
                tnext = t_hrs / d
                i_rising = ip
                i_falling = ip*math.exp( (-b*tp*(tnext-tp))/(1-tp) )
                i_values.append( i_rising*((tp-t)/(tnext-t)) + i_falling*((tnext-tp)/(tnext-t)) )
    
            for interval in range(fallingCt):
                t_hrs = (float(risingCt+peakCt) / 60.) + ((interval+1.) / 60.)
                t = t_hrs / d
                i_value = ip*math.exp( -b*tp*(t-tp)/(1-tp) )
                i_values.append( i_value )
    
            accum_values = []
            accumulation = 0
            for value in i_values:
                ip = value
                Ip = ip * (p/d)
                accum = Ip * (1./60.)
                accum_values.append( accum )        
                accumulation += accum
    
            for i, value in enumerate(accum_values[::MIN_INTERVAL]):
                disagg = sum(accum_values[i*MIN_INTERVAL:i*MIN_INTERVAL+MIN_INTERVAL])
                disagg_values.append( disagg )

        else:
            pass

        return disagg_values
    
    
    def temp( self, row, MIN_INTERVAL ):
        
        disagg_values = []
        
        tmin = float(row[8])
        tmax = float(row[7])
    
        daily_interval_n = int(1440./MIN_INTERVAL)
    
        for hr in np.linspace( 0., 24. - MIN_INTERVAL/60., daily_interval_n ):

            tinterval = (.525*tmax + 0.464*tmin - 0.229) + (((tmax - tmin)/2.) * (np.cos((np.pi*(hr - 15.))/12.)))
            
            disagg_values.append( tinterval )
            
        return disagg_values
            
    
    def dewpt( self, row, rownext, MIN_INTERVAL ):

        disagg_values = []        

        k = 6.

        tdew = float(row[12])
        tdewnext = float(rownext[12])

        daily_interval_n = int(1440./MIN_INTERVAL)
    
        for hr in np.linspace( 0., 24. - MIN_INTERVAL/60., daily_interval_n ):

            tdelta = 0.5*np.sin( (hr+1.)*(np.pi/k) - (3.*np.pi/4.) )
            tinterval = tdew + (hr/24.) * (tdewnext - tdew) + tdelta

            disagg_values.append( tinterval )

        return disagg_values        
        

    def solrad( self, row, jday, lat, lon, MIN_INTERVAL ):

        disagg_values = []        

        daily_interval_n = int(1440./MIN_INTERVAL)        

        latrad = lat*np.pi/180.

        standardmeridian = 15.*math.floor( lon/15. )

        angularfractionofyear = 2.*np.pi*( math.floor( jday ) - 1.) / 365.
    
        equationoftime = .170*np.sin( 4.*np.pi*(math.floor( jday ) - 80.) / 373. ) \
                        - .129*np.sin( 2.*np.pi*(math.floor( jday ) - 8.) / 355. )
    
        solardeclination = .006918 - .399912*np.cos( 1.*angularfractionofyear )    \
                          + .070257*np.sin( 1.*angularfractionofyear )             \
                          - .006758*np.cos( 2.*angularfractionofyear )             \
                          + .000907*np.sin( 2.*angularfractionofyear )             \
                          - .002697*np.cos( 3.*angularfractionofyear )             \
                          + .001480*np.sin( 3.*angularfractionofyear )             \
    
        avgsolrad = float(row[9]) * 41840. / 86400.
    
        clearskies = []
        for hr in np.linspace( 0., 24. - MIN_INTERVAL/60., daily_interval_n ):
    
            localhourangle = 2.*np.pi/24.*(hr - (lon-standardmeridian)*24./360. + equationoftime - 12.)
    
            solaraltitude = np.arcsin( np.sin( latrad )*np.sin( solardeclination )    \
                                      + np.cos( latrad )*np.cos( solardeclination )    \
                                      * np.cos( localhourangle ) ) * 180./np.pi
    
            if solaraltitude > 0.:
    
                clearsky = 24.*(2.044*solaraltitude + .1296*solaraltitude**2           \
                              - .001941*solaraltitude**3 + .000007591*solaraltitude**4)*.1314
    
                clearskies.append( clearsky )
            
            else:
                
                clearsky = 0.
                clearskies.append( clearsky )

        avgclearsky = sum(clearskies)/24.
        disagg_values = [elem * avgsolrad / avgclearsky for elem in clearskies]
        
        return disagg_values
    
    def windspeed( self, row, MIN_INTERVAL ):        
        
        disagg_values = []
        daily_interval_n = int(1440./MIN_INTERVAL)      
        speed = float(row[10])

        for hr in np.linspace( 0., 24. - MIN_INTERVAL/60., daily_interval_n ):
            
            hrspeed = speed + 0.5*speed*np.cos( np.pi*(hr - 14.)/12. )
            disagg_values.append( hrspeed )
        
        return disagg_values

        
        
        
