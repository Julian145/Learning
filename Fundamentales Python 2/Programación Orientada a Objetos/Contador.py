class Timer:
    h = 0
    m = 0
    s = 0
    h_str = ''
    m_str = ''
    s_str = ''
    format = ''
    def __init__(self, hor=0, min=0, seg=0):
        self.h = hor
        self.m = min
        self.s = seg 

    def __str__(self):
        self.format = ''
        #Parte para validar que los numeros no sean mayores del formato 23:59:59
        if self.s > 60:
            self.m = self.m + (self.s//60)
            try:
                self.s = (self.s%60)
            except:
                self.s=0
        if self.s == 60:
            self.s = 0
            self.m += 1
        if self.s < 0:
            self.s = self.s + 60
            self.m = self.m + 59
            self.h = self.h + 23

        if self.m > 60:
            self.h = self.h + (self.m//60)
            try:
                self.m = (self.m%60)
            except:
                self.m=0
        if self.m == 60:
            self.m = 0
            self.h += 1
        if self.h >= 24:
            self.h = (self.h%24)
        if self.h<10:
            self.h_str = '0'+ str(self.h)
        else:
            self.h_str = str(self.h)
        if self.m<10:
            self.m_str = '0'+ str(self.m)
        else:
            self.m_str = str(self.m)
        if self.s<10:
            self.s_str = '0'+ str(self.s)
        else:
            self.s_str = str(self.s)
        self.format = self.format + self.h_str + ':' + self.m_str + ':' + self.s_str
        return self.format

    def next_second(self):
        self.s = self.s + 1
    def prev_second(self):
        self.s = self.s - 1
        self.__str__()

timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)