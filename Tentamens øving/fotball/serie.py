from lag import Lag

class Serie():
    def __init__(self, navn) -> None:
        self._navn = navn
        self._lag = []

    
    def hent_nav(self):
        return self._navn
    
    def hent_lagliste(self):
        return self._lag
    
    def legg_til_lag(self, lag: Lag):
        self._lag.append(lag)
    
    def spill_kamp(self, hjemmelag:Lag, bortelag: Lag, hjemmemaal: int, bortemaal: int ):
        if hjemmemaal > bortemaal:
            hjemmelag.seier()
            bortelag.tap()
        elif bortemaal > hjemmemaal:
            bortelag.seier()
            hjemmelag.tap()
        else:
            hjemmelag.uavgjort()
            bortelag.uavgjort()

    def finn_spiller(self, navn: str):
        for lag in self._lag:
           return lag.finn_spiller(navn)
            
            