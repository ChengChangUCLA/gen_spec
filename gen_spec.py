from DRC import *
from TOTEM import *


# Cell Parameters
type = "p"
l = 35
w = 340
nf = 4
v = "svt"


# Cell Class
class Cell():
    
    def __init__(self, type, l, w, nf, v):
        self.type = type
        self.l = l
        self.w = w
        self.nf = nf
        self.v = v
        self.totem_list = []
        self.check()
        
    def check(self):
        if self.type != "p" and self.type != "n":
            assert(False)
        if self.l not in LENGTH_OPTIONS:
            assert(False)
        if self.w < PMOS_MIN_CHANNEL_WIDTH or self.w > PMOS_MAX_CHANNEL_WIDTH:
            assert(False)
        if self.w %5 != 0:
            assert(False)
        if self.nf not in NF_OPTIONS:
            assert(False)
        
    def construct(self):
        self.place_vdd()
        self.place_po(M1_S)
        
        if nf >= 2:
            self.place_po_m1_m2("s")
        else:
            self.place_po_m1(HEIGHT[1])
            
        if self.w > PMOS_REF_CHANNEL_WIDTH:
            h1 = self.w - PMOS_REF_CHANNEL_WIDTH + HEIGHT[2]
        else:
            h1 = HEIGHT[2]
        self.place_po_m1(h1)
        
        if nf <= 2:
            self.place_po_m1(HEIGHT[1])
        else:
            self.place_po_m1_m2("d")
            
        self.place_po(HEIGHT[3])
        self.place_gate()
        self.place_empty(CELL_HIGHT - 2*HEIGHT[0] - M1_S - 2*HEIGHT[1] - h1 - HEIGHT[3] - HEIGHT[4])
        self.place_vss()
        
    def place_vdd(self):
        vdd_list = []
        for i in range(self.nf):
            vdd_list.append(TOTEM_VDD)
        self.totem_list.append(vdd_list)
        
    def place_po(self, height):
        n_row = height // GRID_SIZE
        for n in range(n_row):
            po_list = []
            for i in range(self.nf):
                po_list.append(TOTEM_PO)
            self.totem_list.append(po_list)
        
    def place_po_m1_m2(self, pin):
        if pin == "s":
            po_m1_m2_list = []
            for i in range(self.nf):
                if i %2 == 0:
                    po_m1_m2_list.append(TOTEM_PMOS[0])
                else:
                    po_m1_m2_list.append(TOTEM_PMOS[1])
        if pin == "d":
            po_m1_m2_list = []
            for i in range(self.nf):
                if i == 0:
                    po_m1_m2_list.append(TOTEM_PMOS[5])
                elif i == self.nf - 1:
                    po_m1_m2_list.append(TOTEM_PMOS[3])
                elif i %2 == 0:
                    po_m1_m2_list.append(TOTEM_PMOS[4])
                else:
                    po_m1_m2_list.append(TOTEM_PMOS[2])
        self.totem_list.append(po_m1_m2_list)

    def place_po_m1(self, height):
        n_row = height // GRID_SIZE
        for n in range(n_row):
            po_od_m1_list = []
            for i in range(self.nf):
                if i %2 == 0:
                    po_od_m1_list.append(TOTEM_PO_M1[0])
                else:
                    po_od_m1_list.append(TOTEM_PO_M1[1])
            self.totem_list.append(po_od_m1_list)
    
    def place_gate(self):
        gate_list = []
        for i in range(self.nf):
            gate_list.append(TOTEM_GATE)
        self.totem_list.append(gate_list)   
    
    def place_vss(self):
        vss_list = []
        for i in range(self.nf):
            vss_list.append(TOTEM_VSS)
        self.totem_list.append(vss_list)   
    
    def place_empty(self, height):
        n_row = height // GRID_SIZE
        for n in range(n_row):
            empty_list = []
            for i in range(self.nf):
                if i == 0:
                    empty_list.append(TOTEM_EMPTY[0])
                elif i == self.nf - 1:
                    empty_list.append(TOTEM_EMPTY[2])
                else:
                    empty_list.append(TOTEM_EMPTY[1])
            self.totem_list.append(empty_list)
    
    def show_list(self):
        for i in self.totem_list:
            print(i)
    
    def output_file(self, path):
        file = open(path, "w")
        file.write("BEGIN ARRAY\n")
        for row in self.totem_list:
            for totem in row:
                file.write(totem + " ")
            file.write("\n")
        file.write("END ARRAY\n")
        file.close()
    
    def draw_nw(self):
        pass
    
    def draw_pp(self):
        pass
    
    def draw_np(self):
        pass
    
    def draw_vth_vtl(self):
        pass


c = Cell(type=type, l=l, w=w, nf=nf, v=v)
c.construct()
c.show_list()
c.output_file("spec")

















