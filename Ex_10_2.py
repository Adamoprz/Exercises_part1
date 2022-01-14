class Pojazdy:
    def __init__(self, **kwargs):
        pr_max = kwargs['pr_max']
        nr_poj = kwargs['nr_poj']
        nr_zaj = kwargs['nr_zaj']


    def __str__(self):
        pass
        #return f"{self.name}"
    def __zajezdnia__(self):
        pass

class Pojazdy_miejske(Pojazdy):
    def __init__(self):
        super().__init__()

class Pojazdy_miejskie_tramwaje(Pojazdy_miejske):
    def __init__(self):
        super().__init__()

class Pojazdy_miejskie_autobusy(Pojazdy_miejske):
    def __init__(self):
        super().__init__()