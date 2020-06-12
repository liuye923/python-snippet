#reshape monthly data to year-month
#dat is a xarray dataframe
import pandas as pd

yyyymm = pd.MultiIndex.from_arrays([dat.coords['time.year'], dat.coords['time.month']], name=('year', 'month'))
dat.coords['yyyymm'] = ('time', yyyymm)
dat = dat.swap_dims({'time': 'yyyymm'})

dat_year_mont = dat.unstack()
