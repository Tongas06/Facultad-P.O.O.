#%%
from manejador_facultades import ManejadorFacultades
#%%
mf = ManejadorFacultades()
#%%
mf.cargar_facultades()
#%%
facultades = mf.get_facultades()
carreras = mf.get_carreras()
#%%
facultades[1].get_nombre()
#%%
carreras[3][3].get_nombre()